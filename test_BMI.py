# Test BMI function

from bmi import *

def test1_BMI():
    height_feet = 5
    height_inches = 3
    weight_lbs = 125

    assert BMI(height_feet, height_inches, weight_lbs) == "Normalweight"

def test2_BMI():
    height_feet = "invalid"
    height_inches = "invalid"
    weight_lbs = "invalid"

    assert BMI(height_feet, height_inches, weight_lbs) == "invalid"

