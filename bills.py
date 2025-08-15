def create_bills_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Bills (
            bill_id INT PRIMARY KEY AUTO_INCREMENT,
            patient_id INT,
            total_amount DECIMAL(10, 2),
            status VARCHAR(20),
            bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
        )
    """)
    print("Bills table created.")

def generate_bill(cursor, connection):
    pid = input("Enter Patient ID: ")
    amount = float(input("Enter Total Amount: "))
    status = input("Status (Paid/Unpaid): ")
    cursor.execute("""
        INSERT INTO Bills (patient_id, total_amount, status)
        VALUES (%s, %s, %s)
    """, (pid, amount, status))
    connection.commit()
    print("Bill generated.")

def view_bills(cursor):
    cursor.execute("SELECT * FROM Bills")
    for row in cursor.fetchall():
        print(row)
