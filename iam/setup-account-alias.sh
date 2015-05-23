#! /bin/bash

source ../utils/logging.sh

aws iam create-account-alias --account-alias $1
