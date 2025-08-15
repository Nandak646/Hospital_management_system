import random

def create_doctors_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Doctors (
            doctor_id INT PRIMARY KEY,
            name VARCHAR(50),
            specialty VARCHAR(50),
            phone VARCHAR(15),
            email VARCHAR(100),
            room_number VARCHAR(10),
            date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("Doctors table created.")

def register_doctor(cursor, connection):
    did = random.randint(5000, 9999)
    print(f"Assigned Doctor ID: {did}")
    name = input("Enter Doctor Name: ")
    specialty = input("Specialty: ")
    phone = input("Phone: ")
    email = input("Email: ")
    room = input("Room Number: ")
    cursor.execute("""
        INSERT INTO Doctors (doctor_id, name, specialty, phone, email, room_number)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (did, name, specialty, phone, email, room))
    connection.commit()
    print("Doctor registered.")

def view_doctors(cursor):
    cursor.execute("SELECT * FROM Doctors")
    for row in cursor.fetchall():
        print(row)
