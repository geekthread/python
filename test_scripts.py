"""
Tests for the Gen_AI_Python learning scripts.

Strategy:
  - Scripts without input(): run via subprocess and assert on stdout lines.
  - Scripts with input() (age_calculator, main): pass stdin via subprocess.
  - Core logic is also tested directly (without running the script) where
    the scripts are too tightly coupled to print statements.

Known issues documented:
  - main.py line 15 contains `message = message.c` which raises AttributeError
    at runtime. TestMainScript covers this and tests the string operations
    the script demonstrates.
"""

import os
import subprocess
import sys
import unittest
from datetime import datetime

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))


def run_script(script_name, stdin_input=None):
    """Run a Python script and return (stdout, stderr, returncode)."""
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    result = subprocess.run(
        [sys.executable, script_path],
        input=stdin_input,
        capture_output=True,
        text=True,
    )
    return result.stdout, result.stderr, result.returncode


# ---------------------------------------------------------------------------
# age_calculator.py
# ---------------------------------------------------------------------------

class TestAgeCalculator(unittest.TestCase):

    def _run(self, name, dob):
        return run_script("age_calculator.py", f"{name}\n{dob}\n")

    def test_runs_successfully(self):
        _, stderr, returncode = self._run("Alice", "1990-01-01")
        self.assertEqual(returncode, 0)
        self.assertEqual(stderr, "")

    def test_output_contains_greeting_and_name(self):
        stdout, _, _ = self._run("Alice", "1990-01-01")
        self.assertIn("Hello", stdout)
        self.assertIn("Alice", stdout)

    def test_age_years_months_days(self):
        stdout, _, returncode = self._run("Bob", "1990-01-01")
        self.assertEqual(returncode, 0)
        age = datetime.now().year - 1990
        self.assertIn(str(age), stdout)
        self.assertIn(str(age * 12), stdout)
        self.assertIn(str(age * 365), stdout)

    def test_recent_birth_year(self):
        stdout, _, returncode = self._run("Charlie", "2010-05-20")
        self.assertEqual(returncode, 0)
        age = datetime.now().year - 2010
        self.assertIn(str(age), stdout)


# ---------------------------------------------------------------------------
# arithmatic.py
# ---------------------------------------------------------------------------

class TestArithmetic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stdout, cls.stderr, cls.returncode = run_script("arithmatic.py")
        cls.lines = cls.stdout.strip().split("\n")

    def test_runs_without_errors(self):
        self.assertEqual(self.returncode, 0)
        self.assertEqual(self.stderr, "")

    # num1=3, num2=2 — six comparison prints
    def test_equal(self):
        self.assertEqual(self.lines[0], "False")   # 3 == 2

    def test_not_equal(self):
        self.assertEqual(self.lines[1], "True")    # 3 != 2

    def test_greater_than(self):
        self.assertEqual(self.lines[2], "True")    # 3 > 2

    def test_less_than(self):
        self.assertEqual(self.lines[3], "False")   # 3 < 2

    def test_greater_than_or_equal(self):
        self.assertEqual(self.lines[4], "True")    # 3 >= 2

    def test_less_than_or_equal(self):
        self.assertEqual(self.lines[5], "False")   # 3 <= 2

    # round() — three prints
    def test_round_no_decimals(self):
        self.assertEqual(self.lines[6], "4")       # round(3.75)

    def test_round_one_decimal(self):
        self.assertEqual(self.lines[7], "3.8")     # round(3.75, 1)

    def test_round_two_decimals(self):
        self.assertEqual(self.lines[8], "3.75")    # round(3.75, 2)

    # string concatenation vs integer addition
    def test_string_concatenation(self):
        self.assertEqual(self.lines[9], "100200")  # '100' + '200'

    def test_integer_addition_after_cast(self):
        self.assertEqual(self.lines[10], "300")    # int('100') + int('200')


# ---------------------------------------------------------------------------
# list.py
# ---------------------------------------------------------------------------

class TestList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stdout, cls.stderr, cls.returncode = run_script("list.py")
        cls.lines = cls.stdout.strip().split("\n")

    def test_runs_without_errors(self):
        self.assertEqual(self.returncode, 0)
        self.assertEqual(self.stderr, "")

    def test_min_of_numbers(self):
        self.assertIn("1", self.stdout)    # min([1,5,2,4,3])

    def test_max_of_numbers(self):
        self.assertIn("5", self.stdout)    # max([1,5,2,4,3])

    def test_sum_of_numbers(self):
        self.assertIn("15", self.stdout)   # sum([1,5,2,4,3])

    def test_average_of_numbers(self):
        self.assertIn("3.0", self.stdout)  # avg = 15 / 5

    def test_math_removed_from_courses(self):
        # 'Math' was removed; membership check prints False
        idx = next(i for i, l in enumerate(self.lines) if "Checking if an item" in l)
        self.assertEqual(self.lines[idx + 1], "False")

    def test_art_still_in_courses(self):
        idx = next(i for i, l in enumerate(self.lines) if "Checking if an item" in l)
        self.assertEqual(self.lines[idx + 2], "True")

    def test_join_separator_present(self):
        self.assertIn(" - ", self.stdout)

    def test_joined_type_is_str(self):
        self.assertIn("<class 'str'>", self.stdout)


# ---------------------------------------------------------------------------
# sets.py
# ---------------------------------------------------------------------------

class TestSets(unittest.TestCase):

    def setUp(self):
        self.courses = {"History", "Math", "Physics", "CompSci"}
        self.art = {"Art", "Design", "History", "Math"}

    def test_script_runs_successfully(self):
        _, stderr, returncode = run_script("sets.py")
        self.assertEqual(returncode, 0)
        self.assertEqual(stderr, "")

    def test_intersection(self):
        self.assertEqual(self.courses & self.art, {"History", "Math"})

    def test_courses_minus_art(self):
        self.assertEqual(self.courses - self.art, {"Physics", "CompSci"})

    def test_art_minus_courses(self):
        self.assertEqual(self.art - self.courses, {"Art", "Design"})

    def test_union(self):
        self.assertEqual(
            self.courses | self.art,
            {"History", "Math", "Physics", "CompSci", "Art", "Design"},
        )

    def test_symmetric_difference(self):
        self.assertEqual(
            self.courses ^ self.art,
            {"Physics", "CompSci", "Art", "Design"},
        )

    def test_issubset_false(self):
        self.assertFalse(self.courses.issubset(self.art))

    def test_issubset_true(self):
        self.assertTrue({"History", "Math"}.issubset(self.courses))

    def test_issuperset_false(self):
        self.assertFalse(self.courses.issuperset(self.art))

    def test_issuperset_true(self):
        self.assertTrue(self.courses.issuperset({"History"}))

    def test_empty_set_length(self):
        self.assertEqual(len(set()), 0)


# ---------------------------------------------------------------------------
# string_concat.py
# ---------------------------------------------------------------------------

class TestStringConcat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stdout, cls.stderr, cls.returncode = run_script("string_concat.py")
        cls.lines = cls.stdout.strip().split("\n")

    def test_runs_without_errors(self):
        self.assertEqual(self.returncode, 0)
        self.assertEqual(self.stderr, "")

    def test_format_method_output(self):
        self.assertEqual(self.lines[0], "Hello , Ankit. Welcome to Python programming!")

    def test_fstring_output_uppercases_name(self):
        self.assertEqual(self.lines[1], "Hello , ANKIT. Welcome to Universe!")

    def test_format_method_logic(self):
        msg = "{} , {}. Welcome to Python programming!".format("Hello", "Ankit")
        self.assertEqual(msg, "Hello , Ankit. Welcome to Python programming!")

    def test_fstring_logic(self):
        msg = f"{'Hello'} , {'Ankit'.upper()}. Welcome to Universe!"
        self.assertEqual(msg, "Hello , ANKIT. Welcome to Universe!")


# ---------------------------------------------------------------------------
# tuples.py
# ---------------------------------------------------------------------------

class TestTuples(unittest.TestCase):

    def test_runs_without_errors(self):
        _, stderr, returncode = run_script("tuples.py")
        self.assertEqual(returncode, 0)
        self.assertEqual(stderr, "")

    def test_list_assignment_is_reference_not_copy(self):
        list_1 = ["History", "Math", "Physics", "CompSci"]
        list_2 = list_1
        list_1[0] = "Art"
        self.assertIs(list_1, list_2)
        self.assertEqual(list_2[0], "Art")

    def test_tuple_reassignment_does_not_affect_original_reference(self):
        tuple_1 = ("History", "Math", "Physics", "CompSci")
        tuple_2 = tuple_1
        tuple_1 = tuple_1 + ("Art",)
        # tuple_2 still points to the original tuple
        self.assertEqual(tuple_2, ("History", "Math", "Physics", "CompSci"))
        self.assertEqual(tuple_1[-1], "Art")

    def test_tuple_item_assignment_raises_type_error(self):
        t = ("a", "b", "c")
        with self.assertRaises(TypeError):
            t[0] = "x"  # tuples are immutable


# ---------------------------------------------------------------------------
# dir.py
# ---------------------------------------------------------------------------

class TestDir(unittest.TestCase):

    def test_runs_without_errors(self):
        # help() writes to stdout; ignore stderr (it may go to stdout too)
        _, _, returncode = run_script("dir.py")
        self.assertEqual(returncode, 0)

    def test_dir_on_string_returns_list(self):
        self.assertIsInstance(dir("Ankit"), list)

    def test_dir_includes_common_string_methods(self):
        methods = dir("Ankit")
        for m in ("lower", "upper", "split", "strip", "replace", "find", "format"):
            self.assertIn(m, methods)


# ---------------------------------------------------------------------------
# main.py  — known bug documented
# ---------------------------------------------------------------------------

class TestMainScript(unittest.TestCase):
    """
    main.py has a bug at line 15: `message = message.c` raises an
    AttributeError at runtime (str has no attribute 'c').

    The tests below:
      1. Confirm the script fails with AttributeError.
      2. Verify the string operations the script *intends* to demonstrate.
    """

    def test_script_fails_due_to_known_bug(self):
        _, stderr, returncode = run_script("main.py", "ankit\nPune\n")
        self.assertNotEqual(returncode, 0, "Expected non-zero exit due to AttributeError")
        self.assertIn("AttributeError", stderr)

    def test_string_length(self):
        self.assertEqual(len("ankit"), 5)
        self.assertEqual(len("Pune"), 4)

    def test_string_slicing(self):
        name = "Tathya"
        self.assertEqual(name[0:5], "Tathy")
        self.assertEqual(name[:5], "Tathy")
        self.assertEqual(name[2:], "thya")

    def test_lowercase_message_construction(self):
        name, city = "Ankit", "Pune"
        msg = (
            "Hello my name is "
            + name.lower()
            + " and I live in "
            + city.lower()
            + ". Nice to meet you!"
        )
        self.assertEqual(msg, "Hello my name is ankit and I live in pune. Nice to meet you!")

    def test_string_count(self):
        msg = "hello my name is ankit and ankit lives here"
        self.assertEqual(msg.count("ankit"), 2)

    def test_string_find(self):
        msg = "hello ankit"
        self.assertEqual(msg.find("ankit"), 6)

    def test_string_replace(self):
        msg = "hello ankit, ankit is here"
        self.assertEqual(msg.replace("ankit", "Tathya"), "hello Tathya, Tathya is here")


if __name__ == "__main__":
    unittest.main(verbosity=2)
