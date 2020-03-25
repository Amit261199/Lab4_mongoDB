#Recommended to use python try-except block to perform error handling.
from pprint import pprint 
#use pprint instead of print to clearly print output documents
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,OperationFailure
ID='201701***'
# enter your id here.
host='localhost'
client=MongoClient('mongodb://'+ID+':'+ID+'@'+host+':27017/?authSource='+ID+'&readPreference=primary&ssl=false')

try:
    client.admin.command('ismaster')
    db=client[ID]

except ConnectionFailure:
    print('Server not available')
    
except OperationFailure:
    print('wrong credentials')
    
else:
    print('connected to database')
    # write your code here
    