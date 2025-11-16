def save_patient_record(filename, patient_data):
    """ Save patient information to file
    args: filename : Name of file to save to 
    patient_data: Dictionary with patient info"""
    with open(filename,'w') as file:
        file.write("="*50 + "\n")
        file.write("patient medical record \n")
        file.write("="*50 +"\n\n")

        for key , value in patient_data.items():
            file.write(f" {key} : {value}\n")
        file.write("\n" + "="*50 + "\n")
    print(f" patient record saved to {filename}")

def read_patient_data(filename):
    """
    Read patient information from file.
    args: name of the file that it will read """
    try:
        with open(filename,'r')as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return " X file not found !"
    
patient = {
    'Name': 'Subodh Oraw',
    ' Age' : 45,
    'Blood Type' : 'o+',
    'Diagnosis': 'Type 2 Diabetes',
    'Medications': 'Metformin 500mg',
    'Next Appointment': '2024-12-01'
}

#save patient data
save_patient_record('Subodh_oraw.txt',patient)

#read patient record
print(read_patient_data('Subodh_oraw.txt'))

