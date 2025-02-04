import boto3
import os
import layerutils as p


def lambda_handler(event, context):


    statement = p.getParameter(os.environ['PARAMETER_NAME'])

    #c = boto3.client('ssm')
    #r = c.get_parameter(Name=parameterName)
    #statament = r['Parameter']['Value']


    if statement == "true":
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
            "bodyMessage": "Morre, diabo.",
            "logMessage": "Perdeu."
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
    "logMessage": "Welcome!"
     }
    }
