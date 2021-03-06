import unittest
from pythonUnitest import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multi_word(self):
        text = 'great python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Great Python')

if __name__=='__main__':
    unittest.main()
