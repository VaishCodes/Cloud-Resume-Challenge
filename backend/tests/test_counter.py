from backend.lambda_function import increment_count

def test_increment_count_from_zero():
    assert increment_count(0) == 1

def test_increment_count_from_positive():
    assert increment_count(5) == 6

def test_increment_count_large_number():
    assert increment_count(999) == 1000
