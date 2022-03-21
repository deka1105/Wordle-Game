
import unittest
from HW03_Shubham_Dekatey_ui import UiX as ui
from HW03_Shubham_Dekatey_wordle import WordleX as wordle
from HW03_Shubham_Dekatey_dictionary import DictionaryX as dictionary
from unittest.mock import patch
class TesterIO(unittest.TestCase):
    
    def testAttemptsEmpty(self) -> None:
        """Check if 5Letter file is being created"""
        self.assertEqual(dictionary.filter5letterWord(5), 0)

    def test_user_input_with_word(self) -> None :
        """Test when the input and the word is same"""
        self.assertEqual(wordle.checker("melon", "melon", 1), 1)
    
    def test_user_input_with_wrong_word(self) -> None :
        """Test when the input and the word is not same"""
        self.assertNotEqual(wordle.checker("melon", "lists", 1), 1)

    def test_user_input_with_only_char(self) -> None :
        """Test when the input is only"""
        self.assertIsNotNone(ui.checkChar("melon"), 1)

    def test_user_input_with_num(self) -> None :
        """Test when the input consists number"""
        self.assertIsNone(ui.checkChar("melo7n"), 1)
    
    def test_user_input_with_specialChar(self) -> None :
        """Test when the input consists special characters"""
        self.assertIsNone(ui.checkChar("melo$n"), 1)

    def test_user_input_in_dictionary(self) -> None :
        """Test when the input word is in dictionary"""
        self.assertEqual(dictionary.checkWordExists("melon"), 1)
    
    # def test_user_input_not_in_dictionary(self) -> None :
    #     """Test when the input and the word is same"""
    #     self.assertNotEquals(dictionary.checkWordExists("valley"), 0)

    #@patch('builtins.input', side_effect = ["melon", 'y'])
    def test_user_input_length_correct(self) -> None :
        """Test when the input length is correct"""
        self.assertEqual((ui.checkInp("melon")),5)
    
    def test_user_input_length_incorrect(self) -> None :
        """Test when the input length is incorrect"""
        self.assertNotEqual((ui.checkInp("valley")),5)

    def test_user_input_new_attempt(self) -> None :
        """Test when the input is new attempt"""
        self.assertFalse(ui.checkAttempts("melon", ["lists"]), 1)

    def test_user_input_existing_attempt(self) -> None :
        """Test when the input present in previous attempts"""
        self.assertTrue(ui.checkAttempts("melon", ["melon"]), 1)


    def check_file_freq(self) -> None:
        """Check if the Frequeny CSV file is created"""
        import pathlib as pl
        path = pl.Path("letterFrequency.csv")
        self.assertEquals((str(path), path.is_file()), (str(path), True))
        
    def check_file_rank(self) -> None:
        """Check if the Rank CSV file is created"""
        import pathlib as pl
        path = pl.Path("wordRank.csv")
        self.assertEquals((str(path), path.is_file()), (str(path), True))


if __name__ == '__main__':
    unittest.main()