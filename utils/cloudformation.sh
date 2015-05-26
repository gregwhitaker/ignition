#! /bin/bash

#/ Usage: wait_for_stack <stack>
#/ Waits for a CloudFormation stack to complete.
wait_for_stack() {
	echo -n "$(tput setaf 2)Waiting for '$(tput setaf 3)$1$(tput setaf 2)' stack to complete $(tput sgr0)"
    TEST_CONTENT=$(aws cloudformation describe-stacks --stack-name $1 --region $REGION | grep \"StackStatus\")

    if [ $? != 0 ]; then
        exit 1
    fi

    CREATE_COMPLETE=$(echo $TEST_CONTENT | grep 'CREATE_COMPLETE' | wc -l)
    while [[ $CREATE_COMPLETE -lt 1 && $UPDATE_COMPLETE -lt 1 && $ROLLBACK -lt 1 ]]; do
        sleep 2
        echo -n "$(tput setaf 2).$(tput sgr0)"

        TEST_CONTENT=$(aws cloudformation describe-stacks --stack-name $1 --region $REGION | grep \"StackStatus\")
        CREATE_COMPLETE=$(echo $TEST_CONTENT | grep 'CREATE_COMPLETE' | wc -l)
        UPDATE_COMPLETE=$(echo $TEST_CONTENT | grep 'UPDATE_COMPLETE' | wc -l)
        ROLLBACK=$(echo $TEST_CONTENT | grep 'ROLLBACK_COMPLETE' | wc -l)
    done

    RETURN_VAL=0
    if [ "$ROLLBACK" == "1" ]; then
        echo -e "$(tput setaf 1)ROLLBACK$(tput sgr0)"
        RETURN_VAL=1
    else
        echo " $(tput setaf 2)[$(tput setaf 3) COMPLETE $(tput setaf 2)]$(tput sgr0)"
    fi

    return $RETURN_VAL
}

#/ Usage: find_resource_created_by_cloudformation <stack> <resource>
#/ Gets the name of the resource created using CloudFormation.
find_resource_created_by_cloudformation() {
	CF_RESX=$(aws --output text cloudformation describe-stack-events --stack-name $1 --region $REGION \
		| grep $2 \
		| grep 'CREATE_COMPLETE' \
		| cut -f 4)
}