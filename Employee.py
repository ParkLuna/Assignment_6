import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __str__(self):
        return f"Name: {self.name}, \nDOB: {self.dob}, \nHeight: {self.height},\nCity: {self.city},\nState: {self.state}\n"

def main():
    employee_list = []

    # Read data from employee.json
    try:
        with open("employee.json", "r") as json_file:
            data = json.load(json_file)

        # Extract employee information and create Employee objects
        employees_data = data.get("employees", [])
        for emp_data in employees_data:
            name = emp_data.get("Name", "")
            dob = emp_data.get("DOB", "")
            height = emp_data.get("Height", 0)
            city = emp_data.get("City", "")
            state = emp_data.get("State", "")
            
            # Create an Employee object and add it to the list
            employee = Employee(name, dob, height, city, state)
            employee_list.append(employee)

        # Print the list of Employee objects
        for employee in employee_list:
            print(employee)

    except FileNotFoundError:
        print("employee.json file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data in employee.json.")

if __name__ == "__main__":
    main()
