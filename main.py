import requests
import json
import argparse

parser = argparse.ArgumentParser(description="List Branches")
parser.add_argument('--owner', help='This is parameter1', required=True)
parser.add_argument('--repos', help='This is parameter1', required=True)

import requests
r=requests.get("https://api.github.com/repos/"+parser.parse_args().owner+"/"+parser.parse_args().repos+"/branches", headers={"Accept": "application/vnd.github+json" ,"X-GitHub-Api-Version":"2022-11-28", "Authorization": "Bearer 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"})

# r=requests.get("https://api.github.com/repos/geovanams/hello-world-docker-action/branches", headers={"Accept": "application/vnd.github+json" ,"X-GitHub-Api-Version":"2022-11-28", "Authorization": "Bearer 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"})

print(r.request.path_url)

obj = (r.text)
objeto = json.loads(obj)

json_formatted_str = json.dumps(objeto, indent=2)
print(json_formatted_str)

for v in objeto:
    print(v['name'])


print(parser.parse_args().owner)






