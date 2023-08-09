from celery import shared_task
from bson import ObjectId
from database.database import connection
import json
from datetime import datetime, timedelta
import requests
import requests
from bson import json_util


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='User:Create New Conversation.')
def savingChat(self,data):
    database,client = connection()
    try:
        database["conversations"].insert_one(data)
    except Exception as e:
        print("Exception here :",e)
        pass
    client.close()

@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='User:Get All Conversation.')
def GetAllChat(self):
    database,client = connection()
    try:
        data=database["conversations"].find({},{'_id': 0})
        data = json_util.dumps(data)
        client.close()
    except Exception as e:
        print("Exception here :",e)
    return data


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='User:Get Conversation by session id')
def GetChatBySessionId(self,id):
    database,client = connection()
    try:
        filter = {'sessionID':id}
        filter_2 = {"_id": 0}
        data=database["conversations"].find(filter,filter_2)
        data = json_util.dumps(data)
        client.close()
    except Exception as e:
        print("Exception here :",e)
    return data



@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='user:Update Message In A Conversation.')
def updateUser(self,data):
    database,client = connection()
    filter = { "_id": ObjectId(data["id"]) }
    del data["id"]
    newvalues = { "$set": data }
    try:
        database["conversations"].update_one(filter,newvalues)
        client.close()
    except Exception as e:
        print("Exception here :",e)
        pass


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='user:Delete User Conversation.')
def deleteUser(self,data):
    database,client = connection()
    filter = { "_id": ObjectId(data["id"]) }
    try:
        database["conversations"].delete_one(filter)
        client.close()
    except Exception as e:
        print("Exception here :",e)
        pass

