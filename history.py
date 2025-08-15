def create_history_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Medical_History (
            history_id INT PRIMARY KEY AUTO_INCREMENT,
            patient_id INT,
            doctor_id INT,
            diagnosis TEXT,
            treatment TEXT,
            prescription TEXT,
            visit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
            FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
        )
    """)
    print("Medical history table created.")

def add_history(cursor, connection):
    pid = input("Enter Patient ID: ")
    did = input("Enter Doctor ID: ")
    diagnosis = input("Diagnosis: ")
    treatment = input("Treatment: ")
    prescription = input("Prescription: ")
    cursor.execute("""
        INSERT INTO Medical_History (patient_id, doctor_id, diagnosis, treatment, prescription)
        VALUES (%s, %s, %s, %s, %s)
    """, (pid, did, diagnosis, treatment, prescription))
    connection.commit()
    print("Medical history recorded.")

def view_history(cursor):
    cursor.execute("SELECT * FROM Medical_History")
    for row in cursor.fetchall():
        print(row)
