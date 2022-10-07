from fastapi import FastAPI, Path
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles


# Instantiate the FastAPI object to be used
# app = FastAPI()
app = FastAPI(docs_url=None)  # Testing dark mode

# Basic example of data to be used by the API
devices = {
    1: {
        "hostname": "asdf-rtr01",
        "vendor": "Cisco",
        "IP": "127.0.0.1",
    }
}


# Example home endpoint that returns json
@app.get("/")
def home():
    return {"Data": "Test"}


# Example of single endpoint variable
# Need to start with None when using Path
# Path is used for setting things like description and validation
# Parameter is typed in function
# Description shows up in swagger
# Input validation with ge 1, le 1
@app.get("/get-item/{item_id}")
def get_item(
    item_id: int = Path(None, description="The ID of the device.", ge=1, le=1)
):
    return devices[item_id]


# Example using a query parameter
# Since the endpoint does not have a variable listed, 'name' is turned into a
# query parameter.
@app.get("/get-by-name")
def get_item_by_name(name: str):
    for device in devices.values():
        if device["hostname"] == name:
            return device


# Example using path variable and query variable
# info is a query parameter because it is not found in the endpoint
# info's default value is None so we know it is optional
@app.get("/get-by-name-and-or-query-parameter/{device_id}")
def get_by_name_and_or_query_parameter(device_id: int, info: str = None):
    if info:
        return devices[device_id][info]
    return devices[device_id]


# Working on getting dark mode

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_css_url="/static/DarkReader-1---0-0-1--000.css",
    )
