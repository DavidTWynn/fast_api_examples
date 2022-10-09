"""Following along FastAPI Tutorial - 
https://fastapi.tiangolo.com/tutorial/first-steps/"""

from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# First Steps
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Path Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Order matters
# In this case the first entry /users is returned
# So Rick and Morty is what comes back
# But in the auto docs get users2  is the name
@app.get("/users")
def get_users1():
    return ["Rick", "Morty"]


# Order matters
@app.get("/users")
def get_users2():
    return ["Shepard", "Ghost"]


# Predefined values with Enum
"""
Now with this in the auto doc we see a drop down
of valid messages.

Error is stated as well when not in enum -
Invoke-webrequest : {"detail":[{"loc":["path","model_name"],"msg":"value is
not a valid enumeration member; permitted: 'cisco', 'hp', 'dell'","type":
"type_error.enum","ctx":{"enum_values":["cisco","hp","dell"]}}]}
"""


class Models(str, Enum):
    cisco = "cisco"
    hp = "hp"
    dell = "dell"


@app.get("/models/{model_name}")
async def get_models(model_name: Models):
    if model_name in Models:
        return True


# path parameter handling with Starlette
# Request: http://127.0.0.1:8000/files/%2Fhome%2Fuser%2Fdoc.txt
# Response: {"file_path": "/home/user/doc.txt"}
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Query parameters
devices = [{"hostname": f"rtr-{hostname}"} for hostname in range(1, 11)]


# Skip is acting more like start after
# limit will limit max number of items to return
@app.get("/devices")
async def get_devices(skip: int = 0, limit: int = len(devices)):
    return devices[skip : skip + limit]
