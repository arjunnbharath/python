import json
data = {"name": "arjun"}
with open("data.txt","w") as f:
  json.dump(data,f)
  print("done")

with open ("data.txt","r") as f:
  a=json.load(f)
  print("data extrated :", a)