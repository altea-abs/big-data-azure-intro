""""
pip install azure-storage-blob

reference:
    https://learn.microsoft.com/en-us/python/api/overview/azure/storage-blob-readme?view=azure-python
    https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob?view=azure-python
"""

import azure.storage.blob as blob

class StorageClient:

    def __init__(self, account_name: str, credential: str):
        self.client = blob.BlobServiceClient(self._blob_api_url(account_name), credential)

    @staticmethod
    def _blob_api_url(account_name: str) -> str:
        return f'https://{account_name}.blob.core.windows.net'
    
    def create_blob(self, container: str, path: str, content: bytes):
        self.client.get_blob_client(container, path).upload_blob(content)

    def upload_file(self, container: str, file_path: str, out_path: str):
        with open(file_path, 'rb') as f:
            self.create_blob(container, out_path, f.read())



