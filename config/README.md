Config
===
AWS Config is a fully managed service that provides you with an AWS resource inventory, configuration history, and configuration change notifications to enable security and governance. With AWS Config you can discover existing AWS resources, export a complete inventory of your AWS resources with all configuration details, and determine how a resource was configured at any point in time. These capabilities enable compliance auditing, security analysis, resource change tracking, and troubleshooting.

The Config scripts can be used to configure the following:

* Enable Config

##setup-config
Enables AWS Config on the account.

	$ ./setup-config.sh

##teardown-config
Disables AWS Config on the account.

	$ ./teardown-config.sh