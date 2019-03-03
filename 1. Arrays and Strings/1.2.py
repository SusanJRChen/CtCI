import unittest

def check_permutation(word1, word2):
    diction = {}

    for i in word1:
        if i in diction:
            diction[i] += 1
        else:
            diction[i] = 1
    
    for i in word2:
        if i in diction:
            if diction[i] == 1:
                del diction[i]
            else:
                diction[i] -= 1
        else:
            return False
            
    if diction == {}:
        return True
    else:
        return False

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()