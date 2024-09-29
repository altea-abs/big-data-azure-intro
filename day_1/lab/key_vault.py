"""
pip install azure-keyvault-secrets

reference:
    https://learn.microsoft.com/en-us/python/api/overview/azure/keyvault-secrets-readme?view=azure-python
    https://azuresdkdocs.blob.core.windows.net/$web/python/azure-keyvault-secrets/latest/azure.keyvault.secrets.html
"""
import azure.keyvault.secrets as kv

from azure.core.credentials import TokenCredential

class KeyVaultClient:
    def __init__(self, url: str, credential: TokenCredential):
        self.client = kv.SecretClient(url, credential)

    def get_secret(self, name: str) -> str:
        self.client.get_secret(name).value