import json
import boto3
import time
from decimal import Decimal
dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key, Attr

# function to be called by Connect to check current date/time against Holiday
# Dates database to determine if today is a holiday and greet customer as such

def lambda_handler(event, context):
    # pull table of Holiday timestamps from DynamoDB
    table = dynamodb.Table('HolidayDates')
    # pull current timestamp
    currentTimestamp = int(round(time.time() * 1000))
    # check if current Timestamp is a holiday date 
    # (i.e. between start and end timestamps of holiday dates)
    response = table.scan(
        FilterExpression = Attr("dateStart").lte(currentTimestamp) & Attr("dateEnd").gte(currentTimestamp)
        )
    # if no matches for a holiday in database, return false
    if response["Count"] == 0:
        return {
            "holiday": "False",
            "name": "noHoliday"
        }
    # if a match for a holiday in database, return true
    else:
        return {
            "holiday": "True",
            "name": response["Items"][0]["name"]
        }
