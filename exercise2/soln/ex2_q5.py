#Recommended to use python try-except block to perform error handling.
from pprint import pprint 
#use pprint instead of print to clearly print output documents
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,OperationFailure
connectionString=''
#enter your connection String here
client=MongoClient(connectionString)

try:
    client.admin.command('ismaster')

except ConnectionFailure:
    print('Server not available')
    
except OperationFailure:
    print('wrong credentials')
    
else:
    print('connected to database')
    # write your code here
    
finally:
	client.close()