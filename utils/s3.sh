#! /bin/bash

function find_bucket() {
  BUCKET_NAME=$1
  OUTPUT=$(aws s3 ls s3://$BUCKET_NAME 2>&1)
  return $?
}

function flush_bucket() {
  BUCKET_NAME=$1
  echo “Flushing bucket $BUCKET_NAME"
  find_bucket $BUCKET_NAME
  if [ $? -ne 0 ]; then
    echo "Bucket not found"
  else
    aws s3 rm "s3://$BUCKET_NAME" --region $REGION --recursive
  fi
}
