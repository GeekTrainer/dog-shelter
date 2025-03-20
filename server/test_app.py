import unittest
from unittest.mock import patch, MagicMock
import json
from app import app  # Changed from relative import to absolute import

# filepath: server/test_app.py
class TestApp(unittest.TestCase):
    def setUp(self):
        # Create a test client using Flask's test client
        self.app = app.test_client()
        self.app.testing = True
        # Turn off database initialization for tests
        app.config['TESTING'] = True
        
    @patch('app.db.session.query')
    def test_get_dogs_success(self, mock_query):
        # Setup mock data properly
        dog1 = MagicMock(spec=['to_dict', 'id', 'name', 'breed'])
        dog1.id = 1
        dog1.name = "Buddy"
        dog1.breed = "Labrador"
        dog1.to_dict.return_value = {'id': 1, 'name': "Buddy", 'breed': "Labrador"}
        
        dog2 = MagicMock(spec=['to_dict', 'id', 'name', 'breed'])
        dog2.id = 2
        dog2.name = "Max"
        dog2.breed = "German Shepherd"
        dog2.to_dict.return_value = {'id': 2, 'name': "Max", 'breed': "German Shepherd"}
        
        mock_dogs = [dog1, dog2]
        
        # Configure the mock to return our test data
        mock_query_instance = MagicMock()
        mock_query.return_value = mock_query_instance
        mock_query_instance.join.return_value = mock_query_instance
        mock_query_instance.all.return_value = mock_dogs
        
        # Make the request
        response = self.app.get('/api/dogs')
        
        # Check status code
        self.assertEqual(response.status_code, 200)
        
        # Check response data
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['name'], "Buddy")
        self.assertEqual(data[0]['breed'], "Labrador")
        self.assertEqual(data[1]['id'], 2)
        self.assertEqual(data[1]['name'], "Max")
        self.assertEqual(data[1]['breed'], "German Shepherd")
        
        # Verify query was called with the right parameters
        mock_query.assert_called_once()
        
    @patch('app.db.session.query')
    def test_get_dogs_empty(self, mock_query):
        # Configure the mock to return empty data
        mock_query_instance = MagicMock()
        mock_query.return_value = mock_query_instance
        mock_query_instance.join.return_value = mock_query_instance
        mock_query_instance.all.return_value = []
        
        # Make the request
        response = self.app.get('/api/dogs')
        
        # Check status code
        self.assertEqual(response.status_code, 200)
        
        # Check response data - should be empty list
        data = json.loads(response.data)
        self.assertEqual(data, [])
        
    @patch('app.db.session.query')
    def test_get_dogs_structure(self, mock_query):
        # Setup mock data with one dog
        dog = MagicMock(spec=['to_dict', 'id', 'name', 'breed'])
        dog.id = 1
        dog.name = "Buddy"
        dog.breed = "Labrador"
        dog.to_dict.return_value = {'id': 1, 'name': "Buddy", 'breed': "Labrador"}
        
        # Configure the mock
        mock_query_instance = MagicMock()
        mock_query.return_value = mock_query_instance
        mock_query_instance.join.return_value = mock_query_instance
        mock_query_instance.all.return_value = [dog]
        
        # Make the request
        response = self.app.get('/api/dogs')
        
        # Check the response structure
        data = json.loads(response.data)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 1)
        self.assertEqual(set(data[0].keys()), {'id', 'name', 'breed'})


if __name__ == '__main__':
    unittest.main()