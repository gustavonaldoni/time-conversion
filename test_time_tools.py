import unittest
from time_tools import TimeTools

class TestTimeTools(unittest.TestCase):
    time_tool = TimeTools()

    def test_calculate_seconds(self):
        examples = {
            '02:38:04' : 9484,
            '01:00:00' : 3600,
            '24:00:00' : 86400        
        }

        for key in examples:
            self.assertEqual(self.time_tool.calculate_seconds(key), examples[key])

    def test_convert_seconds(self):
        examples = {
            78968 : '21:56:08',
            7896 : '02:11:36',
            3600 : '01:00:00',
            86400 : '24:00:00'
        }

        for key in examples:
            self.assertEqual(self.time_tool.convert_seconds(key), examples[key])

if __name__ == "__main__":
    unittest.main()