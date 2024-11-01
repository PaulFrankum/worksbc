
import requests

def fetch_data(url):
    """Function to fetch data from an API endpoint."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()


def test_fetch_data():
    """Test the fetch_data function without mocking (not recommended)."""
    url = "https://catfact.ninja/fact"
    data = fetch_data(url)
    assert data['length'] == 43  # Check that the fetched data has id = 1


from unittest.mock import patch

@patch('requests.get')
def test_fetch_data_mocked(mock_get):
    """Test the fetch_data function with mocking."""
    # Arrange: Set up the mock to return a specific response
    mock_get.return_value.json.return_value = {'length': 116, 'fact': 'A cat almost never meows at another cat, mostly just humans. Cats typically will spit, purr, and hiss at other cats.'}
    
    # Act: Call the function under test
    url = "https://catfact.ninja/fact"
    data = fetch_data(url)

    # Assert: Check the results
    assert data['length'] == 116
    assert data['fact'] == 'A cat almost never meows at another cat, mostly just humans. Cats typically will spit, purr, and hiss at other cats.'
    mock_get.assert_called_once_with(url)  # Ensure the mock was called with the correct URL
