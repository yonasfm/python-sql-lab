import psycopg2

def connect_db():
    """Connect to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname="crm_tool",
            user="your_username",  # Replace with your actual username
            password="your_password",  # Replace with your actual password
            host="localhost"  # Or your database host
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_company(conn, name, location):
    """Create a new company."""
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO companies (name, location) VALUES (%s, %s) RETURNING id;", (name, location))
            company_id = cur.fetchone()[0]
            conn.commit()
            print(f"Company '{name}' created with ID: {company_id}")
            return company_id
    except psycopg2.Error as e:
        print(f"Error creating company: {e}")
        conn.rollback()
        return None

def read_companies(conn):
    """Read all companies."""
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM companies;")
            companies = cur.fetchall()
            for company in companies:
                print(company)
    except psycopg2.Error as e:
        print(f"Error reading companies: {e}")

def update_company(conn, company_id, new_name, new_location):
    """Update an existing company."""
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE companies SET name = %s, location = %s WHERE id = %s;", (new_name, new_location, company_id))
            conn.commit()
            print(f"Company with ID {company_id} updated.")
    except psycopg2.Error as e:
        print(f"Error updating company: {e}")
        conn.rollback()

def delete_company(conn, company_id):
    """Delete a company."""
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM companies WHERE id = %s;", (company_id,))
            conn.commit()
            print(f"Company with ID {company_id} deleted.")
    except psycopg2.Error as e:
        print(f"Error deleting company: {e}")
        conn.rollback()

def create_employee(conn, name, position, salary, company_id):
    """Create a new employee."""
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO employees (name, position, salary, company_id) VALUES (%s, %s, %s, %s) RETURNING id;",
                (name, position, salary, company_id),
            )
            employee_id = cur.fetchone()[0]
            conn.commit()
            print(f"Employee '{name}' created with ID: {employee_id}")
            return employee_id
    except psycopg2.Error as e:
        print(f"Error creating employee: {e}")
        conn.rollback()
        return None

def read_employees(conn):
    """Read all employees."""
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM employees;")
            employees = cur.fetchall()
            for employee in employees:
                print(employee)
    except psycopg2.Error as e:
        print(f"Error reading employees: {e}")

def update_employee(conn, employee_id, new_name, new_position, new_salary, new_company_id):
    """Update an existing employee."""
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE employees SET name = %s, position = %s, salary = %s, company_id = %s WHERE id = %s;",
                (new_name, new_position, new_salary, new_company_id, employee_id),
            )
            conn.commit()
            print(f"Employee with ID {employee_id} updated.")
    except psycopg2.Error as e:
        print(f"Error updating employee: {e}")
        conn.rollback()

def delete_employee(conn, employee_id):
    """Delete an employee."""
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM employees WHERE id = %s;", (employee_id,))
            conn.commit()
            print(f"Employee with ID {employee_id} deleted.")
    except psycopg2.Error as e:
        print(f"Error deleting employee: {e}")
        conn.rollback()

def main():
    """Main function to run the CRM tool."""
    conn = connect_db()
    if conn is None:
        return

    while True:
        print("\nCRM Tool Menu:")
        print("1. Create Company")
        print("2. Read Companies")
        print("3. Update Company")
        print("4. Delete Company")
        print("5. Create Employee")
        print("6. Read Employees")
        print("7. Update Employee")
        print("8. Delete Employee")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter company name: ")
            location = input("Enter company location: ")
            create_company(conn, name, location)
        elif choice == "2":
            read_companies(conn)
        elif choice == "3":
            company_id = int(input("Enter company ID to update: "))
            new_name = input("Enter new company name: ")
            new_location = input("Enter new company location: ")
            update_company(conn, company_id, new_name, new_location)
        elif choice == "4":
            company_id = int(input("Enter company ID to delete: "))
            delete_company(conn, company_id)
        elif choice == "5":
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            company_id = int(input("Enter company ID for the employee: "))
            create_employee(conn, name, position, salary, company_id)
        elif choice == "6":
            read_employees(conn)
        elif choice == "7":
            employee_id = int(input("Enter employee ID to update: "))
            new_name = input("Enter new employee name: ")
            new_position = input("Enter new employee position: ")
            new_salary = float(input("Enter new employee salary: "))
            new_company_id = int(input("Enter new company ID: "))
            update_employee(conn, employee_id, new_name, new_position, new_salary, new_company_id)
        elif choice == "8":
            employee_id = int(input("Enter employee ID to delete: "))
            delete_employee(conn, employee_id)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")

    if conn:
        conn.close()

if __name__ == "__main__":
    main()