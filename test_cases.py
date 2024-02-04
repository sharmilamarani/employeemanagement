import unittest
import os
from main import Employee, Department, Company

class TestEmployeeManagementSystem(unittest.TestCase):

    def setUp(self):
        # Create sample data for testing
        self.company = Company()

        hr = Department("HR")
        hr.add_employee(Employee("John Doe", 101, "HR Specialist", "HR"))
        hr.add_employee(Employee("Jane Smith", 102, "HR Manager", "HR"))
        self.company.add_department(hr)

        it = Department("IT")
        it.add_employee(Employee("Bob Johnson", 201, "Software Engineer", "IT"))
        it.add_employee(Employee("Alice Lee", 202, "System Analyst", "IT"))
        self.company.add_department(it)

    def tearDown(self):
        # Clean up any resources if needed
        pass

    def test_add_employee(self):
        hr_department = self.company.departments["HR"]
        hr_department.add_employee(Employee("Alex Johnson", 103, "HR Assistant", "HR"))
        self.assertEqual(len(hr_department.employees), 3)

    def test_remove_employee(self):
        it_department = self.company.departments["IT"]
        it_department.remove_employee(it_department.employees[0])
        self.assertEqual(len(it_department.employees), 1)

    def test_display_departments(self):
        # Redirect stdout to capture printed output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        self.company.display_departments()
        sys.stdout = sys.__stdout__  # Reset redirect.

        # Check if the output contains the expected department names
        expected_output = "Department: HR\nDepartment: IT\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_save_and_load_data(self):
        # Save data to a file
        filename = "company_data.json"
        self.company.save_to_file(filename)

        # Load data from the file
        new_company = Company()
        new_company.load_from_file(filename)

        # Check if the loaded data matches the original data
        self.assertEqual(self.company.departments.keys(), new_company.departments.keys())

        for department_name, department in self.company.departments.items():
            self.assertEqual(len(department.employees), len(new_company.departments[department_name].employees))

        # Clean up the test file
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
