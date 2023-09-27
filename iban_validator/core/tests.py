from django.test import TestCase

from core.utils import translate_iban, valid_iban, generate_iban_check_digits, iban_is_genuine

# From the django official documentation:
"""
What should you test?
You should test all aspects of your own code, but not any libraries or functionality provided as part of Python or Django.
"""


class TestTranslateIBAN(TestCase):

    def test_translate_iban_no_input(self):
        with self.assertRaises(TypeError):
            translate_iban()
    
    def test_translate_iban_empty_string(self):
        self.assertEquals(translate_iban(''), '')

    def test_translate_iban_wrong_input_type(self):
        with self.assertRaises(TypeError):
            translate_iban([1, 2, 3])
    
    def test_translate_iban_short_string_digit(self):
        self.assertEqual(translate_iban('1'),'1')
    
    def test_translate_iban_short_string_nr(self):
        self.assertEqual(translate_iban('a'),'10')
    
    def test_translate_iban_only_letters(self):
        self.assertEqual(translate_iban('abcdefgh'),'1415161710111213')
    
    def test_translate_iban_only_letters_uppercase(self):
        self.assertEqual(translate_iban('ABCDEFGH'),'1415161710111213')
    
    def test_translate_iban_only_digits(self):
        self.assertEqual(translate_iban('1123612315235'),'6123152351123')
            
    def test_translate_iban_invalid_iban(self):
        iban = 'ME25505000012345678952'
        expected_result = '505000012345678952221425'
        self.assertEqual(translate_iban(iban), expected_result)
    
    def test_translate_iban_valid_iban(self):
        iban = 'ME25505000012345678951'
        expected_result = '505000012345678951221425'
        self.assertEqual(translate_iban(iban), expected_result)

class TestValidIBAN(TestCase):
    def test_valid_iban_no_input(self):
        with self.assertRaises(TypeError):
            valid_iban()
    
    def test_valid_iban_empty_string(self):
        self.assertEqual(valid_iban(''), False)

    def test_valid_iban_wrong_input_type(self):
        with self.assertRaises(TypeError):
            valid_iban([1, 2, 3])
    
    def test_valid_iban_short_string_digit(self):
        self.assertEqual(valid_iban('1'), False)
    
    def test_valid_iban_short_string_nr(self):
        self.assertEqual(valid_iban('a'), False)
    
    def test_valid_iban_only_letters(self):
        self.assertEqual(valid_iban('abcdefgh'),False)
    
    def test_valid_iban_only_letters_uppercase(self):
        self.assertEqual(valid_iban('ABCDEFGH'), False)
    
    def test_valid_iban_only_digits(self):
        self.assertEqual(valid_iban('1123612315235'), False)
            
    def test_valid_iban_invalid_iban(self):
        iban = 'ME25505000012345678952'
        self.assertEqual(valid_iban(iban), False)
    
    def test_valid_iban_valid_iban(self):
        iban = 'ME25505000012345678951'
        self.assertEqual(valid_iban(iban), True)

class TestGenerateCheckDigits(TestCase):

    def test_g_check_digits_no_input(self):
        with self.assertRaises(TypeError):
            valid_iban()
    
    def test_g_check_digits_empty_string(self):
        self.assertEqual(generate_iban_check_digits(''), '98')

    def test_g_check_digits_wrong_input_type(self):
        with self.assertRaises(TypeError):
            generate_iban_check_digits([1, 2, 3])
    
    def test_g_check_digits_short_string_digit(self):
        self.assertEqual(generate_iban_check_digits('1'), '95')
    
    def test_g_check_digits_short_string_nr(self):
        self.assertEqual(generate_iban_check_digits('a'), '68')
    
    def test_g_check_digits_only_letters(self):
        self.assertEqual(generate_iban_check_digits('abcdefgh'), '83')
    
    def test_g_check_digits_only_letters_uppercase(self):
        self.assertEqual(generate_iban_check_digits('ABCDEFGH'), '83')
    
    def test_g_check_digits_only_digits(self):
        self.assertEqual(generate_iban_check_digits('1123612315235'), '88')
            
    def test_g_check_digits_invalid_iban(self):
        iban = 'ME25505000012345678952'
        self.assertEqual(generate_iban_check_digits(iban), '95')
    
    def test_g_check_digits_valid_iban(self):
        iban = 'ME25505000012345678951'
        self.assertEqual(generate_iban_check_digits(iban), '25')


class TestIBANisGenuine(TestCase):
    
    def test_iban_is_genuine_no_input(self):
        with self.assertRaises(TypeError):
            iban_is_genuine()
    
    def test_iban_is_genuine_empty_string(self):
        self.assertEqual(iban_is_genuine(''), False)

    def test_iban_is_genuine_wrong_input_type(self):
        with self.assertRaises(TypeError):
            iban_is_genuine([1, 2, 3])
    
    def test_iban_is_genuine_short_string_digit(self):
        self.assertEqual(iban_is_genuine('1'), False)
    
    def test_iban_is_genuine_short_string_nr(self):
        self.assertEqual(iban_is_genuine('a'), False)
    
    def test_iban_is_genuine_only_letters(self):
        self.assertEqual(iban_is_genuine('abcdefgh'), False)
    
    def test_iban_is_genuine_only_letters_uppercase(self):
        self.assertEqual(iban_is_genuine('ABCDEFGH'), False)
    
    def test_iban_is_genuine_only_digits(self):
        self.assertEqual(iban_is_genuine('1123612315235'), False)
            
    def test_iban_is_genuine_invalid_iban(self):
        iban = 'ME25505000012345678952'
        self.assertEqual(iban_is_genuine(iban), False)
    
    def test_iban_is_genuine_valid_iban(self):
        iban = 'ME25505000012345678951'
        self.assertEqual(iban_is_genuine(iban), True)