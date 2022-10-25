import requests
import base64
import sys
import os.path
import json
#Add in API ID and Key from apikey.py file
from apikey import headers, accountID


for pageNum in range(0,6):
        url = f'https://my.imperva.com/api/prov/v1/sites/list?account_id={accountID}&page_size=100&page_num={pageNum}'
        listResponse = requests.post(url, headers=headers)
        jsonListResponse = json.loads(listResponse.text)
        for site in jsonListResponse['sites']:
                url = f"https://my.imperva.com/api/prov/v1/sites/status?site_id={site['site_id']}&tests=domain_validation,services,dns"
                statusResponse = requests.request("POST", url, headers=headers)
                jsonStatusObject = json.loads(statusResponse.text)
                stringIps = ' | '.join(map(str, jsonStatusObject['ips']))
                cl = (str, jsonStatusObject['dns'])
                cname = cl[:2]
                row = (f"{jsonStatusObject['site_id']} {jsonStatusObject['domain']} {stringIps} {cname} {jsonStatusObject['active']}").split()
                print(jsonStatusObject)
                print(row)
exit()
