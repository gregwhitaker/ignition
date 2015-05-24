#! /bin/bash

wait_for_stack() {
	echo -n "Waiting for stack to complete"
    TEST_CONTENT=$(aws cloudformation describe-stacks --stack-name $1 --region $REGION | grep \"StackStatus\")

    CREATE_COMPLETE=$(echo $TEST_CONTENT | grep 'CREATE_COMPLETE' | wc -l)
    while [[ $CREATE_COMPLETE -lt 1 && $UPDATE_COMPLETE -lt 1 && $ROLLBACK -lt 1 ]]; do
        sleep 2
        echo -n "."

        TEST_CONTENT=$(aws cloudformation describe-stacks --stack-name $1 --region $REGION | grep \"StackStatus\")
        CREATE_COMPLETE=$(echo $TEST_CONTENT | grep 'CREATE_COMPLETE' | wc -l)
        UPDATE_COMPLETE=$(echo $TEST_CONTENT | grep 'UPDATE_COMPLETE' | wc -l)
        ROLLBACK=$(echo $TEST_CONTENT | grep 'ROLLBACK_COMPLETE' | wc -l)
    done

    echo ""

    RETURN_VAL=0
    if [ "$ROLLBACK" == "1" ]; then
        RETURN_VAL=1
    fi

    return $RETURN_VAL
}

function find_cloudformation_bucket() {
	# This should return the name of a bucket created via cloudformation
}