import csv
import os

def generate_csv_file(file_path):
    """Generates a mock patient data CSV file automatically."""
    print("Generating raw patient database...")
    
    # Define the mock dataset
    patients_list = [
        {"Patient_ID": "P01", "Name": "Ravi", "Age": 34, "Blood_Type": "O+", "Condition": "Healthy"},
        {"Patient_ID": "P02", "Name": "Meena", "Age": 65, "Blood_Type": "A-", "Condition": "Diabetes"},
        {"Patient_ID": "P03", "Name": "Vijay", "Age": 21, "Blood_Type": "B+", "Condition": "Flu"},
        {"Patient_ID": "P04", "Name": "Anita", "Age": 48, "Blood_Type": "AB-", "Condition": "Hypertension"},
        {"Patient_ID": "P05", "Name": "Rajesh", "Age": 72, "Blood_Type": "O-", "Condition": "Diabetes"}
    ]

    # Define columns
    headers = ["Patient_ID", "Name", "Age", "Blood_Type", "Condition"]

    # Write the data to a CSV file
    # newline='' prevents blank row insertions on Windows platforms
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(patients_list)
        
    print(f"Success: '{file_path}' created in your directory.\n")


def analyze_patient_data(file_path):
    """Reads the CSV file and computes analysis metrics."""
    print("--- Medical Records Analysis ---")
    
    total_age = 0
    patient_count = 0
    diabetes_patients = []

    try:
        with open(file_path, mode='r') as file:
            # Using DictReader to map column headers to dictionary keys
            reader = csv.DictReader(file)
            
            for row in reader:
                patient_count += 1
                
                # Convert the age string into an integer for arithmetic tracking
                age = int(row['Age'])
                total_age += age
                
                # Identify specific medical targets
                if row['Condition'].strip() == 'Diabetes':
                    diabetes_patients.append(row['Name'])
                    
        # Compute summary metrics
        average_age = total_age / patient_count if patient_count > 0 else 0
        
        # Display the formatted breakdown
        print(f"Total Patients Processed : {patient_count}")
        print(f"Average Patient Age      : {average_age:.1f} years old")
        print(f"Diabetes Diagnoses       : {', '.join(diabetes_patients)}")
        print("--------------------------------")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' could not be located. Run the generator step first.")


if __name__ == "__main__":
    # Target filename definition
    target_csv = 'patient_records.csv'
    
    # Step 1: Create the data file dynamically
    generate_csv_file(target_csv)
    
    # Step 2: Extract and process the generated file
    analyze_patient_data(target_csv)