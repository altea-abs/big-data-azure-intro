""""
pip install azure-storage-blob

reference:
    https://learn.microsoft.com/en-us/python/api/overview/azure/storage-blob-readme?view=azure-python
    https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob?view=azure-python
    https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-acl-python?tabs=entra-id
"""
import datetime

import azure.storage.blob as blob
import azure.storage.filedatalake as lake

class StorageClient:

    def __init__(self, account_name: str, credential: str):
        self.account_name = account_name
        self.blob_client = blob.BlobServiceClient(self._blob_api_url(account_name), credential)
        self.lake_client = lake.DataLakeServiceClient(self._lake_api_url(account_name), credential)

    @staticmethod
    def _blob_api_url(account_name: str) -> str:
        return f'https://{account_name}.blob.core.windows.net'
    
    @staticmethod
    def _lake_api_url(account_name: str) -> str:
        return f'https://{account_name}.dfs.core.windows.net'
    
    def create_blob(self, container: str, path: str, content: bytes):
        self.blob_client.get_blob_client(container, path).upload_blob(content)

    def upload_file(self, container: str, file_path: str, out_path: str):
        with open(file_path, 'rb') as f:
            self.create_blob(container, out_path, f.read())

    def create_container(self, name: str):
        self.blob_client.create_container(name)

    @staticmethod
    def _acl_string(principal_type: str, id: str, permissions: str):
        return f'{principal_type}:{id}:{permissions}'

    def set_acl(self, container:str, path:str, permissions: str, principal_id: str, principal_type: str = 'user'):
        file_system_client = self.lake_client.get_file_system_client(file_system=container)
        directory_client = file_system_client.get_directory_client(path)
              
        acl = self._acl_string(principal_type, principal_id, permissions)

        directory_client.update_access_control_recursive(acl=acl)

        acl_props = directory_client.get_access_control()
        
        print(acl_props['permissions'])


    def create_sas_token(self, container: str, path: str):
        now = datetime.datetime.now(datetime.timezone.utc)
        key = self.blob_client.get_user_delegation_key(
            now, now + datetime.timedelta(days=1))
        sas = blob.generate_blob_sas(self.account_name, container, path, user_delegation_key=key,
                               permission=blob.BlobSasPermissions(read=True), 
                               expiry= now + datetime.timedelta(days=1),
                               start=now)
        return sas




