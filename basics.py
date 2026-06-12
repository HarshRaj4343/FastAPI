from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'hello world'}


@app.get("/about")
def about():
    return {'about':'this is the about section of the website'}

# for running this:
"""
python3 -m uvicorn file_name:app --reload
"""