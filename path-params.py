from fastapi import FastAPI, HTTPException, Path, Query
import json

# HTTPException is used to raise custom HTTP server errors
# '...' represents that is field is necessary to give and not Optional
# Path is used to provide metadata, validation rules, and documentation hints for path params in your API documentations. Could be title, ge,gt,le,lt,regex patterns or anything else.

app = FastAPI()

# Query Params:-
"""
Query parameters are optional key-value pairs appended to the end of a URL, used to pass additional data to the server in an HTTP request. They are typically employed for operations like filtering, sorting,
searching, and pagination, without altering the endpoint path itself.
"""

# Pagination:-
"""
Pagination is the process of dividing a large dataset into smaller, discrete, and manageable segments (pages). It improves performance and user experience by preventing systems from loading thousands of records all at once.
"""

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



# for running this:
"""
python3 -m uvicorn file_name:app --reload
"""



"""
`Query()` is a utility function provided by FastAPI to define, validate, and document query parameters in API endpoints. It helps developers set default values, apply validation rules, and add useful metadata such as titles, descriptions, and example values. Using `Query()`, you can ensure that incoming query parameters meet specific requirements before they are processed by your application.

Some commonly used arguments of `Query()` include `default`, which sets a default value for the parameter; `title`, which displays a readable name in the API documentation; and `description`, which provides detailed information about the parameter in Swagger UI. The `example` or `examples` argument allows you to show sample inputs, making the API easier to understand. For validation, `min_length` and `max_length` can be used to restrict the length of string inputs, while `ge`, `gt`, `le`, and `lt` help enforce numeric boundaries. Additionally, `regex` (or `pattern` in newer versions) can be used to ensure that string inputs follow a specific format or pattern.

"""