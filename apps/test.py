
import requests

track_ids = []
#     request_data = json.dump

query = f'https://api.spotify.com/v1/albums/4aawyAB9vmqN3uQ7FjRGTy/tracks'
response = requests.get(
    query,
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer AQA92cE5oL-fTQvG1_objGmNUVNQ_6AseJUqjsNC2ujDEFeMTOPxBpLqQ6Ct2tkmLIp79RT6deD3WjdPRYDlhnU2YgautBPNYw5aGMjYVD-y35lz5_n1L88yxG2UA-7nd58'
    })
response_json = response.json()
print(response_json)
tracks = response_json['items']
for track in tracks:
    track_ids.append(track['uri'])
    # track_urs
    print(track['id'])
