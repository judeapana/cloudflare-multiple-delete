import requests

email = input('Enter Your Email Address: ')
auth_key = input('Enter Your X-AUTH-KEY: ')
zone_id = input('Enter Your Zone ID: ')
headers = {
    'X-Auth-Email': f'{email}',
    'X-Auth-Key': f'{auth_key}'
}
req = requests.get(f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records', headers=headers)
if req.status_code == 200:
    data = req.json()

    for i in data.get('result'):
        delete = requests.delete(f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{i.get("id")}',
                                 headers=headers)
        print(">> Deleting>>: " + str(delete.content))
else:
    print(req.content)
