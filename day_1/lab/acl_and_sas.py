import asyncio

import auth
import graph
import storage

async def set_acl(account: str, credential):    
    user = await graph_client.get_user('claudio.paterniti@absontheweb.onmicrosoft.com')
    storage_client = storage.StorageClient(account, credential)
    storage_client.set_acl('test', 'test', 'rwx', user.id)

credential = auth.get_default_credential()
graph_client = graph.GraphClient(credential)
account = 'tempbigdata'
credential = auth.get_default_credential()
storage_client = storage.StorageClient(account, credential)
print(storage_client.create_sas_token('test', 'test/file.txt'))

asyncio.run(set_acl)
