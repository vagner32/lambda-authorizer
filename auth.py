import boto3

def lambda_handler(event, context):

    c = boto3.client('ssm')
    r = c.get_parameter(Name='YouShallNotPass')
    statament = r['Parameter']['Value']


    if statament == "true":
        return {
        "principalId": "user",
        "policyDocument": {
        "Version": "2012-10-17",
        "Statement": [
        {
            "Action": "execute-api:Invoke",
            "Effect": 'Deny',
            "Resource": '*'
        }
                    ]
        },
            "context": {
            "message": "Keep Out!"
        }
    }

    return {
        "principalId": "user",
        "policyDocument": {
        "Version": "2012-10-17",
        "Statement": [
        {
            "Action": "execute-api:Invoke",
            "Effect": 'Allow',
            "Resource": '*'
        }
                    ]
    },
    "context": {
    "message": "Welcome!"
     }
    }
