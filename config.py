import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

CLIENT_SECRET = "VP5f~u5nZFK58xzp~~A5Hljfu_8XF17a.O" # Our Quickstart uses this placeholder
# In your production app, we recommend you to use other ways to store your secret,
# such as KeyVault, or environment variable as described in Flask's documentation here
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

CLIENT_ID = "1d640fc8-03b2-48cb-bcc3-2e7252af571f"

REDIRECT_PATH = "/getAToken"  # It will be used to form an absolute URL
    # And that absolute URL must match your app's redirect_uri set in AAD
#Eg60_4crB.9_GZ4rK0efB2zzcG7~-~a-yL
# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session
STORAGE_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=jrbvstorage;AccountKey=VnJ+dmAvWZvwt6RLkqhl++sSAeqnvh4AYwvsEkI7P/oYvbT8B/DqCqsUh/gzDs42CleoAeXisKK6KUTAZfrayQ==;EndpointSuffix=core.windows.net'