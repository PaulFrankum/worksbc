import pytest

def add(a,b): return a+b

def divide(a,b):
    if a==0 or b==0:
        print("divide")
        return "Divide by Zero"
    else:
        return a/b

def test_add():
    assert add(2,3) ==5

def test_add_negative_numbers():
    assert  add(-1,-1) == -2

def test_add_with_zero():
    assert add(0,5) == 5

def test_divide():
    assert divide(10,5) == 2

def test_divide_by_zero():
    assert divide(10,0) == "Divide by Zero"
