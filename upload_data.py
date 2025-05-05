from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri="mongodb+srv://rohit8120sahu:iBX57K4Tqlb7FVuO@cluster0.majirey.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connected to server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

df=pd.read_csv("C:\Users\Administrator\Desktop\Sensor Project\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)