import unittest
from src.directory import Directory
from unittest.mock import patch
from io import StringIO

class TestDirectory(unittest.TestCase):
       
    def test_directory_delete(self):
        dir = Directory("fruits")
        dir.add(["apples"])
        dir.delete(["apples"])
        self.assertNotIn("apples", dir.children)

    def test_directory_move(self):
        src = Directory("fruits")
        src.add(["apples"])
        dest = Directory("basket")
        src.move(["apples"], dest)
        self.assertIn("apples", dest.children)
        self.assertNotIn("apples", src.children)

    def test_directory_list(self):
        dir = Directory("fruits")
        dir.add(["apples"])
        # Capture printed outputs using patch
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            dir.list()
            output = mock_stdout.getvalue().splitlines()
        self.assertIn("fruits", output[0])
        self.assertIn("apples", output[1])

if __name__ == '__main__':
    unittest.main()