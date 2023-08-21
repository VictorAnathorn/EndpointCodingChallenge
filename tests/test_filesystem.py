import unittest
from src.filesystem import FileSystem
from src.directory import Directory
from unittest.mock import patch
from io import StringIO

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        # Setting up a fresh FileSystem for each test
        self.fs = FileSystem()

    def test_create(self):
        self.fs.execute_command("CREATE fruits")
        self.assertIn("fruits", self.fs.root.children)

    def test_list(self):
        self.fs.execute_command("CREATE fruits")
        self.fs.execute_command("CREATE vegetables")
        self.fs.execute_command("CREATE fruits/apples")

        # Capture printed outputs using patch
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.fs.execute_command("LIST")
            output = mock_stdout.getvalue().splitlines()

        self.assertIn("fruits", output[1])
        self.assertIn("apples", output[2])
        self.assertIn("vegetables", output[3])

    def test_delete(self):
        self.fs.execute_command("CREATE fruits")
        self.fs.execute_command("DELETE fruits")
        self.assertNotIn("fruits", self.fs.root.children)

    def test_move(self):
        self.fs.execute_command("CREATE fruits")
        self.fs.execute_command("CREATE fruits/apples")
        self.fs.execute_command("CREATE basket")
        self.fs.execute_command("MOVE fruits/apples basket")
        self.assertIn("apples", self.fs.root.children["basket"].children)
        self.assertNotIn("apples", self.fs.root.children["fruits"].children)

    def test_find(self):
        self.fs.execute_command("CREATE fruits")
        self.fs.execute_command("CREATE fruits/apples")
        directory = self.fs.root.find(["fruits", "apples"])
        self.assertIsInstance(directory, Directory)
        self.assertEqual(directory.name, "apples")

    def test_add(self):
        self.fs.root.add(["fruits", "apples"])
        self.assertIn("fruits", self.fs.root.children)
        self.assertIn("apples", self.fs.root.children["fruits"].children)

if __name__ == "__main__":
    unittest.main()
