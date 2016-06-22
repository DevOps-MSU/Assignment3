from retirement import *


def test_savings_goal1():
    age = 48
    annual_sal = 98000
    percentage = 10
    goal = 1000000

    assert calucate_years_to_goal(age, annual_sal, percentage, goal) == 99
    

def test_savings_goal2():
    age = 46
    annual_sal = 98000
    percentage = 10
    goal = 1000000
    
    assert calucate_years_to_goal(age, annual_sal, percentage, goal) == 44

def test_savings_goal3():
    age = 21
    annual_sal = 98000
    percentage = 10
    goal = 1000000
    
    assert calucate_years_to_goal(age, annual_sal, percentage, goal) == 72


def test_savings_goal4():
    age = 50
    annual_sal = 90000
    percentage = 10
    goal = 1000000
    
    assert calucate_years_to_goal(age, annual_sal, percentage, goal) == 'x'


def test_savings_goal5():
    age = 50
    annual_sal = 90000
    percentage = 10
    goal = 1000000
    
    assert calucate_years_to_goal(age, annual_sal, percentage, goal) == "Num"

def test_savings_goal6():
    age = 50
    annual_sal = 90000
    percentage = 10
    goal = 1000000
    
    assert calucate_years_to_goal(age, annual_sal, percentage, goal) == 0

def test_savings_goal7():
    age = 32
    annual_sal = 32000
    percentage = 20
    goal = 700000
    
    assert calucate_years_to_goal(age, annual_sal, percentage, goal) == 86



