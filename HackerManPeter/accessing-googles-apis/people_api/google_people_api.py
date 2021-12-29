from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = "https://www.googleapis.com/auth/userinfo.profile"
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
    creds = tools.run_flow(flow, store)
PEOPLE = discovery.build('people', 'v1', http=creds.authorize(Http()))

pep = PEOPLE.people().get(
    resourceName='people/me',
    personFields='names'
).execute()
