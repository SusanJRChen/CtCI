import unittest

def urlify(word, length):
    word = word[0:int(length) + 1]
    last = 0
    final = ""
    
    for i in range (0,len(word)):
        if (word[i] == " "):
            final += (word[last:i])
            final += "%20"
            last = i+1
        elif (i == len(word)-1):
            final += word[last:len(word)]
    

    return final

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()