import pytest
from employee import Employee

def test_give_default_raise():
    emp = Employee("John", "Doe", 60000)
    emp.give_raise()
    assert emp.annual_salary == 65000 

def test_give_custom_raise():
    emp = Employee("Jane", "Smith", 70000)
    emp.give_raise(10000) 
    assert emp.annual_salary == 80000  

@pytest.fixture
def new_employee():
    emp = Employee("Alice", "Johnson", 75000)
    return emp

def test_give_default_raise_with_fixture(new_employee):
    new_employee.give_raise()
    assert new_employee.annual_salary == 80000  
    
def test_give_custom_raise_with_fixture(new_employee):
    new_employee.give_raise(2000) 
    assert new_employee.annual_salary == 77000  
