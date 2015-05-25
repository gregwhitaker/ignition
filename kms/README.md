Key Management Service
===
AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.

##setup-master-key
Creates a master encryption key in KMS.

	$ ./setup-master-key [alias]

##teardown-master-key
Disables a master encryption key in KMS.

	$ ./teardown-master-key [alias]