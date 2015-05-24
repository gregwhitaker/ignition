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
  echo "$(tput setaf 2)Flushing bucket: $(tput setaf 3)$BUCKET_NAME$(tput sgr0)"
  find_bucket $BUCKET_NAME
  if [ $? -ne 0 ]; then
    echo "Bucket not found!"
  else
    aws s3 rm "s3://$BUCKET_NAME" --region $REGION --recursive
  fi
}