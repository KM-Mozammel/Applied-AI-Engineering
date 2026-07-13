from Testing import add, subtract, square, divide, LinearModel
import pytest

# def test_add_positive():
#     assert add(5, 3) == 8

# def test_add_negative():
#     assert add(-5, -3) == -8

# def test_add_zero():
#     assert add(5, 0) == 5

# def test_add_mixed():
#     assert add(-5, 10) == 5
    
    
# def test_subtract():
#     assert subtract(5, 2) == 3
    
# def test_subtract_minus():
#     assert subtract(6, 6) == 0
    
# def test_subtract_negative():
#     assert subtract(6, 8) == -2

# @pytest.fixture
# def names ():
#     return ["Alice", "Bob", "Charlie"]

# def test_length(names):
#     assert len(names) == 3
    
# def test_firstItem(names):
#     assert names[0] == "Alice"
    
# def test_has_in_list(names):
#     assert "Bob" in names

# def test_divide_zero():
#     with pytest.raises(ZeroDivisionError):
#         divide(3, 0)

def test_predict_zero():
    model = LinearModel(weight=2, bias=1)
    assert model.predict(0) == 1