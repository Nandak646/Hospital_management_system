from db_config import connect_db, ADMIN_PASSWORD
from patients import register_patient, view_patients, create_patients_table
from doctors import register_doctor, view_doctors, create_doctors_table
from appointments import book_appointment, view_appointments, create_appointments_table
from bills import generate_bill, view_bills, create_bills_table
from history import add_history, view_history, create_history_table
from secure_access import select_patient_or_doctor
import getpass

def main():
    conn = connect_db()
    cur = conn.cursor()

    menu = """
=============== Hospital Management System ===============
1. Register Patient
2. Register Doctor
3. Book Appointment
4. Generate Bill
5. Add Medical History
6. View Patients
7. View Doctors
8. View Appointments
9. View Bills
10. View Medical History
11. Create All Tables (Admin)
12. Select Patient or Doctor (Secure Access)
0. Exit
===========================================================
"""

    while True:
        print(menu)
        choice = input("Enter your choice: ")
        if choice == '1':
            register_patient(cur, conn)
        elif choice == '2':
            register_doctor(cur, conn)
        elif choice == '3':
            book_appointment(cur, conn)
        elif choice == '4':
            generate_bill(cur, conn)
        elif choice == '5':
            add_history(cur, conn)
        elif choice == '6':
            view_patients(cur)
        elif choice == '7':
            view_doctors(cur)
        elif choice == '8':
            view_appointments(cur)
        elif choice == '9':
            view_bills(cur)
        elif choice == '10':
            view_history(cur)
        elif choice == '11':
            pw = getpass.getpass("Enter Admin Password: ")
            if pw == ADMIN_PASSWORD:
                create_patients_table(cur)
                create_doctors_table(cur)
                create_appointments_table(cur)
                create_bills_table(cur)
                create_history_table(cur)
            else:
                print("Incorrect password.")
        elif choice == '12':
            select_patient_or_doctor(cur)
        elif choice == '0':
            print("Exiting system. Thank you.")
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
