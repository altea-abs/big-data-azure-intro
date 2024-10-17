"""
pip install msgraph-sdk

https://github.com/microsoftgraph/msgraph-sdk-python
"""

from azure.core.credentials import TokenCredential
import msgraph
from msgraph.generated.models.user import User

class GraphClient:

    def __init__(self, credential: TokenCredential):
        self.client = msgraph.GraphServiceClient(
            credentials=credential, scopes=['https://graph.microsoft.com/.default'])
        
    async def get_user(self, mail:str) -> User:
        user = await self.client.users.by_user_id(mail).get()
        return user