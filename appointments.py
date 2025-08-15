def create_appointments_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Appointments (
            appointment_id INT PRIMARY KEY AUTO_INCREMENT,
            patient_id INT,
            doctor_id INT,
            appointment_date DATETIME,
            status VARCHAR(20),
            reason TEXT,
            FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
            FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
        )
    """)
    print("Appointments table created.")

def book_appointment(cursor, connection):
    pid = input("Enter Patient ID: ")
    did = input("Enter Doctor ID: ")
    date = input("Enter Appointment Date and Time (YYYY-MM-DD HH:MM:SS): ")
    reason = input("Reason for Visit: ")
    cursor.execute("""
        INSERT INTO Appointments (patient_id, doctor_id, appointment_date, status, reason)
        VALUES (%s, %s, %s, 'Scheduled', %s)
    """, (pid, did, date, reason))
    connection.commit()
    print("Appointment booked.")

def view_appointments(cursor):
    cursor.execute("SELECT * FROM Appointments")
    for row in cursor.fetchall():
        print(row)
