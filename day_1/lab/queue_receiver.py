import time
import auth
from storage_queue import StorageQueueClient

credential = auth.get_default_credential()
storage = 'tempbigdata'
queue_name = 'test'

client = StorageQueueClient(storage, queue_name, credential)


while True:
    if client.get_message_count() > 0:
        print(client.receive_message())
    else:
        print('No messages')
    time.sleep(3)