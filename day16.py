#Build a script that manages a small database of student registrations, records their chosen branch, and tracks their assigned tuition fee slabs.

student = {"0001": ["Indrajit", "Computer Science", "Slab 5"], "0002": ["Nilashree", "MBBS", "Slab 4"]}
student["0003"] = ["Joy Melvin", "MBBS", "Slab 5"]
student["0001"][2] = "Slab 4"  # Update Indrajit's tuition fee slab

for application_no in student:
    print(f"Application number {application_no}: {student[application_no][0]} is enrolled in {student[application_no][1]} ({student[application_no][2]})")


#Clean a duplicate-filled attendance list using a set, then use set operations to find which attendees successfully submitted their forms and which ones attended but forgot to submit them.

raw_logs = ["Alpha", "Beta", "Alpha", "Gamma", "Beta", "Delta", "Epsilon"]


submitted_forms = {"Alpha", "Gamma", "Epsilon"}

unique_logs = set(raw_logs)
attended_and_submitted = unique_logs & submitted_forms
attended_but_not_submitted = unique_logs - submitted_forms

print(f"Attendees who submitted their forms: {attended_and_submitted}")
print(f"Attendees who attended but did not submit their forms: {attended_but_not_submitted}")