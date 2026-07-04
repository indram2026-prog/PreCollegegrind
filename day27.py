import csv
def filter_senior_patients(input_path, output_path):
    with open(input_path, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        headers = reader.fieldnames
        
        with open(output_path, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=headers)
            writer.writeheader()
            
            for row in reader:
                if int(row['Age']) > 40:
                    writer.writerow(row)
if __name__ == "__main__":
    target_csv = 'patient_records.csv'
    output_csv = 'senior_patients.csv'
    
    filter_senior_patients(target_csv, output_csv)