#!/usr/bin/env python3
import os
import quiz1
import unittest

TEST_DIRECTORY = os.path.dirname(__file__)


##################################################
#  Problem 1
##################################################

class TestProblem1(unittest.TestCase):

    def test_01(self):
        """Unique max index in a three-element list"""
        nums = [10, 1, 7]
        expect = 1
        result = quiz1.max_diff_index(nums)
        self.assertEqual(expect, result)

        nums = [7, 10, 1]
        expect = 2
        result = quiz1.max_diff_index(nums)
        self.assertEqual(expect, result)

    def test_02(self):
        """Unique max index in a short list"""
        nums = [12, -21, 56, -9, -3]
        expect = 2
        result = quiz1.max_diff_index(nums)
        self.assertEqual(expect, result)

        nums = [3, 4, 41, -9, -3]
        expect = 3
        result = quiz1.max_diff_index(nums)
        self.assertEqual(expect, result)

    def test_03(self):
        """Multiple possible max indices in a short list"""
        nums = [19, 8, -3, 6, 2, 6]
        result = quiz1.max_diff_index(nums)
        self.assertIn(result, {1, 2})

        nums = [-10, -11, -12, -15, -18]
        result = quiz1.max_diff_index(nums)
        self.assertIn(result, {3, 4})

    def test_04(self):
        """Multiple possible max indices in a long list"""
        nums = [0, 0, 2, 1, 1, 3, 2, 2, 3, 2, 1, 0]
        result = quiz1.max_diff_index(nums)
        self.assertIn(result, {2, 5})
        
        nums = [1, 4, 5, 4, 2, 1, -2, 1, 2, 3, 4, 6]
        result = quiz1.max_diff_index(nums)
        self.assertIn(result, {1, 6, 7})

##################################################
#  Problem 2
##################################################

class WireDictionary:
    def __init__(self, inner_dict: dict, equivalent_keys):
        self.key_to_id = {key: index for index, key in enumerate(list(inner_dict.keys()))}
        self.equivalents = equivalent_keys
        self.inter_dict = self.process_dict(inner_dict, equivalent_keys)

    def assertEqual(self, other: dict):
        for key in other:
            if key not in self.key_to_id:
                raise AssertionError("Wrong wire dictionary, wire id ", key, "could not be found")
            key_id = self.key_to_id[key]
            value = self.inter_dict[key_id]
            if value != frozenset(other[key]):
                raise AssertionError("Wrong wire value for the following wire id: " + str(key) + ", expected: " +
                                     other[key] + " or " + str((other[key][1], other[key][0])) + " but got: " +
                                     str(tuple(value)))
        if len(other) != len(self.inter_dict):
            raise AssertionError("Wrong number of wires in the wire dictionary, expected: " +
                                 str(len(other)) + " but got: " + str(len(self.inter_dict)))
        assert(True)

    def process_dict(self, inner_dict: dict, equivalent_keys):
        for group in equivalent_keys:
            key_id = self.key_to_id[[key for key in group if key in self.key_to_id][0]]
            for key in group:
                self.key_to_id[key] = key_id
        return {self.key_to_id[key]: frozenset(inner_dict[key]) for key in inner_dict}


class ResistanceDictionary(WireDictionary):
    def __init__(self, inner_dict: dict, equivalent_keys):
        super(ResistanceDictionary, self).__init__(inner_dict, equivalent_keys)

    def assertEqual(self, other: dict):
        for key in other:
            if key not in self.key_to_id:
                raise AssertionError("Wrong wire dictionary, wire id ", key, "could not be found")
            key_id = self.key_to_id[key]
            if abs(self.inter_dict[key_id] - other[key]) > 1e-5:
                raise AssertionError("Wrong resistance value for the following wire id: " + str(key) + ", expected: " +
                                     str(other[key]) + " but got: " + str(self.inter_dict[key_id]))
        if len(other) != len(self.inter_dict):
            raise AssertionError("Wrong number of wires in the wire dictionary, expected: " +
                                 str(len(other)) + " but got: " + str(len(self.inter_dict)))
        assert (True)

    def process_dict(self, inner_dict: dict, equivalent_keys):
        for group in equivalent_keys:
            key_id = self.key_to_id[[key for key in group if key in self.key_to_id][0]]
            for key in group:
                self.key_to_id[key] = key_id
        return {self.key_to_id[key]: inner_dict[key] for key in inner_dict}


class TestProblem2(unittest.TestCase):
    def test_01(self):
        """Test that something is returned"""
        try:
            result = quiz1.replace_parallels({"1": (0, 1)}, {"1": 2})
            self.assertTrue(result is not None, "Your function should return something")
        except RecursionError:
            self.fail("A recursion error occurred, check if your code recurses infinitely")

    def test_02(self):
        """No wires in parallel. Wire ids and junctions are both strings."""
        wires = {'0': ('A', 'B'), '1': ('B', 'C'), '2': ('C', 'A')}
        resistances = {'0': 5, '1': 2, '2': 3}
        try:
            new_wires, new_resistances = quiz1.replace_parallels(wires, resistances)
        except RecursionError:
            self.fail("A runtime error occurred, check if your code recurses infinitely")
        wires_wrapper = WireDictionary(new_wires, set())
        resistances_wrapper = ResistanceDictionary(new_resistances, set())

        try:
            wires_wrapper.assertEqual({'0': ('A', 'B'), '1': ('B', 'C'), '2': ('C', 'A')})
            resistances_wrapper.assertEqual({'0': 5, '1': 2, '2': 3})
        except AssertionError as ex:
            self.fail("No wires in parallel, nothing to simplify: " + str(ex))

    def test_03(self):
        """One cluster of only two wires in parallel; some other wires. String wire ids and junctions."""
        wires = {'wire1': ('X', 'Y'), 'wire2': ('Y', 'X'), 'other1': ('X', 'Z'), 'other2': ('W', 'Y')}
        resistances = {'wire1': 2, 'wire2': 2 / 3, 'other1': 4, 'other2': 2}
        try:
            new_wires, new_resistances = quiz1.replace_parallels(wires, resistances)
        except RecursionError:
            self.fail("A runtime error occurred, check if your code recurses infinitely")
        wires_wrapper = WireDictionary(new_wires, {frozenset(['wire1', 'wire2'])})
        resistances_wrapper = ResistanceDictionary(new_resistances, {frozenset(['wire1', 'wire2'])})

        try:
            wires_wrapper.assertEqual({'wire1': ('X', 'Y'), 'other1': ('X', 'Z'), 'other2': ('W', 'Y')})
            resistances_wrapper.assertEqual({'wire2': 0.5, 'other1': 4, 'other2': 2})
        except AssertionError as ex:
            self.fail(str(ex))

    def test_04(self):
        """One cluster with 4 parallel wires, tuple wire ids are tuples, some tuple junctions."""
        wires = {(0, 0): (("a", "a"), "b"), (0, 1): ("b", ("a", "a")),
                 (0, 2): (("a", "a"), "b"), (0, 3): ("b", ("a", "a")),
                 (1, 1): (("A", "B"), ("a", "a")), (1, 2): (("a", "a"), ("C", "D")),
                 (2, 2): (("A", "B"), ("C", "D"))}
        resistances = {(0, 0): 28, (0, 1): 35, (0, 2): 44, (0, 3): 77,
                       (1, 1): 3, (1, 2): 5, (2, 2): 10}
        try:
            new_wires, new_resistances = quiz1.replace_parallels(wires, resistances)
        except RecursionError:
            self.fail("A runtime error occurred, check if your code recurses infinitely")
        wires_wrapper = WireDictionary(new_wires, {frozenset([(0, 0), (0, 1), (0, 2), (0, 3)])})
        resistances_wrapper = ResistanceDictionary(new_resistances, {frozenset([(0, 0), (0, 1), (0, 2), (0, 3)])})

        expected_wires = {(0, 1): ("b", ("a", "a")), (1, 1): (("A", "B"), ("a", "a")),
                          (1, 2): (("a", "a"), ("C", "D")), (2, 2): (("A", "B"), ("C", "D"))}
        expected_resistances ={(0, 2): 10, (1, 1): 3, (1, 2): 5, (2, 2): 10}
        try:
            wires_wrapper.assertEqual(expected_wires)
            resistances_wrapper.assertEqual(expected_resistances)
        except AssertionError as ex:
            self.fail(str(ex))

    def test_05(self):
        """Two groups of 2 and >2 parallel wires, some tuple wire ids and junctions."""
        wires = {(0, 0): (("a", "a"), "b"), (0, 1): ("b", ("a", "a")),
                 (0, 2): (("a", "a"), "b"), (0, 3): ("b", ("a", "a")),
                 (1, 1): (("A", "B"), ("a", "a")), (1, 2): (("A", "B"), ("C", "D")),
                 (2, 2): (("E", "F"), ("C", "D")), "wire": (("C", "D"), ("E", "F"))}
        resistances = {(0, 0): 16, (0, 1): 72, (0, 2): 80, (0, 3): 90,
                       (1, 1): 3, (1, 2): 5, (2, 2): 20, "wire": 80}
        try:
            new_wires, new_resistances = quiz1.replace_parallels(wires, resistances)
        except RecursionError:
            self.fail("A runtime error occurred, check if your code recurses infinitely")
        equivalent_wires = {frozenset([(0, 0), (0, 1), (0, 2), (0, 3)]), frozenset([(2, 2), "wire"])}
        wires_wrapper = WireDictionary(new_wires, equivalent_wires)
        resistances_wrapper = ResistanceDictionary(new_resistances, equivalent_wires)

        expected_wires = {(0, 1): ("b", ("a", "a")), (1, 1): (("a", "a"), ("A", "B")),
                          (1, 2): (("A", "B"), ("C", "D")), "wire": (("C", "D"), ("E", "F"))}
        expected_resistances = {(0, 3): 10, (1, 1): 3, (1, 2): 5, "wire": 16}
        try:
            wires_wrapper.assertEqual(expected_wires)
            resistances_wrapper.assertEqual(expected_resistances)
        except AssertionError as ex:
            self.fail(str(ex))

    def test_06(self):
        """Big test (a lot of wires) to check performance: 10000 groups of 3 parallel wires."""
        wires = {str(i): (str(int(i) // 3), str((int(i) + 3) // 3)) for i in range(30000)}
        resistances = {str(i): 12 if i % 3 == 0 else (28 if i % 3 == 1 else 42) for i in range(30000)}
        try:
            new_wires, new_resistances = quiz1.replace_parallels(wires, resistances)
        except RecursionError:
            self.fail("A runtime error occurred, check if your code recurses infinitely")
        equivalent_wires = {frozenset([str(i * 3), str(i * 3 + 1), str(i * 3 + 2)]) for i in range(10000)}
        wires_wrapper = WireDictionary(new_wires, equivalent_wires)
        resistances_wrapper = ResistanceDictionary(new_resistances, equivalent_wires)

        expected_wires = {str(i): (str(int(i) // 3), str((int(i) + 3) // 3)) for i in range(0, 30000, 3)}
        expected_resistances = {str(i): 7 for i in range(0, 30000, 3)}
        try:
            wires_wrapper.assertEqual(expected_wires)
            resistances_wrapper.assertEqual(expected_resistances)
        except AssertionError as ex:
            self.fail(str(ex))

##################################################
#  Problem 3
##################################################

class TestProblem3(unittest.TestCase):
    def test_01(self):
        """Tests completely full and completely empty boards."""
        board1 = [1, 1, 1, 1, 1]
        board2 = [0, 0, 0, 0, 0]
        self.assertEqual(5, quiz1.minimum_pegs(board1))
        self.assertEqual(0, quiz1.minimum_pegs(board2))

    def test_02(self):
        """Tests boards with only one possible move."""
        board1 = [1, 1, 0]
        self.assertEqual(1, quiz1.minimum_pegs(board1))

        board2 = [0, 1, 1]
        self.assertEqual(1, quiz1.minimum_pegs(board2))

        board3 = [0]*100
        board3[0]  = 1
        board3[-1] = 1
        board3[-2] = 1
        self.assertEqual(2, quiz1.minimum_pegs(board3))

    def test_03(self):
        """Tests boards with only one possible move at a time."""
        board1 = [1, 1, 1, 0, 1]
        self.assertEqual(2, quiz1.minimum_pegs(board1))

        board2 = [1, 1] + [0, 1]*100
        self.assertEqual(1, quiz1.minimum_pegs(board2))

    def test_04(self):
        """Tests boards with multiple possible moves at a time, and multiple paths to the minimum number of pegs."""
        board1 = [1, 1, 0, 1, 1]
        self.assertEqual(2, quiz1.minimum_pegs(board1))

        board2 = [1, 1, 0, 1, 1] + [0]*1000 + [1, 1, 0, 1, 1]
        self.assertEqual(4, quiz1.minimum_pegs(board2))

    def test_05(self):
        """Tests boards with multiple possible moves at a time, but only one path to the minimum number of pegs."""
        board1 = [1, 1, 1, 0, 1, 1]
        self.assertEqual(2, quiz1.minimum_pegs(board1))

        board2 = [1, 1, 1] + [0, 1]*100
        self.assertEqual(2, quiz1.minimum_pegs(board2))

        board3 = [1]*20 + board1
        self.assertEqual(3, quiz1.minimum_pegs(board3))


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
