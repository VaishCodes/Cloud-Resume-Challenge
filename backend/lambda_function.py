http://vaishnavi-cloud-resume.s3-website-euimport json
import boto3
from decimal import Decimal
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('resume-visitor-count')

def lambda_handler(event, context):
    try:
        response = table.get_item(
            Key={'ID': 'resume'}   # <-- use ID here
        )
        item = response.get('Item', {'ID': 'resume', 'count': 0})
        current_count = int(item.get('count', 0))

        new_count = current_count + 1

        table.put_item(
            Item={
                'ID': 'resume',    # <-- and here
                'count': Decimal(new_count)
            }
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"count": new_count})
        }

    except ClientError as e:
        print(e)
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Internal server error"})
        }
-west-1.amazonaws.com