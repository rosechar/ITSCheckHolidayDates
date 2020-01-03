import json
import boto3
dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key, Attr

# function to add an entry to the Holiday Dates database via the DynamoDB
# API. To be called via the admin website

def lambda_handler(event, context):
    # pull table of Holiday timestamps from DynamoDB
    table = dynamodb.Table('HolidayDates')
    
    # pull event context for dateStart, dateEnd, and name input from admin website
    input = json.loads(event["body"])
    
    # add entry in database via DynamoDB API
    response = table.put_item(
        Item = {
            "dateStart": input["dateStart"],
            "dateEnd":  input["dateEnd"],
            "name": input["name"]
        }
        )
    
    # need to add logic to check if there is already an item with input key
    
    # return successful message 
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

