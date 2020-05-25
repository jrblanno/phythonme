import azure.common
from azure.storage import CloudStorageAccount ,SharedAccessSignature
from azure.storage.table import TableService, Entity
import config
class azuretabla():
    account_connection_string = config.STORAGE_CONNECTION_STRING
    # Split into key=value pairs removing empties, then split the pairs into a dict
    konfig = dict(s.split('=', 1) for s in account_connection_string.split(';') if s)
    # Authentication
    account_name = konfig.get('AccountName')
    account_key = konfig.get('AccountKey')
    # Basic URL Configuration
    table_service = TableService(account_name = account_name, account_key = account_key)
    table_name = 'bilfingerareas'
    # Create a sample entity to insert into the table
    #customer = {'PartitionKey': 'Harp', 'RowKey': '1', 'email' : 'harp@contoso.com', 'phone' : '555-555-5555'}
    # Insert the entity into the table
    #print('Inserting a new entity into table - ' + table_name)
    #table_service.insert_entity(table_name, customer)
    #print('Successfully inserted the new entity')
    # Demonstrate how to query the entity
    #print('Read the inserted entity.')
    entity = table_service.get_entity(table_name, 'Harp', '1')
    mail = (entity['email'])
    phone = (entity['phone'])