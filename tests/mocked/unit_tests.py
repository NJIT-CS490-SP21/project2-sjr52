import unittest
import unittest.mock as mock
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import *
from models import *
KEY_INPUT = "input"
KEY_EXPECTED = "expected"


class AddUserTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT:'Abhi',
                KEY_EXPECTED: {'Sunny': 100, 'Abhi': 100},
            },
            {
                KEY_INPUT:'Brij',
                KEY_EXPECTED: {'Sunny': 100, 'Abhi': 100, 'Brij': 100},
            },   
            {
                KEY_INPUT:'Dipm',
                KEY_EXPECTED: {'Sunny': 100, 'Abhi': 100, 'Brij':100, 'Dipm':100},
            }   
        ]
        
        initial_person = models.Person(username='Sunny', score=100)
        self.initial_db_mock = [initial_person]
        
        
    def mocked_db_session_add(self, username):
        self.initial_db_mock.append(username)
        
        
    def mocked_db_session_commit(self):
        pass  
    

    def mocked_person_query_all(self):
        return self.initial_db_mock
        
    def test_success(self):
        for test in self.success_test_params:
            with patch('app.DB.session.add', self.mocked_db_session_add):
                with patch('app.DB.session.commit', self.mocked_db_session_commit):
                    with patch('models.Person.query') as mocked_query:
                        mocked_query.all = self.mocked_person_query_all
                         
                        actual_result = Set_Score_NewUser(test[KEY_INPUT])
                        expected_result = test[KEY_EXPECTED]
                        self.assertEqual(actual_result, expected_result)
                        self.assertEqual(len(actual_result),len(expected_result))
                        
if __name__ == '__main__':
    unittest.main()