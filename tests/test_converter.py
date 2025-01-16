import unittest
from ships.converter import convert_webpage_to_ascii


class TestWeb2Ascii(unittest.TestCase):
    def test_valid_url(self):
        url = "https://example.com"
        result = convert_webpage_to_ascii(url)
        self.assertIn("Example Domain", result)

    def test_invalid_url(self):
        url = "https://nonexistenturl.example"
        with self.assertRaises(RuntimeError):
            convert_webpage_to_ascii(url)


if __name__ == "__main__":
    unittest.main()
