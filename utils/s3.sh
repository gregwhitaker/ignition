#! /bin/bash

#/ Usage: find_bucket <bucket>
#/ Finds an S3 Bucket by name.
find_bucket() {
  BUCKET_NAME=$1
  OUTPUT=$(aws s3 ls s3://$BUCKET_NAME 2>&1)
  return $?
}

#/ Usage: delete_bucket <bucket>
#/ Deletes an S3 Bucket.
delete_bucket() {
  BUCKET_NAME=$1
  echo “Flushing bucket $BUCKET_NAME"
  find_bucket $BUCKET_NAME
  if [ $? -ne 0 ]; then
    echo "Bucket not found"
  else
    delete_bucket $BUCKET_NAME
  fi
}

