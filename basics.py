from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Patient Management System'}


@app.get("/about")
def about():
    return {'about':'This API is a simple patient management system.'}

# for running this:
"""
python3 -m uvicorn file_name:app --reload
"""

# Use:
"""
pip freeze > requirements.txt for auto-generating requirements.txt
"""
