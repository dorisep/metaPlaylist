from urllib.parse import urlencode
import requests
import base64
import datetime
from config import *



# # # GET https://accounts.spotify.com/authorize?client_id=5fe01282e44241328a84e7c5cc169165&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-read-private%20user-read-email&state=34fFs29kd09
'''get auth'''
# endpoint = 'https://accounts.spotify.com/authorize'
# params = {
# 'client_id' : f'{spotify_client_id}',
# 'response_type' : 'code',	
# 'redirect_uri' : f'{spotify_redirect_uri}',
# 'scope' : 'playlist-modify-public'
# }

# data = urlencode(params)

# auth_url = f'{endpoint}?{data}'

# print(auth_url)
# r_auth = requests.get(auth_url)
# print(r_auth)
'''get access and refresh token
code=
'''
# curl -H "Authorization: Basic ZjM...zE=" -d grant_type=authorization_code -d code=MQCbtKe...44KN
#  -d redirect_uri=https%3A%2F%2Fwww.foo.com%2Fauth https://accounts.spotify.com/api/token


# client_creds = f'{spotify_client_id}:{spotify_client_secret}'
# client_creds_b64 = base64.b64encode(client_creds.encode())
# auth_code = 'AQCSVKdFUm4yT2mx48wKht9atyu8u4PbMGUR76CBQYMpiowwVKHTOrtw02EHWJjheakBD4BZvdHamx7HVhbJHiy-bBbJGkawq46KYs_orEektQYXIQmhKbMwB7MxNZbMcecgrmXZzuVwv9EdUa_5ax0f0OiKbLr89xlNctRC-c97vPFFL_YS2Z1s-BLSp2q1pHpxGVzGwTWk-ck'

# token_header = {
#     'Authorization' : f'Basic {client_creds_b64.decode()}'
# }

# token_body_params = {
#     'grant_type' : 'authorization_code',
#     'code' : f'{auth_code}',
#     'redirect_uri' : f'{spotify_redirect_uri}'
# }

# token_url = 'https://accounts.spotify.com/api/token'

# r_token = requests.post(token_url, data = token_body_params, headers=token_header)
# print(r_token.json())
# token_response_data = r_token.json()
# print(token_response_data)
# now = datetime.datetime.now()
# access_token = token_response_data['access_token']
# expires_in = token_response_data['expires_in']
# refresh_token = token_repsonse_data['refresh_token']
# expires = now + datetime.timedelta(seconds=expires_in)
# did_expire = expires < now
# print(did_expire)
'''
Gets an access token using a refresh token
'''
def refresh_accesss_token()
    client_creds = f'{spotify_client_id}:{spotify_client_secret}'
    client_creds_b64 = base64.b64encode(client_creds.encode())

    refresh_token_header = {
        'Authorization' : f'Basic {client_creds_b64.decode()}'
    }

    # def refresh_playlist_token():
    refresh_url =  'https://accounts.spotify.com/api/token'
    refresh_params = {
        'grant_type': 'refresh_token',
        'refresh_token': 'AQA92cE5oL-fTQvG1_objGmNUVNQ_6AseJUqjsNC2ujDEFeMTOPxBpLqQ6Ct2tkmLIp79RT6deD3WjdPRYDlhnU2YgautBPNYw5aGMjYVD-y35lz5_n1L88yxG2UA-7nd58'
        
    }

    refresh_data = urlencode(refresh_params)



    r_token = requests.post(refresh_url, data=refresh_params, headers=refresh_token_header)

    refresh_response = r_token.json()

    access_token = refresh_response['access_token']

    return access_token

