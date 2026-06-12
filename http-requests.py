from fastapi import FastAPI
import json
app = FastAPI()

def data_loader():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message':'Patient Management System'}


@app.get("/about")
def about():
    return {'about':'This API is a simple patient management system.'}

@app.get("/view_patients")
def patient_viewer():
    data = data_loader()
    return data


# for running this:
"""
python3 -m uvicorn file_name:app --reload
"""