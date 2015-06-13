Key Management Service
===
AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.

##Setup Master Key
Creates a master encryption key in KMS.

	$ python master_key.py --setup --region REGION [--alias ALIAS]

If a key alias is not supplied the script assumes an alias of "master".

##Teardown Master Key
Disables a master encryption key in KMS and deletes the alias so that it may be used by another key.

	$ python master_key.py --teardown --region REGION [--alias ALIAS]

If a key alias is not supplied the script assumes an alias of "master".
