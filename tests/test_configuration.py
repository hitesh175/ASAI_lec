import contextlib
import importlib.util
import io
import os
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("configuration_example", Path(__file__).parents[1] / "Python_exam.py")
example = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example)


class ConfigurationTests(unittest.TestCase):
    def test_success_does_not_disclose_values(self):
        output = io.StringIO()
        with patch.object(example, "load_dotenv"), patch.dict(os.environ, {"MAIN_KEY": "private-one", "SECRET_KEY": "private-two"}, clear=True), contextlib.redirect_stdout(output):
            self.assertEqual(example.main(), 0)
        self.assertNotIn("private-one", output.getvalue())
        self.assertNotIn("private-two", output.getvalue())

    def test_missing_keys_have_failure_status(self):
        output = io.StringIO()
        with patch.object(example, "load_dotenv"), patch.dict(os.environ, {}, clear=True), contextlib.redirect_stdout(output):
            self.assertEqual(example.main(), 1)
        self.assertIn("MAIN_KEY", output.getvalue())
        self.assertIn("SECRET_KEY", output.getvalue())


if __name__ == "__main__":
    unittest.main()
