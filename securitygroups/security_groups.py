from colorama import Fore, init
import boto.ec2
import argparse
import json

class SecurityGroups:
    """
    Adds or removes the default security groups for a region.
    """

    def __init__(self, region, vpc_id, profile):
        """
        Creates an instance of SecurityGroups.

        :type region: str
        :type vpc_id: str
        :type profile: str
        :param region: AWS region
        :param vpc_id: VPC identifier (optional)
        :param profile: AWS credentials profile name (optional)
        """
        self.region = region
        self.vpc_id = vpc_id
        self.profile = profile

    def setup(self):
        """
        Adds the default security groups as well as ingress and egress rules.
        """
        config = self.__load_configuration()

        if self.profile is None:
            # Using the default profile
            ec2_conn = boto.ec2.connect_to_region(self.region)
        else:
            ec2_conn = boto.ec2.connect_to_region(self.region, profile_name=self.profile)

        groupdict = dict()
        for sg in config['securityGroups']:
            name = sg['groupName']
            desc = sg['description']

            if not self.vpc_id is None:
                response = ec2_conn.create_security_group(name, desc, self.vpc_id)
                print Fore.GREEN + "Created security group '" + Fore.YELLOW + name + Fore.GREEN + "' in vpc '" + Fore.YELLOW + self.vpc_id + Fore.GREEN + "'" + Fore.RESET
            else:
                response = ec2_conn.create_security_group(name, desc)
                print Fore.GREEN + "Created security group '" + Fore.YELLOW + name + Fore.GREEN + "' in vpc '" + Fore.YELLOW + 'default' + Fore.GREEN + "'" + Fore.RESET

            groupdict[name] = [response.id, response]

        for sg_config in config['securityGroups']:
            sg_id = groupdict[sg_config['groupName']][0]
            sg = groupdict[sg_config['groupName']][1]

            print Fore.GREEN + "Creating ingress rules for security group '" + Fore.YELLOW + sg_config['groupName'] + Fore.GREEN + "':" + Fore.RESET

            # Applying Inbound Rules Security Group
            for inboundRule in sg_config['rules']['inbound']:
                protocol = inboundRule['protocol']
                portRange = str(inboundRule['portRange'])
                source = inboundRule['source']

                ports = portRange.split("-", 1)

                if len(ports) == 1:
                    startPort = ports[0]
                    stopPort = ports[0]
                else:
                    startPort = ports[0]
                    stopPort = ports[1]

                if inboundRule['type'] == 'cidr':
                    sg.authorize(ip_protocol=protocol, from_port=startPort, to_port=stopPort, cidr_ip=source)
                    self.__log_rule_create(ip_protocol=protocol, from_port=startPort, to_port=stopPort, cidr_ip=source)
                elif inboundRule['type'] == 'sg-reference':
                    sg.authorize(ip_protocol=protocol, from_port=startPort, to_port=stopPort, src_group=groupdict[source][1])
                    self.__log_rule_create(ip_protocol=protocol, from_port=startPort, to_port=stopPort, src_group=source)
                else:
                    print Fore.RED + "Unknown ingress rule type '" + inboundRule['type'] + "'" + Fore.RESET
                    exit(1)

    def teardown(self):
        """
        Removes the default security groups as well as ingress and egress rules.
        """
        config = self.__load_configuration()

        if self.profile is None:
            # Using the default profile
            ec2_conn = boto.ec2.connect_to_region(self.region)
        else:
            ec2_conn = boto.ec2.connect_to_region(self.region, profile_name=self.profile)

        allgroups = ec2_conn.get_all_security_groups()

        idmap = dict()
        for sg_config in config['securityGroups']:
            for g in allgroups:
                if g.name == sg_config['groupName']:
                    idmap[sg_config['groupName']] = g.id

        for key, value in idmap.iteritems():
            mygroup = ec2_conn.get_all_security_groups(group_ids=value)
            groupname = mygroup[0].name
            groupid = mygroup[0].id
            group = mygroup[0]

            for rule in group.rules:
                for grants in rule.grants:
                    if grants.cidr_ip:
                        print "revoking ingress rule with source as cidr_ip"
                        print groupname, groupid, rule.ip_protocol, rule.from_port, rule.to_port, grants.cidr_ip
                        ec2_conn.revoke_security_group(group_id=groupid, ip_protocol=rule.ip_protocol, from_port=rule.from_port, to_port=rule.to_port, cidr_ip=grants.cidr_ip)
                    else:
                        print "revoking ingress rule with source as security group"
                        print groupname, groupid, rule.ip_protocol, rule.from_port, rule.to_port, grants.name
                        ec2_conn.revoke_security_group(group_id=groupid, ip_protocol=rule.ip_protocol, from_port=rule.from_port, to_port=rule.to_port, src_security_group_group_id=grants.name)

            # handle cases where the security group is referred to by other security groups
            for othergroup in allgroups:
                for otherrule in othergroup.rules:
                    for othergrant in otherrule.grants:
                        grant_nom = othergrant.name or othergrant.group_id
                        if grant_nom:
                            if grant_nom == groupid:
                                print "revoking ingress rule where source is the security group to be deleted"
                                print othergroup.name, otherrule.ip_protocol, otherrule.from_port, otherrule.to_port, othergrant.group_id
                                ec2_conn.revoke_security_group(group_id=othergroup.id, ip_protocol=otherrule.ip_protocol, from_port=otherrule.from_port, to_port=otherrule.to_port, src_security_group_group_id=groupid)

            # delete the security group itself
            print Fore.GREEN + "Deleting security group '" + Fore.YELLOW + key + Fore.GREEN + "'" + Fore.RESET
            ec2_conn.delete_security_group(group_id=groupid)

    def __load_configuration(self):
        """
        Loads the security group configuration file for the region specified when this class was initialized.
        :rtype: dict
        :return: config data
        """
        config_path = './configs/default-' + self.region + '.json'

        with open(config_path, "r") as config_file:
            data = config_file.read().replace('\n', '')
            json_data = json.loads(data)

        return json_data

    def __log_rule_create(self, **kwargs):
        """
        Logs the rule creation to console.
        """
        if 'cidr_ip' in kwargs:
            print Fore.GREEN + "  Created ip_protocol='" + Fore.YELLOW + kwargs['ip_protocol'] + Fore.GREEN + "' " + \
                  "from_port='" + Fore.YELLOW + kwargs['from_port'] + Fore.GREEN + "' " + \
                  "to_port='" + Fore.YELLOW + kwargs['to_port'] + Fore.GREEN + "' " + \
                  "cidr_ip='" + Fore.YELLOW + kwargs['cidr_ip'] + Fore.GREEN + "'"
        else:
            print Fore.GREEN + "  Created ip_protocol='" + Fore.YELLOW + kwargs['ip_protocol'] + Fore.GREEN + "' " + \
                  "from_port='" + Fore.YELLOW + kwargs['from_port'] + Fore.GREEN + "' " + \
                  "to_port='" + Fore.YELLOW + kwargs['to_port'] + Fore.GREEN + "' " + \
                  "src_group='" + Fore.YELLOW + kwargs['src_group'] + Fore.GREEN + "'"

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from utils.account_util import is_valid_region

        # Initializing colorama because this method is currently being called as a top-level script and not a module.
        init()
    else:
        from utils.account_util import is_valid_region

    parser = argparse.ArgumentParser(description="Adds or removes the default security groups.")

    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-s", "--setup", help="Adds the default security groups to the region.", action="store_true")
    command_group.add_argument("-t", "--teardown", help="Removes the default security groups from the region.", action="store_true")

    parser.add_argument("--region", required=True, action="store", dest="region", help="AWS region")
    parser.add_argument("--vpc-id", required=False, action="store", dest="vpc_id", help="VPC identifier")
    parser.add_argument("--profile", required=False, action="store", dest="profile", help="AWS credentials profile name")

    args = parser.parse_args()

    if is_valid_region(args.region):
        args.region = args.region.strip().lower()
    else:
        parser.error('Invalid region')

    master_key = SecurityGroups(args.region, args.vpc_id, args.profile)

    if args.setup:
        master_key.setup()
    elif args.teardown:
        master_key.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')
