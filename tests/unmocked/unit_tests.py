'''
The file is used to do unmocked testing, it contains:
Split function to check if the usernames obtained from the form are correctly stored

'''

import unittest


KEY_INPUT = "input"
KEY_EXPECTED ="expected"
KEY_EXPECTED1 ="name_expected"
KEY_EXPECTED2 ="score_expected"


class SplitTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params_one = [
            {
                KEY_INPUT: "Abhi SR AR",
                KEY_EXPECTED: ["Sunny", "Abhi", "SR", 'AR'],
            }
        ]
        self.success_test_params_two = [
            {
                KEY_INPUT: "Abhi SR AR",
                KEY_EXPECTED: ["Sunny", "Abhi", "SR", 'AR'],
            }
        ]
        self.success_test_params_three = [
            {
                KEY_INPUT: "Abhi SR AR",
                KEY_EXPECTED: ["Sunny", "Abhi", "SR", 'AR'],
            }
        ]
        
        
    def test_split_success(self):
        for test in self.success_test_params_one:
            actual_result = test[KEY_INPUT].split()
            expected_result = test[KEY_EXPECTED]
            
            self.assertEqual(actual_result[0], expected_result[1])
            self.assertEqual(len(actual_result[0]), len(expected_result[1]))
            
        for test in self.success_test_params_two:
            actual_result = test[KEY_INPUT].split()
            expected_result = test[KEY_EXPECTED]
            
            self.assertEqual(actual_result[1], expected_result[2])
            self.assertEqual(len(actual_result[1]), len(expected_result[2]))
            
        for test in self.success_test_params_three:
            actual_result = test[KEY_INPUT].split()
            expected_result = test[KEY_EXPECTED]
            
            self.assertEqual(actual_result[2], expected_result[3])
            self.assertEqual(len(actual_result[2]), len(expected_result[3]))
        
        

class ScoreCheck(unittest.TestCase):
    def setUp(self):
        self.success_test_params_User_Score_One = [
            {
                KEY_INPUT: {"Sunny": 101},
                KEY_EXPECTED1: ["Sunny"], 
                KEY_EXPECTED2: [101],
            }
        ]
        
        self.success_test_params_User_Score_Two = [
            {
                KEY_INPUT: {"Sunny": 101, "Abhi": 102},
                KEY_EXPECTED1: ["Sunny", "Abhi"], 
                KEY_EXPECTED2: [101, 102],
            }
        ]
        
        self.success_test_params_User_Score_Three = [
            {
                KEY_INPUT: {"Sunny": 101, "Abhi": 102, "SR": 99},
                KEY_EXPECTED1: ["Sunny", "Abhi", "SR"], 
                KEY_EXPECTED2: [101, 102, 99],
            }
        ]
        
        self.success_test_params_User_Score_Four = [
            {
                KEY_INPUT: {"Sunny": 101, "Abhi": 102, "SR": 99, "AR": 98},
                KEY_EXPECTED1: ["Sunny", "Abhi", "SR", "AR"], 
                KEY_EXPECTED2: [101, 102, 99, 98],
            }
        ]
        
        
    def Test_Scores(self):
        for test in self.success_test_params_User_Score_One:
            actual_result = test[KEY_INPUT]
            expected_result1 = test[KEY_EXPECTED1]
            expected_result2 = test[KEY_EXPECTED2]
            
            self.assertEqual(list(actual_result.keys())[0], expected_result1[0])
            self.assertEqual(actual_result[list(actual_result.keys())[0]], expected_result2[0])
            
            
        for test in self.success_test_params_User_Score_Two:
            actual_result = test[KEY_INPUT]
            expected_result1 = test[KEY_EXPECTED1]
            expected_result2 = test[KEY_EXPECTED2]
            
            self.assertEqual(list(actual_result.keys())[1], expected_result1[1])
            self.assertEqual(actual_result[list(actual_result.keys())[1]], expected_result2[1])
            
        for test in self.success_test_params_User_Score_Three:
            actual_result = test[KEY_INPUT]
            expected_result1 = test[KEY_EXPECTED1]
            expected_result2 = test[KEY_EXPECTED2]
            
            self.assertEqual(list(actual_result.keys())[2], expected_result1[2])
            self.assertEqual(actual_result[list(actual_result.keys())[2]], expected_result2[2])
            
        for test in self.success_test_params_User_Score_Four:
            actual_result = test[KEY_INPUT]
            expected_result1 = test[KEY_EXPECTED1]
            expected_result2 = test[KEY_EXPECTED2]
            
            self.assertEqual(list(actual_result.keys())[3], expected_result1[3])
            self.assertEqual(actual_result[list(actual_result.keys())[3]], expected_result2[3])
            
        

if __name__ == '__main__':
    unittest.main()