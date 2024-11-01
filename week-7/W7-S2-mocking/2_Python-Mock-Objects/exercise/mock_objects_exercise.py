
class Database:
    """Simulated Database class."""
    
    def connect(self):
        """Simulates a database connection."""
        raise NotImplementedError("This method should connect to the database.")

    def fetch_data(self, query):
        """Simulates fetching data from the database."""
        raise NotImplementedError("This method should fetch data based on the query.")

class DataService:
    """Service that uses the Database class to fetch data."""

    def __init__(self, database: Database):
        self.database = database

    def get_user_data(self, user_id):
        """Fetches user data based on user_id."""
        query = f"SELECT * FROM users WHERE id={user_id}"
        return self.database.fetch_data(query)


from unittest.mock import Mock

def test_get_user_data():
    """Test the DataService.get_user_data method using mock objects."""
    
    # Create a mock database object
    mock_database = Mock(spec=Database)

    # Define the behavior of the fetch_data method
    mock_database.fetch_data.return_value = {'id': 13, 'name': 'Jane'}

    # Create an instance of DataService with the mock database
    service = DataService(mock_database)

    # Call the method under test
    result = service.get_user_data(1)

    # Assert the results
    assert result['id'] == 13
    assert result['name'] == 'Jane'
    
    # Verify that the fetch_data method was called with the correct query
    mock_database.fetch_data.assert_called_once_with("SELECT * FROM users WHERE id=1")
