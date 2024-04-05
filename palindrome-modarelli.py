import unittest 

def is_palindrome(mystring):
    return mystring[0] == mystring[-1] + mystring[1] == mystring[-2]


class TestPalindrome(unittest.Testcase): 

    def test_a(self):
        resultado = is_palindrome("a")
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome("aa")
        self.assertEqual(resultado, True) 

    def test_ab(self):
        resultado = is_palindrome("ab")
        self.assertEqual(resultado, False) 

    def test_abca(self):
        resultado = is_palindrome("abca")
        self.assertEqual(resultado, False)     

    unittest.main()
      
      
    