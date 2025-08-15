import random
from utils import get_valid_date, get_valid_input

def create_patients_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Patients (
            patient_id INT PRIMARY KEY,
            name VARCHAR(50),
            gender VARCHAR(10),
            dob DATE,
            phone VARCHAR(15),
            address VARCHAR(100),
            blood_type VARCHAR(5),
            date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("Patients table created.")

def register_patient(cursor, connection):
    pid = random.randint(1000, 9999)
    print(f"Assigned Patient ID: {pid}")
    name = input("Enter Patient Name: ")
    gender = get_valid_input("Gender (M/F/O): ", ["M", "F", "O"])
    dob = get_valid_date("Date of Birth (YYYY-MM-DD): ")
    phone = input("Phone: ")
    address = input("Address: ")
    blood_type = input("Blood Type: ").upper()
    cursor.execute("""
        INSERT INTO Patients (patient_id, name, gender, dob, phone, address, blood_type)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (pid, name, gender, dob, phone, address, blood_type))
    connection.commit()
    print("Patient registered.")

def view_patients(cursor):
    cursor.execute("SELECT * FROM Patients")
    for row in cursor.fetchall():
        print(row)
