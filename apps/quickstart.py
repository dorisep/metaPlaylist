from __future__ import print_function
import base64
import os.path
from googleapiclient.errors import *
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# def create_mail():
   
def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
     # Call the Gmail API
    sender = 'ed.doris@gmail.com'
    to = '8166653854@txt.att.net'
    subject = 'Week 25 metaScrape playlist'
    message_text = '''
    here is the link for this weeks list: 
    <html>
        <head>week 25</head>
        <body>
            <p>Link:</p>
            <a href="https://open.spotify.com/playlist/0kMcsRRfPYEQTN2JSbsY2q?si=8040a5bf25464c15">Link Text</a>
        </body>
    </html>
    ''' 
     
    message = MIMEText(message_text)
    print
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    body = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

   
    message = (service.users().messages().send(userId='me', body = body)
               .execute())
        
    return message
    
    
# def send_message(service = main(), user_id = 'me', message = create_mail()):
#   """Send an email message.

#   Args:
#     service: Authorized Gmail API service instance.
#     user_id: User's email address. The special value "me"
#     can be used to indicate the authenticated user.
#     message: Message to be sent.

#   Returns:
#     Sent Message.
#   """
#   try:
#     message = (service.users().messages().send(userId=user_id, body=message)
#                .execute())
#     print('Message Id: %s' % message['id'])
#     return message
#   except(errors.HttpError, error):
#     print ('An error occurred: %s' % error)
if __name__ == '__main__':
    main()
