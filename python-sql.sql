
CREATE DATABASE crm_tool;

\c crm_tool;


CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);


CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);


INSERT INTO companies (name, location)
VALUES
    ('Tech Corp', 'San Francisco'),
    ('Design Solutions', 'New York');


INSERT INTO employees (name, position, salary, company_id)
VALUES
    ('Yonas Misganaw', 'Junior Software Engineer', 100000.00, 1),
    ('Noah Smith', 'Product Manager', 125000.00, 1),


SELECT * FROM companies;
SELECT * FROM employees;
