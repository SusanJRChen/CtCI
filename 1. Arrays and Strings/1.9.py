import unittest

def string_rotation(string, sub):
    n = len(string)
    if n != len(sub):
        return False
    else:
        count = 0
        stringa = ""

        for i in range(n):
            if (sub[0:i] in string):
                stringa = sub[0:i]
                count = i
                if count == n:
                    return True
            else:
                if (sub[count:n] in string):
                    return True
                else:
                    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('atwaterbottlew', 'waterbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
