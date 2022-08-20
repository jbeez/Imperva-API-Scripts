import requests
import base64

#site specific
site_id = {123456}
pemfile = "certs\\certfile.pem"
keyfile = "certs\\certfile.key"
pw = "certificatePWhere"

#pem file is the client cert followed by the chain with root at the end
#########################################################################

with open(pemfile, "rb") as mycert:
   b64c = base64.b64encode(mycert.read()).decode('utf-8')
with open(keyfile, "rb") as mycert:
   b64k = base64.b64encode(mycert.read()).decode('utf-8')
    
from apikey import headers

payload = {
  "certificate": b64c,
  "passphrase": pw,
  "private_key": b64k,
  "auth_type": "RSA"
}

for id in site_id:
  url = f"https://my.imperva.com/api/prov/v2/sites/{id}/customCertificate"
  response = resquests.request("PUT", url, headers=headers, json=payload)
  print(response.text)
