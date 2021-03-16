'''
The file is used to do unmocked testing

'''

import unittest

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_EXPECTED1 = "name_expected"
KEY_EXPECTED2 = "score_expected"


class SplitTestCase(unittest.TestCase):
    '''This class is used to extend the unittest.TestCase and performs splitting of the string'''
    def setUp(self):
        self.success_test_params_one = [{
            KEY_INPUT:
            "Sunny Abhi",
            KEY_EXPECTED: ["Sunny", "Abhi"],
        }]
        self.success_test_params_two = [{
            KEY_INPUT:
            "Sunny Abhi SR",
            KEY_EXPECTED: ["Sunny", "Abhi", "SR"],
        }]
        self.success_test_params_three = [{
            KEY_INPUT:
            "Sunny Abhi SR AR",
            KEY_EXPECTED: ["Sunny", "Abhi", "SR", 'AR'],
        }]

    def test_split_success(self):
        '''This function is used to split string and replicates the way it was done in app.py'''
        for test in self.success_test_params_one:
            actual_result = test[KEY_INPUT].split()
            print(actual_result)
            expected_result = test[KEY_EXPECTED]
            print(expected_result)

            self.assertEqual(actual_result[1], expected_result[1])
            self.assertEqual(len(actual_result[1]), len(expected_result[1]))

        for test in self.success_test_params_two:
            actual_result = test[KEY_INPUT].split()
            print(actual_result)
            expected_result = test[KEY_EXPECTED]
            print(expected_result)

            self.assertEqual(actual_result[2], expected_result[2])
            self.assertEqual(len(actual_result[2]), len(expected_result[2]))

        for test in self.success_test_params_three:
            actual_result = test[KEY_INPUT].split()
            print(actual_result)
            expected_result = test[KEY_EXPECTED]
            print(expected_result)

            self.assertEqual(actual_result[3], expected_result[3])
            self.assertEqual(len(actual_result[3]), len(expected_result[3]))


class ScoreCheck(unittest.TestCase):
    '''Class extend unittest.TestCase and check if username and score are synchronously stored'''
    def setUp(self):
        self.success_test_params_user_score_one = [{
            KEY_INPUT: {
                "Sunny": 101
            },
            KEY_EXPECTED1: ["Sunny"],
            KEY_EXPECTED2: [101],
        }]

        self.success_test_params_user_score_two = [{
            KEY_INPUT: {
                "Sunny": 101,
                "Abhi": 102
            },
            KEY_EXPECTED1: ["Sunny", "Abhi"],
            KEY_EXPECTED2: [101, 102],
        }]

        self.success_test_params_user_score_three = [{
            KEY_INPUT: {
                "Sunny": 101,
                "Abhi": 102,
                "SR": 99
            },
            KEY_EXPECTED1: ["Sunny", "Abhi", "SR"],
            KEY_EXPECTED2: [101, 102, 99],
        }]

        self.success_test_params_user_score_four = [{
            KEY_INPUT: {
                "Sunny": 101,
                "Abhi": 102,
                "SR": 99,
                "AR": 98
            },
            KEY_EXPECTED1: ["Sunny", "Abhi", "SR", "AR"],
            KEY_EXPECTED2: [101, 102, 99, 98],
        }]

    def test_scores(self):
        '''This function checks if the result obtained matches the format shown above'''
        for test in self.success_test_params_user_score_one:
            actual_result = test[KEY_INPUT]
            print(actual_result)
            expected_result1 = test[KEY_EXPECTED1]
            print(expected_result1)
            expected_result2 = test[KEY_EXPECTED2]
            print(expected_result2)

            self.assertEqual(
                list(actual_result.keys())[0], expected_result1[0])
            self.assertEqual(actual_result[list(actual_result.keys())[0]],
                             expected_result2[0])

        for test in self.success_test_params_user_score_two:
            actual_result = test[KEY_INPUT]
            print(actual_result)
            expected_result1 = test[KEY_EXPECTED1]
            print(expected_result1)
            expected_result2 = test[KEY_EXPECTED2]
            print(expected_result2)

            self.assertEqual(
                list(actual_result.keys())[1], expected_result1[1])
            self.assertEqual(actual_result[list(actual_result.keys())[1]],
                             expected_result2[1])

        for test in self.success_test_params_user_score_three:
            actual_result = test[KEY_INPUT]
            print(actual_result)
            expected_result1 = test[KEY_EXPECTED1]
            print(expected_result1)
            expected_result2 = test[KEY_EXPECTED2]
            print(expected_result2)

            self.assertEqual(
                list(actual_result.keys())[2], expected_result1[2])
            self.assertEqual(actual_result[list(actual_result.keys())[2]],
                             expected_result2[2])

        for test in self.success_test_params_user_score_four:
            actual_result = test[KEY_INPUT]
            print(actual_result)
            expected_result1 = test[KEY_EXPECTED1]
            print(expected_result1)
            expected_result2 = test[KEY_EXPECTED2]
            print(expected_result2)

            self.assertEqual(
                list(actual_result.keys())[3], expected_result1[3])
            self.assertEqual(actual_result[list(actual_result.keys())[3]],
                             expected_result2[3])


if __name__ == '__main__':
    unittest.main()
