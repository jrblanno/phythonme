import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

CLIENT_SECRET = "eH_4LQTY4.rXHqPVc0Th5WHp_M-wiin~0Y" # Our Quickstart uses this placeholder
# In your production app, we recommend you to use other ways to store your secret,
# such as KeyVault, or environment variable as described in Flask's documentation here
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

CLIENT_ID = "dbd302cc-e9e3-46ab-897b-6d03516346a5"

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