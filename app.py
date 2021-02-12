import requests
import json
url = "https://setraining.sisensepoc.com/api/v1/users"
url2 = "https://setraining.sisensepoc.com/api/v1/groups"
url3 = "https://setraining.sisensepoc.com/api/groups/tester102/users"
url4 = "https://setraining.sisensepoc.com/api/v1/groups/tester102"
data = {
  "email": "testmail2@gmail.com",
  "userName": "testmail2@gmail.com",
  "firstName": "tester",
  "lastName": "",
  "roleId": "5f07336c8ccbecc190a7c743",
  "groups": [
  ],
  "preferences": {
    "localeId": "en-US"
  },
  "uiSettings": {}
}

data2 = {
  "name": "tester10"
}

data3 = [
  "mohantay@gmail.com"
]

data4 = {
   "access": "View"
}

headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNWYwNzRhZmVhNDdhZmMwMDJjZjVmZWUyIiwiYXBpU2VjcmV0IjoiMmM4NzAxOTItY2YxZi1mZGYwLTQyYTMtODRjMzM3NWM1NWUzIiwiaWF0IjoxNjA0MDAxMjQ1fQ.FKJhFl6x980oBJnSLD8vxf7nJcaDEMwBD_tmSYUBYkQ','Content-type': 'application/json', 'Accept': 'text/plain'}

#Add a new user
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.status_code)
#add a new group
b = requests.post(url2, data=json.dumps(data2), headers=headers)
print(b.status_code)
#add user to group
c = requests.post(url3, data=json.dumps(data3), headers=headers)
print(c.status_code)
#add security to group
f = requests.put(url4, data=json.dumps(data4), headers=headers)
print(f.status_code)
