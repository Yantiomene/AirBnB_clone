#!/usr/bin/python3
"""
Unit Test for User Class
"""
import unittest
from datetime import datetime
from models.base_model import Base.Model
import json

User = models.user.User
model = BaseModel()


class TestUserInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  User  Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new user for testing"""
        self.user = User()

    def test_instantiation(self):
        """... checks if User is properly instantiated"""
        self.assertIsInstance(self.user, User)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_string = str(self.user)
        my_list = ['User', 'id', 'created_at']
        actual = 0
        for sub_string in my_list:
            if sub_string in my_string:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        self.user = User()
        my_string = str(self.user)
        actual = 0
        if 'updated_at' in my_string:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.user.save()
        actual = type(self.user.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.user_json = self.user.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.user_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value User"""
        self.user_json = self.user.to_json()
        actual = None
        if self.user_json['__class__']:
            actual = self.user_json['__class__']
        expected = 'User'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... add email attribute"""
        self.user.email = "bettyalx@gmail.com"
        if hasattr(self.user, 'email'):
            actual = self.user.email
        else:
            actual = ''
        expected = "bettyalx@gmail.com"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
