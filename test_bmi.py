import DevOps_lab2.bmi as BMI

def test_calculate_bmi_func():
    expected = 0
    result = BMI.calculate_bmi(height=1.85, weight=65)
    assert (result == expected)

def test_calc_bmi_overWeight():
    expected = 1
    result = BMI.calculate_bmi(height=1.85, weight = 100)
    assert (result == expected)

def test_calc_bmi_underWeight():
    expected = -1
    result = BMI.calculate_bmi(height=1.85, weight=40)
    assert (result == expected)