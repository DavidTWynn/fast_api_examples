# FAST API Examples

![GitHub last commit](https://img.shields.io/github/last-commit/davidtwynn/fast_api_examples?style=plastic&color=success)
![commits](https://badgen.net/github/commits/davidtwynn/fast_api_examples?icon=github&color=blue)
![Python version](https://img.shields.io/badge/python%20version-3.10-blue)
![Coding style](https://img.shields.io/badge/code%20style-black-000000.svg)

Repo for learning FastAPI and storing examples

## Fast API Basics

    1. Import fastapi
    2. Create an instance of the FastAPI class
    3. Write a path operation decorator (like @app.get("/"))
    4. Write a path operation function (like def root(): ... below the decorator)
    5. Run the development server (like uvicorn pythonfile:classinstance --reload)

## Setup

```Bash
git clone https://github.com/DavidTWynn/fast_api_examples
cd fast_api_examples
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run

```Bash
uvicorn tech_with_tim_example:app --reload
```

Go to http://127.0.0.1:8000
Swagger docs at http://127.0.0.1:8000/docs

### Output

<img src="images/fastapi_darkmode.JPG" width="100%" height="100%">

## Resources

Tech with Tim video - https://www.youtube.com/watch?v=-ykeT6kk4bk

FastAPI Docs and tutorial user guide - https://fastapi.tiangolo.com/

### CSS

CSS Base template - https://github.com/Itz-fork/Fastapi-Swagger-UI-Dark/tree/main/assets

CSS Dark Mode changes - Pulled from DarkReader extension CSS Export
