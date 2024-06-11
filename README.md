# sqlalchemy_challenge
# Shannon Hoffman
# README file

# Files included
# Pat 1 Jupyter notebook file: part_one_climate_analysis.ipynb
# Part 2 .py file for Climate App: part_two_climate_app.py

# Resources
    Class notes
    Instructor Tom Bogue
    TA Jordan Thompkins
    Classmates (including brief conversations with Lorenzo, Elisabeth, 
        Jim, and Chelsea). 
    Xpert Learning Assistant/ChatGPT
    Coronel, C., Morris, S., & Rob, P. (2012). Database systems: Design, 
        implementation, and management (10th ed.). Cengage Learning.
    SQLtutorial.org
    pandas.pydata.org


# Part 1
Reviewed each .csv file to create logic model.

department.csv
-dept_no varchar(10) PK
-dept_name varchar(50)

dept_emp.csv
-emp_no varchar(20)
-dept_no varchar(10)

dept_manager.csv
-dept_no varchar(10)
-emp_no varchar(20)

employees.csv
-emp_no PK varchar(20)
-emp_title_id FK varchar(20)
-birth_date datetime
-first_name varchar(50)
-last_name varchar(50)
-sex char(1)
-hire_date datetime

salaries.csv
-emp_no varchar(20)
-salary int

titles.csv
-title_id PK varchar(20)
-title varchar(50)


# Creating the Entity Relationship Diagram
In employees.csv, title_id and emp_title_id are PK/FK
dept_emp.csv requires a composite key because an employee can belong to
multiple departments over time. 

dept_manager.csv requires a composite key because an employee can manage
multiple departments over time.

salaries.csv requres a composite key because an employee can have more than
one salary over time.

department.csv
-dept_no varchar(10) PK
-dept_name varchar(50)

titles.csv
-title_id varchar(20) PK
-title varchar(50)

employees.csv
-emp_no varchar(20) PK
-emp_title_id varchar(20) FK
-birth_date datetime
-first_name varchar(50)
-last_name varchar(50)
-sex char(1)
-hire_date datetime

dept_emp.csv
-emp_no varchar(20) PK, FK
-dept_no varchar(10) PK, FK

dept_manager.csv
-dept_no varchar(10) PK, FK
-emp_no varchar(20) PK, FK

salaries.csv
-emp_no varchar(20) PK, FK
-salary int


# Data Engineering
Creating the table schema, etc. in pgAdmin4
working in PostgreSQL
Database title: Pewlett Hackard
Checking NOT NULL (determined based on PK, FK, and 
mandatory values - all employee.csv data required.)

department.csv
-dept_no VARCHAR(10) PRIMARY KEY
-dept_name VARCHAR(50) NOT NULL

titles.csv
-title_id VARCHAR(20) PRIMARY KEY
-title VARCHAR(50) NOT NULL

employees.csv
-emp_no VARCHAR(20) PRIMARY KEY
-emp_title_id VARCHAR(20) NOT NULL
-birth_date TIMESTAMP NOT NULL
-first_name VARCHAR(50) NOT NULL
-last_name VARCHAR(50) NOT NULL
-sex CHAR(1) NOT NULL
-hire_date TIMESTAMP NOT NULL
-FOREIGN KEY (emp_title_id) REFERENCES titles(title_id)

dept_emp.csv
-emp_no VARCHAR(20) NOT NULL
-dept_no VARCHAR(10) NOT NULL
-PRIMARY KEY (emp_no, dept_no)
-FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
-FOREIGN KEY (dept_no) REFERENCES department(dept_no)

dept_manager.csv
-dept_no VARCHAR(10) NOT NULL
-emp_no VARCHAR(20) NOT NULL
-PRIMARY KEY (dept_no, emp_no)
-FOREIGN KEY (dept_no) REFERENCES department(dept_no)
-FOREIGN KEY (emp_no) REFERENCES employees(emp_no)

salaries.csv
-emp_no VARCHAR(20) NOT NULL
-salary INT NOT NULL
-PRIMARY KEY (emp_no, salary)
-FOREIGN KEY (emp_no) REFERENCES employees(emp_no)


Data imported.

# Data Analysis
Utilized pgAdmin4 to create queries for Data Analysis