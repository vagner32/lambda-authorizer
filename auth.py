import boto3
import os

def lambda_handler(event, context):


    parameterName = os.environ['PARAMETER_NAME']
    c = boto3.client('ssm')
    r = c.get_parameter(Name=parameterName)
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
            "header-message": "Keep out!",
            "body-message": "Morre, diabo.",
            "log-message": "Perdeu."
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
    "log-message": "Welcome!"
     }
    }
