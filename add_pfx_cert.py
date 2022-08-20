import requests
import base64

#site specific
site_id = {123456}
pfxfile = "certs\\certfile.pfx"
pw = "certificatePWhere"

############################################################

with open(pfxfile, "rb") as mycert:
   b64c = base64.b64encode(mycert.read()).decode('utf-8')
    
from apikey import headers

payload = {
  "certificate": b64c,
  "passphrase": pw,
  "auth_type": "RSA"
}

for id in site_id:
  url = f"https://my.imperva.com/api/prov/v2/sites/{id}/customCertificate"
  response = resquests.request("PUT", url, headers=headers, json=payload)
  print(response.text)
