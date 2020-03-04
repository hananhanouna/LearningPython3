class Employee:
    def __init__(self, first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary

    def show_info(self):
        print(f"First Name : {self.first_name}")
        print(f"Last Name  : {self.last_name}")
        print(f"Title      : {self.title}")
        print(f"Salary     : {self.salary}")


emp = Employee(first_name='Sam', last_name='David', title='Business Analyst', salary=70000)

emp.show_info()





# Add the following functionalities to the Employee class
# if the employee performance is very strong grant 2000 bonus + increase salary by 5 percent
# if the employee performance is excellent grant 4000 bonus + increase salary by 10 percent

# performance values are [inconsistent, strong, very strong, excellent]