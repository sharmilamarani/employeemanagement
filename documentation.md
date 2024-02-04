## Employee Management System Documentation

### Overview

The Employee Management System is a command-line application developed in Python using Object-Oriented Programming principles. It allows a company to manage information about its employees and departments efficiently.

### Features

- **Employee Class:**
  - Represents an employee with attributes for name, ID, title, and department.
  - Includes methods to display employee details and a string representation method.

- **Department Class:**
  - Represents a department with attributes for the department name and a list of employees.
  - Includes methods to add an employee, remove an employee, and list all employees in the department.

- **Company Class:**
  - Represents the entire company using a dictionary with department names as keys and Department objects as values.
  - Includes methods to add a department, remove a department, and display all departments.

- **User Interaction:**
  - Provides a menu-driven command-line interface for users to perform actions such as adding employees, removing employees, and viewing department details.

- **Data Persistence (Optional):**
  - Supports saving and loading company data to and from a file in JSON format.

### How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sharmilamarani/employeemanagement.git
   ```

2. **Install Dependencies:**
   The application doesn't have external dependencies.

3. **Run the Application:**
   ```bash
   python main.py
   ```

4. **Interact with the Menu:**
   Follow the on-screen instructions to interact with the Employee Management System. Options include adding employees, removing employees, displaying departments, saving data to a file, and loading data from a file.

5. **Testing (Optional):**
   If you want to run the unit tests, use the following command:
   ```bash
   python test_cases.py
   ```

### Example

Here's an example interaction with the application:

```bash
python employee_management_system.py
```

```
Employee Management System Menu:
1. Add Employee
2. Remove Employee
3. Display Departments
4. Save Data to File
5. Load Data from File
0. Exit

Enter your choice: 1
Enter employee name: John Doe
Enter employee ID: 101
Enter employee title: HR Specialist
Enter department name: HR

Employee Management System Menu:
1. Add Employee
2. Remove Employee
3. Display Departments
4. Save Data to File
5. Load Data from File
0. Exit

Enter your choice: 3
Department: HR

Employee Management System Menu:
1. Add Employee
2. Remove Employee
3. Display Departments
4. Save Data to File
5. Load Data from File
0. Exit

Enter your choice: 0
```
