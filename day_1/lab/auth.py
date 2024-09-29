"""
pip install azure-identity

reference: 
    https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python
    https://azuresdkdocs.blob.core.windows.net/$web/python/azure-identity/latest/azure.identity.html
"""

import azure.identity as az_identity

from azure.core.credentials import TokenCredential, AccessToken

def get_default_credential() -> TokenCredential:
    return az_identity.DefaultAzureCredential()

def get_secret_credential(tenant_id: str, app_id: str, app_secret: str) -> TokenCredential:
    return az_identity.ClientSecretCredential(tenant_id, app_id, app_secret)

def get_managed_identity_credential() -> TokenCredential:
    return az_identity.ManagedIdentityCredential()

def get_token(credential: TokenCredential, resource_id: str) -> AccessToken:
    return credential.get_token(resource_id)