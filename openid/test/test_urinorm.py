import os
import unittest
import openid.urinorm


class UrinormTest(unittest.TestCase):
    def __init__(self, desc, case, expected):
        unittest.TestCase.__init__(self)
        self.desc = desc
        self.case = case
        self.expected = expected

    def shortDescription(self):
        return self.desc

    def runTest(self):
        try:
            actual = openid.urinorm.urinorm(self.case)
        except ValueError as why:
            self.assertEqual(self.expected, 'fail', why)
        else:
            self.assertEqual(actual, self.expected)

    def parse(cls, full_case):
        desc, case, expected = full_case.split('\n')
        case = str(case, 'utf-8') if isinstance(case, bytes) else case

        return cls(desc, case, expected)

    parse = classmethod(parse)


def parseTests(test_data):
    result = []

    cases = test_data.split('\n\n')
    for case in cases:
        case = case.strip()

        if case:
            result.append(UrinormTest.parse(case))

    return result


def pyUnitTests():
    here = os.path.dirname(os.path.abspath(__file__))
    test_data_file_name = os.path.join(here, 'urinorm.txt')
    test_data_file = open(test_data_file_name)
    test_data = test_data_file.read()
    test_data_file.close()

    tests = parseTests(test_data)
    return unittest.TestSuite(tests)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(pyUnitTests())
