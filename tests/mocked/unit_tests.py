'''This file is used for mock testing'''
# pylint: disable= E1101, C0413, R0903, W0603, W1508, E0401, E0602, W0107
import unittest
import unittest.mock as mock # pylint: disable=unused-import
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import *
from models import *
KEY_INPUT = "input"
KEY_EXPECTED = "expected"


class AddUserTestCase(unittest.TestCase):
    '''This class and its functions are used to mock a new user being added to a dummy database'''
    def setUp(self):
        '''This function sets up the params that will be tested'''
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
        '''This function replicates DB.session.add()'''
        self.initial_db_mock.append(username)


    def mocked_db_session_commit(self):
        '''This function replicates DB.session.commit()'''
        pass

    def mocked_person_query_all(self):
        '''This function replicates models.Person.query.all()'''
        return self.initial_db_mock

    def test_success(self):
        '''This function checks if the conditions are met'''
        for test in self.success_test_params:
            with patch('app.DB.session.add', self.mocked_db_session_add):
                with patch('app.DB.session.commit', self.mocked_db_session_commit):
                    with patch('models.Person.query') as mocked_query:
                        mocked_query.all = self.mocked_person_query_all
                        actual_result = set_score_newuser(test[KEY_INPUT])
                        print(actual_result)
                        expected_result = test[KEY_EXPECTED]
                        print(expected_result)
                        self.assertEqual(actual_result, expected_result)
                        self.assertEqual(len(actual_result), len(expected_result))
class GetLeaderBoardTestCase(unittest.TestCase):
    '''This class checks if the user is already in db or not'''
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT:'Abhi',
                KEY_EXPECTED:'User Not Is In DB',
            },
            {
                KEY_INPUT:'Brij',
                KEY_EXPECTED: 'User Not Is In DB',
            },
            {
                KEY_INPUT:'Dipm',
                KEY_EXPECTED: 'User Not Is In DB',
            },
            {
                KEY_INPUT:'Sunny',
                KEY_EXPECTED: 'User Is In DB',
            }
        ]

        initial_person = models.Person(username='Sunny', score=100)
        self.initial_db_mock = [initial_person]

    def mocked_db_session_add(self, username):
        '''This function replicates DB.session.add()'''
        self.initial_db_mock.append(username)


    def mocked_db_session_commit(self):
        '''This function replicates DB.session.commit()'''
        pass
    def mocked_person_query_all(self):
        '''This function replicates models.Person.query.all()'''
        return self.initial_db_mock
    def user_check(self):
        '''This function compares the results with expected results'''
        for test in self.success_test_params:
            with patch('app.DB.session.add', self.mocked_db_session_add):
                with patch('app.DB.session.commit', self.mocked_db_session_commit):
                    with patch('models.Person.query') as mocked_query:
                        mocked_query.all = self.mocked_person_query_all
                        actual_result = isuser_in_db(test[KEY_INPUT])
                        print("Actual Result: " + actual_result)
                        expected_result = test[KEY_EXPECTED]
                        print("Expected Result: " + expected_result)
                        self.assertEqual(actual_result, expected_result)
                        self.assertEqual(len(actual_result), len(expected_result))

if __name__ == '__main__':
    unittest.main()
    