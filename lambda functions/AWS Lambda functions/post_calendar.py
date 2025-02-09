import json
import boto3
import hashlib
import decimal

def lambda_handler(event, context):
    # TODO implement
    print(event)
    user_id = event['user_id']
    user_profile = check_user(user_id)
    completion_level = event['page_num']
    if int(user_profile['completion_level']) < 3:
        update_user_level(user_id)
    delete_user_calendar(user_id)
    first_date = event['first_date']
    last_date = event['last_date']
    monday_breakfast = event['monday_breakfast']
    monday_lunch = event['monday_lunch']
    monday_snack = event['monday_snack']
    monday_dinner = event['monday_dinner']
    tuesday_breakfast = event['tuesday_breakfast']
    tuesday_lunch = event['tuesday_lunch']
    tuesday_snack = event['tuesday_snack']
    tuesday_dinner = event['tuesday_dinner']
    wednesday_breakfast = event['wednesday_breakfast']
    wednesday_lunch = event['wednesday_lunch']
    wednesday_snack = event['wednesday_snack']
    wednesday_dinner = event['wednesday_dinner']
    thursday_breakfast = event['thursday_breakfast']
    thursday_lunch = event['thursday_lunch']
    thursday_snack = event['thursday_snack']
    thursday_dinner = event['thursday_dinner']
    friday_breakfast = event['friday_breakfast']
    friday_lunch = event['friday_lunch']
    friday_snack = event['friday_snack']
    friday_dinner = event['friday_dinner']
    saturday_breakfast = event['saturday_breakfast']
    saturday_lunch = event['saturday_lunch']
    saturday_snack = event['saturday_snack']
    saturday_dinner = event['saturday_dinner']
    sunday_breakfast = event['sunday_breakfast']
    sunday_lunch = event['sunday_lunch']
    sunday_snack = event['sunday_snack']
    sunday_dinner = event['sunday_dinner']
    if user_profile:
        insert_meal_calendar(user_id,first_date,last_date,monday_breakfast,
        monday_lunch,monday_snack,monday_dinner,
        tuesday_breakfast,tuesday_lunch,tuesday_snack,tuesday_dinner,
        wednesday_breakfast,wednesday_lunch,wednesday_snack,wednesday_dinner,
        thursday_breakfast,thursday_lunch,thursday_snack,thursday_dinner,
        friday_breakfast,friday_lunch,friday_snack,friday_dinner,
        saturday_breakfast,saturday_lunch,saturday_snack,saturday_dinner,
        sunday_breakfast,sunday_lunch,sunday_snack,sunday_dinner)
        return {
        'statusCode': 200,
        'body': json.dumps('timings for all meals added to the database')
        }
    return {
        'statusCode': 200,
        'body': json.dumps('user does not exist')
    }
    
def update_user_level(user_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user_profile')
    response = table.update_item(
        Key={
            'user_id': user_id
        },
        UpdateExpression="set completion_level = :r",
        ExpressionAttributeValues={
            ':r': '3'
        },
        ReturnValues="UPDATED_NEW"
    )
    print("UpdateItem succeeded:")
    print(response)
    
def check_user(user_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user_profile')
    response = table.get_item(
        Key={
            'user_id': user_id
        }
    )
    if 'Item' in response:
        print("GetItem succeeded:")
        return response['Item']
    return False
    
def insert_meal_calendar(user_id,first_date,last_date,monday_breakfast,
        monday_lunch,monday_snack,monday_dinner,
        tuesday_breakfast,tuesday_lunch,tuesday_snack,tuesday_dinner,
        wednesday_breakfast,wednesday_lunch,wednesday_snack,wednesday_dinner,
        thursday_breakfast,thursday_lunch,thursday_snack,thursday_dinner,
        friday_breakfast,friday_lunch,friday_snack,friday_dinner,
        saturday_breakfast,saturday_lunch,saturday_snack,saturday_dinner,
        sunday_breakfast,sunday_lunch,sunday_snack,sunday_dinner):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('calendar')
    response = table.put_item(
        Item={
            'user_id':user_id,
            'first_date':first_date,
            'last_date':last_date,
            'monday_breakfast': monday_breakfast,
            'monday_lunch': monday_lunch,
            'monday_snack': monday_snack,
            'monday_dinner': monday_dinner,
            'tuesday_breakfast': tuesday_breakfast,
            'tuesday_lunch': tuesday_lunch,
            'tuesday_snack': tuesday_snack,
            'tuesday_dinner': tuesday_dinner,
            'wednesday_breakfast': wednesday_breakfast,
            'wednesday_lunch': wednesday_lunch,
            'wednesday_snack': wednesday_snack,
            'wednesday_dinner': wednesday_dinner,
            'thursday_breakfast': thursday_breakfast,
            'thursday_lunch': thursday_lunch,
            'thursday_snack': thursday_snack,
            'thursday_dinner': thursday_dinner,
            'friday_breakfast': friday_breakfast,
            'friday_lunch': friday_lunch,
            'friday_snack': friday_snack,
            'friday_dinner': friday_dinner,
            'saturday_breakfast': saturday_breakfast,
            'saturday_lunch': saturday_lunch,
            'saturday_snack': saturday_snack,
            'saturday_dinner': saturday_dinner,
            'sunday_breakfast': sunday_breakfast,
            'sunday_lunch': sunday_lunch,
            'sunday_snack': sunday_snack,
            'sunday_dinner': sunday_dinner
        }
    )
    print("PutItem succeeded:")
    print(response)
    
def delete_user_calendar(user_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('calendar')
    response = table.delete_item(
        Key={
            'user_id': user_id
        }
    )
    print("Delete Item succeeded:")
    print(json.dumps(response, indent=4))