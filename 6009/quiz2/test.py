import unittest, pickle, marshal, types, json, hashlib
import quiz2

##################################################
#  Problem 1
##################################################

class TestProblem1(unittest.TestCase):
    def validate(self, expected, returned):
        if returned is not expected:
            self.assertTrue(isinstance(returned, bool),                  \
                            "Your solution did not return a boolean." \
                            "It returned a object of type: {type(returned)}")
            if expected:
                self.assertTrue(False, "\nYour solution returned False but the " \
                                       "sequence is balanced.")
            else:
                self.assertTrue(False, "\nYour solution returned True but the " \
                                       "sequence is not balanced.")

    def test_01(self):
        """ Sequences with only one kind of bracket """
        sequence = '()'
        
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = ']['
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '()())'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '][[]]'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '(()())'
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '(()()))(()()'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '[[]][][][][[]]][[]]'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '(())((())()()(())(()())'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '((()(()))())(((((((())))))))()()()'
        self.validate(True, quiz2.is_balanced(sequence))

    def test_02(self):
        """ Small sequences with both types of brackets """
        sequence = '[]()'
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '([])'
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '([)]'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '(][)'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '[[()][]()]([()[[]]])'
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '[[](]())'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '[(])[[(())]][((]))'
        self.validate(False, quiz2.is_balanced(sequence))

    def test_03(self):
        """ Deeply nested sequences """
        sequence = '([[([[((([((([((([[]])))])))])))]])]])'
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '([[([[((([((((((([[]])))])))])))]])]]))'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '[' * 10 + ']' * 10 + '(' * 11 + ')' * 11
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '[((' * 10 + '))]' * 10 + '([' * 11 + '])' * 11
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '[[((' * 10 + ']]))' * 10 + '[](())'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '([[' * 20 + '))]' * 20 + '(' * 30 + ')' * 30
        self.validate(False, quiz2.is_balanced(sequence))

    def test_04(self):
        """ Moderately sized sequences """
        sequence = '([()]([]))[[[]()]][[[[[]]]]]([([([])])])'
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '([()]([]))[[[[]()]][[[[[]]]]]([([([])])])]'
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '(([()]([]))[[[[]()]][[[[][[]]]]]([([([)])])])]'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '([()](([]))[[[]()]][[[[[]]]]]([([([])])]))'
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '([()]([[]))[[[]()]][[[[[]]]]]([([([])])]))'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '([()]([[]))[[[]()]][[[[[]]]]]([([([])])]))'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = ']' * 20 + ')' * 20
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '([' * 20
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '(' * 10 + ']' * 10
        self.validate(False, quiz2.is_balanced(sequence))

    def test_05(self):
        """ More moderately sized sequences """
        sequence = '[[((())))(]]'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '()' * 20 + '[]' * 20 + '(' * 20 + ')' * 20
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '()' * 20 + '[]' * 20 + '[' + '(' * 20 + ')' * 19 + ']'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '()' * 20 + '[]' * 20 + '[' + '(' * 20 + ')' * 19 + ']'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = ')' * 10 + '(' * 10 + '[' * 10 + ']' * 10
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = ']' * 10 + '[' * 10 + '(' * 10 + ')' * 10
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '((((((([[[[[[)))))))]]]]]]'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '(([([[[()]]])][[()(([()]))([])](())[()]]))' * 10
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '([[((([[[[((((([[[[[[((((((([[[[[[[[((((((((([[[[[[[[[[]]]]]]]]]])))))))))]]]]]]]])))))))]]]]]])))))]]]])))]])'
        self.validate(True, quiz2.is_balanced(sequence))

        sequence = '([[((([[[[((((([[[[[[((((((([[[[[[[[((((((((([[[[[[[[[[]]]]]]]]]])))))))))]]]]]]]])))))))]]]]]])))))]]])])))]])'
        self.validate(False, quiz2.is_balanced(sequence))

        sequence = '(([[)])]' * 20
        self.validate(False, quiz2.is_balanced(sequence))


##################################################
#  Problem 2
##################################################

class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.tries = {}
        for i in range(3, 7):
            with open("resources/trie_" + str(i) + ".pickle", "rb") as f:
                self.tries[i] = pickle.load(f)

    def run_test(self, test_num, expected):
        trie = self.tries[test_num]
        result = quiz2.find_prefixes(trie)
        self.assertEqual(expected, result)

    def test_01(self):
        trie = quiz2.Trie(None,
                {'a': quiz2.Trie(None,
                    {'s': quiz2.Trie(1,
                        {'k': quiz2.Trie(1,
                            {"s":quiz2.Trie(None, {})})
                        }),
                     'n': quiz2.Trie(1,
                        {'d': quiz2.Trie(1, {}),
                         't': quiz2.Trie(1,
                            {"s": quiz2.Trie(1, {})})
                        }),
                    })
                })

        expected = {'as', 'an', 'ant'}
        result = quiz2.find_prefixes(trie)
        self.assertEqual(expected, result)

    def test_02(self):
        trie = quiz2.Trie(None,
                {'s': quiz2.Trie(None,
                    {'u': quiz2.Trie(None,
                        {'n': quiz2.Trie(1,
                            {'n': quiz2.Trie(None,
                                {'y': quiz2.Trie(1, {})})}),
                         'p': quiz2.Trie(None,
                            {'e': quiz2.Trie(None,
                                {'r': quiz2.Trie(1, {})})}),
                         'r': quiz2.Trie(None,
                            {'e':quiz2.Trie(None, {})})}),
                    'h': quiz2.Trie(None, {
                        'i': quiz2.Trie(None, {
                            'n': quiz2.Trie(None, {
                                'e': quiz2.Trie(1, {})})})})}),
                't': quiz2.Trie(None, {
                    'r': quiz2.Trie(None, {
                        'e': quiz2.Trie(None, {
                            'e': quiz2.Trie(1, {})}),
                        'i': quiz2.Trie(None, {
                            'e': quiz2.Trie(1, {})}), 
                        'y': quiz2.Trie(1, {})})})})
        expected = {"sun"}
        result = quiz2.find_prefixes(trie)
        self.assertEqual(expected, result)

    def test_03(self):
        expected = {'love', 'youth', 'thank', 'kind', 'hope'}
        self.run_test(3, expected)

    def test_04(self):
        expected = set()
        self.run_test(4, expected)

    def test_05(self):
        expected = {'arch', 'bus'}
        self.run_test(5, expected)

    def test_06(self):
        expected = {'tach'}
        self.run_test(6, expected)


##################################################
#  Problem 3
##################################################
class TestProblem3(unittest.TestCase):

    @staticmethod
    def load_data(test_num):
        with open('resources/valid_boards_test%s.json' % test_num, 'r') as f:
            data = json.load(f)
        return data

    def board_equivalents(self, board):

        def horizontal_flip(board):
            return board[::-1]

        def vertical_flip(board):
            new_board = [len(board) - 1 - x for x in board]
            return new_board

        def rotate90(board, n):
            rotated_board = [-1]*n
            for col in range(n):
                row = board[col]
                if row == -1: continue
                new_row = n - col - 1
                new_col = row
                rotated_board[new_col] = new_row
            return rotated_board

        def hash_board(board):
            str_board = str(tuple(board)).encode('utf-8')
            hash_fn = hashlib.sha1
            return hash_fn(str_board).hexdigest()

        equivalents = set([hash_board(board)])
        equivalents.add(hash_board(horizontal_flip(board)))
        equivalents.add(hash_board(vertical_flip(board)))
        for i in range(3):
            board = rotate90(board, len(board))
            equivalents.add(hash_board(board))

        return equivalents


    def validate(self, data, k, n, returned):
        if n <= 0 or k <= 0:
            self.assertIsNone(returned,                                             \
                            "\nSolutions are not possible for k={k} and size={n}." \
                            "\nYour solution returned: {returned}.")

        expected = []
        for min_k in data[str(n)]:
            if int(min_k) <= k:
                expected.extend(data[str(n)][str(min_k)])

        if returned is None:
            self.assertTrue(len(expected) == 0,                                 \
                            "\nSolutions are possible for k={k} and size={n}." \
                            "\nYour solution returned None.")
        else:
            self.assertTrue(isinstance(returned, list),                                      \
                            "\nYour solution did not return a list for k={k} and size={n}." \
                            "\nIt returned a object of type: {type(returned)}")

            self.assertTrue(all([isinstance(value, int) or isinstance(value, float) for value in returned]), \
                            "\nYour solution did not return a list of numbers for k={k} and size={n}."      \
                            "\nIt returned a list of objects of types: {set([type(value) for value in returned])}")

            self.assertEqual(n, len(returned),                                                   \
                            "\nYour solution is not the correct length for k={k} and size={n}." \
                            "\nYour solution is length: {len(returned)}, but the board is of size: {n}.")

            number_of_queens = [x for x in returned if x > -1]
            self.assertLessEqual(len(number_of_queens), k,                                 \
                            "\nYour solution has too many queens for k={k} and size={n}." \
                            "\nYour solution placed {len(number_of_queens)} queens, but you must place less than or equal to {k} queens.")

            returned_equivalents = self.board_equivalents(returned)
            self.assertTrue(any([equivalent in expected for equivalent in returned_equivalents]), \
                            "\nYour solution is not a valid solution for k={k} and size={n}."    \
                            "\nYour solution returned {returned}, which either has conflicting queens or does not cover every cell.")
    def test_01(self):
        """ The 1x1 board."""
        data = self.load_data('1')
        self.validate(data, 1, 1, quiz2.k_queens_coverage(1, 1))

    def test_02(self):
        """ The 2x2 board for k in (1, 2)."""
        data = self.load_data('2')
        n = 2
        for k in range(1, n+1):
            self.validate(data, k, n, quiz2.k_queens_coverage(k, n))

    def test_03(self):
        """ The 3x3 board for k in (1, 2, 3)."""
        data = self.load_data('3')
        n = 3
        for k in range(1, n+1):
            self.validate(data, k, n, quiz2.k_queens_coverage(k, n))

    def test_04(self):
        """ Medium boards between than 4x4 and 6x6 with k that produce solutions."""
        data = self.load_data('4')
        self.validate(data, 3, 4, quiz2.k_queens_coverage(3, 4))
        self.validate(data, 4, 4, quiz2.k_queens_coverage(4, 4))

        self.validate(data, 3, 5, quiz2.k_queens_coverage(3, 5))
        self.validate(data, 4, 5, quiz2.k_queens_coverage(4, 5))
        self.validate(data, 5, 5, quiz2.k_queens_coverage(5, 5))

        self.validate(data, 4, 6, quiz2.k_queens_coverage(4, 6))
        self.validate(data, 5, 6, quiz2.k_queens_coverage(5, 6))
        self.validate(data, 6, 6, quiz2.k_queens_coverage(6, 6))

    def test_05(self):
        """ Medium boards between than 4x4 and 6x6 with k that do not produce solutions."""
        data = self.load_data('5')
        self.validate(data, 1, 4, quiz2.k_queens_coverage(1, 4))
        self.validate(data, 2, 4, quiz2.k_queens_coverage(2, 4))

        self.validate(data, 1, 5, quiz2.k_queens_coverage(1, 5))
        self.validate(data, 2, 5, quiz2.k_queens_coverage(2, 5))

        self.validate(data, 1, 6, quiz2.k_queens_coverage(1, 6))
        self.validate(data, 2, 6, quiz2.k_queens_coverage(2, 6))
        self.validate(data, 3, 6, quiz2.k_queens_coverage(3, 6))

    def test_06(self):
        """ Large boards greater than 6x6 with small k that produce solutions."""
        data = self.load_data('6-7')
        self.validate(data, 3, 7, quiz2.k_queens_coverage(3, 7))
        self.validate(data, 4, 7, quiz2.k_queens_coverage(4, 7))
        self.validate(data, 5, 7, quiz2.k_queens_coverage(5, 7))
        self.validate(data, 6, 7, quiz2.k_queens_coverage(6, 7))

        self.validate(data, 5, 8, quiz2.k_queens_coverage(5, 8))
        self.validate(data, 6, 8, quiz2.k_queens_coverage(6, 8))

    def test_07(self):
        """ Large boards greater than 6x6 with large k that produce solutions."""
        data = self.load_data('6-7')
        self.validate(data, 7, 7, quiz2.k_queens_coverage(7, 7))

        self.validate(data, 7, 8, quiz2.k_queens_coverage(7, 8))
        self.validate(data, 8, 8, quiz2.k_queens_coverage(8, 8))

    def test_08(self):
        """ Large boards greater than 6x6 with k that do not produce solutions."""
        data = self.load_data('8')
        self.validate(data, 1, 7, quiz2.k_queens_coverage(1, 7))
        self.validate(data, 2, 7, quiz2.k_queens_coverage(2, 7))

        self.validate(data, 1, 8, quiz2.k_queens_coverage(1, 8))
        self.validate(data, 2, 8, quiz2.k_queens_coverage(2, 8))
        self.validate(data, 3, 8, quiz2.k_queens_coverage(3, 8))
        self.validate(data, 4, 8, quiz2.k_queens_coverage(4, 8))

    def test_09(self):
        """ Impossible values of k."""
        data = self.load_data('9')
        for n in range(1, 9):
            self.validate(data, 0, n, quiz2.k_queens_coverage(0, n))

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
