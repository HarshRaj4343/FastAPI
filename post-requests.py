from fastapi import FastAPI, HTTPException, Path, Query
import json
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated, Optional
from fastapi.responses import JSONResponse

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'


def data_loader():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

def data_saver(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


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


@app.get("/patients/{patient_id}")
def view_specific_patient(patient_id: str = Path(..., description="ID of the patient you wanna search for.",example='P004')):
    # loading all the patients
    data = data_loader()
    # extract the particular patient
    if patient_id in data:
        uniq_patient = data[patient_id]
        return uniq_patient
    raise HTTPException(status_code=404,detail='Patient not found in database.')

@app.get("/sort")
def sort_patients(sort_by:str = Query(...,description='Sort on the basis of height, weight or bmi'),order: str = Query('asc',description='Sort either in ascending order or in descending')):
    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,description='Invalid field selected, select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,description='Invalid field selected, select from [asc,desc]')
    data = data_loader()
    ar = True if order=='desc' else False
    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by,0),reverse=ar)
    return sorted_data

@app.post("/create")
def add_patient(patient:Patient):
    # load existing patients
    data = data_loader()
    # check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists in the database.")
    # new patient addition into database
    data[patient.id] = patient.model_dump(exclude=['id'])
    # save into json
    data_saver(data)

    return JSONResponse(status_code=201,content={'message':'Patient created successfully.'})
# for running this:
"""
python3 -m uvicorn file_name:app --reload
"""

