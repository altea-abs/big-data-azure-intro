import auth
from storage_queue import StorageQueueClient

credential = auth.get_default_credential()
storage = 'tempbigdata'
queue_name = 'test'

client = StorageQueueClient(storage, queue_name, credential)

print('sending message')
#client.add_message('first test message')

print(client.receive_message())