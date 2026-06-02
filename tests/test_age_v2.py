import age_v2

def test_get_age():
    # Arrange
    ERROR = -1
    CHILD_PRICE = 7.50
    ADULT_PRICE = 10.50
    SENIOR_PRICE = 6.50
    
    # Act
    # Invalid
    str_input = age_v2.check_age("XLII")
    decimal_input = age_v2.check_age("12.5")
    
    # Boundary
    low_input = age_v2.check_age(11)
    hi_input = age_v2.check_age(115)

    # Expected
    exp_inp_low = age_v2.check_age(12)
    exp_inp = age_v2.check_age(13)
    exp_adlt = age_v2.check_age(55)
    exp_bnd_hi = age_v2.check_age(113)
    exp_inp_hi = age_v2.check_age(114)

    # Assert
    assert str_input == ERROR
    assert decimal_input == ERROR

    assert low_input == ERROR
    assert hi_input == ERROR

    assert exp_inp_low == CHILD_PRICE
    assert exp_inp == CHILD_PRICE
    assert exp_adlt == ADULT_PRICE
    assert exp_bnd_hi == SENIOR_PRICE
    assert exp_inp_hi == SENIOR_PRICE

