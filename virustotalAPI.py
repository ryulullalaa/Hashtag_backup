
#api_key = "5b46d9789014d1737abdc1bdb10aff4bc45528621c31f0e341ad4536e4fa3399"

import requests 
api_key = '5b46d9789014d1737abdc1bdb10aff4bc45528621c31f0e341ad4536e4fa3399'
# params = {'api_key': api_key, 'hash': '5845F52D425C75E232B1AD5EE3B189A8'}
params = {'api_key': api_key, 'hash': '069846ff6799955eea05aee1a005d87fbce6f2f8394fc464b821dee23f7aac3e'}
response = requests.get('https://public.api.malwares.com/v3/file/mwsinfo', params=params)
json_response = response.json()
print(json_response)