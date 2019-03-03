import unittest

def string_compression(string):
    prev = string[0]
    result = prev
    counter = 0

    for i in string:
        if i == prev:
            counter += 1
        else:
            result += str(counter)
            result += i
            prev = i
            counter = 1
    result += str(counter)

    if len(result) > len(string):
        return string

    return result

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
