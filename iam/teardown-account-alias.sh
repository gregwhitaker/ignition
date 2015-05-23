#! /bin/bash

source ../utils/logging.sh

aws iam delete-account-alias --account-alias $1