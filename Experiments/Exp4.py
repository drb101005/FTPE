# Task List Manager
CET = {'Mahipal', 'Mayuresh', 'Rashika', 'Manish'}
JEE = {'Mahipal', 'Mayuresh', 'Shivam', 'Sharman'}
NEET = {'Nirmala', 'Sana', 'Rashika', 'Mahipal'}

print("Students appearing for CET, NEET and JEE are:", (JEE|CET|NEET))
print("Students appearing for all three exams are:", (JEE&CET&NEET))
print("Students appearing for CET but not for NEET and JEE:", (CET-JEE-NEET))
SD = CET ^ JEE ^ NEET
print("Students appearing for either CET, NEET and JEE not all are:", (SD))

# Student Record Keeper
CET = {'Mahipal', 'Mayuresh', 'Rashika', 'Manish'}
JEE = {'Mahipal', 'Mayuresh', 'Shivam', 'Sharman'}
NEET = {'Nirmala', 'Sana', 'Rashika', 'Mahipal'}

print("Students appearing for CET, NEET and JEE are:", (JEE|CET|NEET))
print("Students appearing for all three exams are:", (JEE&CET&NEET))
print("Students appearing for CET but not for NEET and JEE:", (CET-JEE-NEET))
SD = CET ^ JEE ^ NEET
print("Students appearing for either CET, NEET and JEE not all are:", (SD))