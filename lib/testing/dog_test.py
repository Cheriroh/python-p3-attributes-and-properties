import pytest
from io import StringIO
from contextlib import redirect_stdout

# Assuming Dog is defined in dog.py
from dog import Dog

def test_dog_name_invalid_empty_string():
    dog = Dog(name="")
    # Capture the output of the print statement
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        dog.name = ""
    assert captured_output.getvalue().strip() == "Name must be string between 1 and 25 characters."

def test_dog_name_invalid_not_string():
    dog = Dog(name=123)
    # Capture the output of the print statement
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        dog.name = 123
    assert captured_output.getvalue().strip() == "Name must be string between 1 and 25 characters."

def test_dog_name_invalid_too_long():
    dog = Dog(name="A" * 26)
    # Capture the output of the print statement
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        dog.name = "A" * 26
    assert captured_output.getvalue().strip() == "Name must be string between 1 and 25 characters."
