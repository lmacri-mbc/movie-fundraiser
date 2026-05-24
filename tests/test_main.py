import age

def test_get_age():
    # Arrange
    expected_err_invalid = "Please enter an integer (i.e. a number which doesn't have a decimal)."
    expected_err_bound_low = "Please enter an integer that is more than (or equal to) 12."
    expected_err_bound_high = "Please enter an integer that is less than 115."
    expected_input = "Thank you"

    # Act
    # Invalid
    str_input = age.check_age("XLII")
    flt_input = age.check_age(12.5)
    
    # Boundary
    low_input = age.check_age(11)
    hi_input = age.check_age(115)

    # Expected
    exp_inp_low = age.check_age(12)
    exp_inp = age.check_age(13)
    exp_bnd_hi = age.check_age(113)
    exp_inp_hi = age.check_age(114)

    # Assert
    assert str_input == expected_err_invalid
    assert flt_input == expected_err_invalid

    assert low_input == expected_err_bound_low
    assert hi_input == expected_err_bound_high

    assert exp_inp_low == expected_input
    assert exp_inp == expected_input
    assert exp_bnd_hi == expected_input
    assert exp_inp_hi == expected_input
