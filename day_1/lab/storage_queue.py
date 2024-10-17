"""
pip install azure-storage-queue

https://learn.microsoft.com/en-us/python/api/overview/azure/storage-queue-readme?view=azure-python
"""

import os, uuid
from azure.core.credentials import TokenCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage, BinaryBase64DecodePolicy, BinaryBase64EncodePolicy


class StorageQueueClient:

    def __init__(self, storage_name: str, queue_name: str, credential: TokenCredential):
        endpoint = f"https://{storage_name}.queue.core.windows.net"
        self.client = QueueClient(endpoint, queue_name=queue_name, credential=credential)

    def add_message(self, message: str):
        self.client.send_message(message)

    def receive_message(self) -> str:
        result = self.client.receive_messages()
        for message in result:
            self.client.delete_message(message)
            return message.content
    
    def get_message_count(self) -> int:
        properties = self.client.get_queue_properties()
        return properties.approximate_message_count