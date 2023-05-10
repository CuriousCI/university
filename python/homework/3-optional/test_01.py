import testlib
import random
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG = True
DEBUG = False


@ddt
class Test(testlib.TestCase):

    def do_test(self, sequence_file, a, b, n, expected):
        """Test implementation
        - sequence_file: the file containing the sequence
        - a, b: the interval extremes
        - n: the maximum number of sequences
        - expected: expected result
        TIMEOUT: 1 second for each test
        """
        if DEBUG:
            import program01 as program
            result = program.ex1(sequence_file, a, b, n)
        else:
            with self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_open(allowed_filenames_modes={sequence_file: ['r']}), \
                    self.check_imports(allowed=['program01', '_io', 'encodings.utf_8']), \
                    self.timeout(1), \
                    self.timer(1):
                import program01 as program
                result = program.ex1(sequence_file, a, b, n)
        self.assertEqual(type(result),  list,
                         "The result should be a list / Il risultato prodotto deve essere una lista")
        self.assertEqual(type(result[0]),  tuple,
                         "The returned list should contain tuples / La lista restituita deve contenere tuple")
        self.assertEqual(type(result[0][0]),  int,
                         "The first element in the list’s tuples should be an integer / " +
                         "La prima coordinata delle tuple restituite deve essere un intero")
        self.assertEqual(type(result[0][1]),  list,
                         "The second element in the list’s tuples should be a list / " +
                         "La seconda  coordinata delle tuple restituite deve essere una lista")
        self.assertEqual(type(result[0][1][0]),  str,
                         "The second element in the list’s tuples should be a list of strings / " +
                         "la seconda coordinata delle tuple deve contenere una lista di stringhe")
        self.assertEqual(result,        expected,
                         "The returned list is incorrect / " +
                         "La lista restituita non e' corretta")
        return 1

    @file_data("test_01.json")
    def test_json(self, filename, da, a, n, expected):
        expected = list(map(tuple, expected))
        return self.do_test(filename, da, a, n, expected)

    @file_data("test_random.json")
    def test_random(self, filename, da, a, n, expected):
        expected = list(map(tuple, expected))
        return self.do_test(filename, da, a, n, expected)


if __name__ == '__main__':
    Test.main()
