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
