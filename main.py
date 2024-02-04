import json

class Employee:
    def __init__(self, name, employee_id, title, department):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Title: {self.title}, Department: {self.department}")

    def __str__(self):
        return f"{self.name} ({self.employee_id})"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def list_employees(self):
        for employee in self.employees:
            print(employee)

    def __str__(self):
        return f"Department: {self.name}"


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        del self.departments[department_name]

    def display_departments(self):
        for department_name, department in self.departments.items():
            print(department)

    def save_to_file(self, filename):
        data = {"departments": {}}
        for department_name, department in self.departments.items():
            data["departments"][department_name] = {
                "name": department.name,
                "employees": [str(employee) for employee in department.employees]
            }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        for department_name, department_data in data["departments"].items():
            department = Department(department_data["name"])
            for employee_str in department_data["employees"]:
                name, employee_id = employee_str.split(" (")
                employee = Employee(name, int(employee_id[:-1]), "", department.name)
                department.add_employee(employee)

            self.add_department(department)


def print_menu():
    print("Employee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Departments")
    print("4. Save Data to File")
    print("5. Load Data from File")
    print("0. Exit")


def main():
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            name = input("Enter employee name: ")
            employee_id = int(input("Enter employee ID: "))
            title = input("Enter employee title: ")
            department_name = input("Enter department name: ")

            if department_name not in company.departments:
                print(f"Error: Department '{department_name}' does not exist.")
                continue

            employee = Employee(name, employee_id, title, department_name)
            company.departments[department_name].add_employee(employee)
        elif choice == '2':
            department_name = input("Enter department name: ")

            if department_name not in company.departments:
                print(f"Error: Department '{department_name}' does not exist.")
                continue

            department = company.departments[department_name]
            if not department.employees:
                print("No employees in this department.")
                continue

            print("Employees in the department:")
            department.list_employees()
            employee_id = int(input("Enter employee ID to remove: "))

            for employee in department.employees:
                if employee.employee_id == employee_id:
                    department.remove_employee(employee)
                    print("Employee removed.")
                    break
            else:
                print("Error: Employee not found.")
        elif choice == '3':
            company.display_departments()
        elif choice == '4':
            filename = input("Enter filename to save data: ")
            company.save_to_file(filename)
            print(f"Data saved to {filename}")
        elif choice == '5':
            filename = input("Enter filename to load data: ")
            company.load_from_file(filename)
            print(f"Data loaded from {filename}")

if __name__ == "__main__":
    main()
