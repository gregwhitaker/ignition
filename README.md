#Ignition
A scriptable installer for automating the configuration of AWS accounts.

Ignition allows you to automate the creation and setup of the following:

* VPC Layout
* IAM Groups and Roles
* CloudFormation
* CloudTrail
* Config
* KMS
* Security Groups

##Prerequisites
Ignition requires the following packages to be installed before use:

* Python 2.6.3 or later
* Pip

First, check to see if you already have Python installed:
	
	$ python --version
	
If you don't have Python installed, download the package from [python.org](https://www.python.org/downloads/) and run the installer or use your distribution's package manager.

##Installation
Run the Ignition installer to prepare your system to begin automation of your AWS account:

	$ ./ignition.sh --install

##Getting Started
Ignition provides two different modes for configuring your AWS account.

* Interactive - Console application that guides you through the configuration process.
* Scripted - Loads a configuration file and configures the account in a headless process.

###Interactive Configuration
Ignition provides an interactive console application to guide you through the configuration process.

	$ ./ignition

###Scripted Configuration
Ignition provides a scripted configuration process that loads a specially formatted configuration file and 
configures the account in a headless process.

	$ ./ignition --configuration-file <file>