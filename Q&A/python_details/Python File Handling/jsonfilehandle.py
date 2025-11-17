import json
def save_patient_json(filename, patient_data):
    """ save patient data as json file.
    args: 
    filename : Json file name 
    patient_data : patient data dictionary"""
    with open(filename, 'w') as file:
        json.dump(patient_data, file, indent = 4)

    print(f" Saved patient data to {filename}")

def load_patient_json(filename):
    """ load patient data from json file.
    args:
    filename: Json filename
    returns:
    dict :patient data"""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f" x file {filename} not found!")
        return None

patient_data = {
    "patient_ID": "P12345",
    "name": "Sarah Corner",
    "age": 35,
    "Blood_type": "AB+",
    "medical_history":[
        { "date" : "2024-01-15", "diagnosis":"flu","treatment":"Rest and fluids"},
        { "date": "2024-03-20", "diagnosis": "sprained ankle","treatment":"RICE method"}],
        "allergies": ["Penicillin","peanuts"],
        "emergency_contacts":{
            "name": "John Conor",
            "reletionships": "Spouse",
            "phone":"555-0123"
        }
}
#Save as JSON
save_patient_json('sarah_connor.json', patient_data)

# Load from Json 
loaded_data = load_patient_json('sarah_connor.json')
if loaded_data:
    print(f"\nPatient: {loaded_data['name']}")
    print(f"age: {loaded_data['age']}")
    print(f"Allergies: {','.join(loaded_data['allergies'])}")
    for record in loaded_data['medical_history']:
        print(f" [{record['date']}]{record['diagnosis']}")
