import json
import boto3
import time
from decimal import Decimal
dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key, Attr

# function to remove an entry from the Holiday Dates database via the DynamoDB
# API. To be called via the admin website

def lambda_handler(event, context):
    # import HolidayDates DynamoDB database 
    table = dynamodb.Table('HolidayDates')
    
    # pull event context data 
    input = json.loads(event["body"])
    
    # make call to delete entry via API
    response = table.delete_item(
        Key = {
            "dateStart": int(input["dateStart"]),
        }
    )
    
    # return success alert
    output = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        },
        "body": json.dumps({"message":"successful!"})
    }
    
    return output
        
        