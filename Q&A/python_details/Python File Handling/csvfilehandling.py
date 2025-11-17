import csv
def save_patients_to_csv(filename, patients):
    """ save patient data to csv file
    Args:
    filename: csv filename
    patients: list of patient"""
    #define column headers
    headers =  ['Name', 'Age','Blood_Type','Diagnosis']

    with  open(filename,'w',newline ='') as file:
        writer = csv.DictWriter(file,fieldnames = headers)

        #write header row
        writer.writeheader()
        #write patient data
        writer.writerows(patients)

    print(f" saved {len(patients)} patients to {filename}")
def read_patients_from_csv(filename):
    """read patient data from"""

    patients = []

    try:
        with open(filename, 'r') as file:
            reader =csv.DictReader(file)

            for row in reader:
                patients.append(row)

        return patients
    except FileNotFoundError:
        print(f" X file {filename} not found")
        return []

#example usage
patients = [{'Name': 'John Doe', 'Age': 45, 'Blood_Type': 'O+', 'Diagnosis': 'Diabetes'},
    {'Name': 'Jane Smith', 'Age': 32, 'Blood_Type': 'A-', 'Diagnosis': 'Hypertension'},
    {'Name': 'Bob Johnson', 'Age': 58, 'Blood_Type': 'B+', 'Diagnosis': 'Healthy'}
]

save_patients_to_csv('patients.csv', patients)

#read the csv file
loaded_patients = read_patients_from_csv('patients.csv')
print("\nLoaded Patients:")
for patient in loaded_patients:
    print(f" {patient['Name']}- Age {patient['Age']} -{patient['Diagnosis']}")


