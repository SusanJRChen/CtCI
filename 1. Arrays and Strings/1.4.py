import unittest

def pal_perm(word):
    pairs = []
    singles = []
    
    for i in word:
        if i != " ":
            i = i.lower()
            if i not in singles:
                singles.append(i)
            else:
                pairs.append(i)
                singles.remove(i)

    if len(singles) > 1:
        return False
    else: return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()