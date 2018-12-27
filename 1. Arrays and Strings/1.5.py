import unittest

def one_away(word1, word2):
    al = len(word1)
    bl = len(word2)

    if abs(al - bl) >= 2:
        return False

    diction = {}
    dis = 0
    for i in word1:
        if i in diction:
            diction[i] += 1
        else:
            diction[i] = 1

    if bl < al:
        for i in word2:
            if i not in diction:
                return False
        return True
    else:
        for i in word2:
            if i in diction:
                diction[i] -= 1
                if diction[i] == 0:
                    del diction[i]
            else:
                dis += 1
        
        return dis <= 1

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            print(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()