import getpass
from db_config import ADMIN_PASSWORD

def select_patient_or_doctor(cursor):
    print("\nSelect Record Type:")
    print("1. Select Patient")
    print("2. Select Doctor (Password Required)")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        pid = input("Enter Patient ID: ")
        cursor.execute("SELECT * FROM Patients WHERE patient_id = %s", (pid,))
        result = cursor.fetchone()
        print(result if result else "No patient found.")

    elif choice == '2':
        password = getpass.getpass("Enter Doctor Access Password: ")
        if password == ADMIN_PASSWORD:
            did = input("Enter Doctor ID: ")
            cursor.execute("SELECT * FROM Doctors WHERE doctor_id = %s", (did,))
            result = cursor.fetchone()
            print(result if result else "No doctor found.")
        else:
            print("Incorrect password.")
