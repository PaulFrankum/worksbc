# start writing code from here

# Write a Class**: Create a Python class to model a real-world system. For example, a `BankAccount` class with methods like `deposit()`, `withdraw()`, and `get_balance()`.

# Implement pytest Fixtures**: Write a fixture to handle setup and teardown of your system. For example, you can create a fixture that initializes an instance of the `BankAccount` before tests run and closes it afterward.

# Write Test Cases**:
# Unit Tests**: Write test functions that cover normal functionality and edge cases for your class methods.
# Parameterized Tests**: Use `@pytest.mark.parametrize` to validate the functionality of methods with various inputs. Aim for at least five parameterized test cases.
# Handle Exceptions**: Write tests to ensure that exceptions are raised correctly when invalid inputs are provided (e.g., attempting to withdraw more than the available balance).
# Generate Coverage Reports**: Use `pytest-cov` to check coverage and ensure that all critical paths of your code are tested.
# Run pytest**: Ensure all your test cases pass, and check the coverage report to verify your test completeness.
# Comment Your Code**: Ensure that each section of the script is properly commented for clarity.


## Advanced Challenge (Optional)
# Explore the use of fixtures with different scopes (function, module, class, or session) for efficient resource management.
# Implement grouping of tests using test classes to organize related test cases.
