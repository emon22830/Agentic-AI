##without pydantic
""""
def add_patient_data(name, age):
    if type(name) ==str and type(age)==int:
        print(name)
        print(age)
        print("Data added successfully to the database!")

    
    else:
        raise TypeError("Invalid Data Type")
    
add_patient_data("Emon", "tweenty-four")

"""


from pydantic import BaseModel 
class PatientData(BaseModel)
    name:str
    age:int



def add_patient_data(PatientData):
    pass



