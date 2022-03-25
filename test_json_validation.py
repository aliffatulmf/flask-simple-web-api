import unittest
from lib.validation import jsonvalidator


class TestJsonValidation(unittest.TestCase):

    def setUp(self):
        self.schema = {
            "type": "object",
            "properties": {
                "code": {
                    "type": "number"
                },
                "name": {
                    "type": "string"
                }
            }
        }

    def test_json_validator_true(self):
        t = {"code": 1, "name": "Lee"}
        j = jsonvalidator(self.schema, t)

        self.assertTrue(j)

    def test_json_validator_false(self):
        t = {"code": "1", "name": "Lee"}
        j = jsonvalidator(self.schema, t)

        self.assertFalse(j)


if __name__ == "__main__":
    unittest.main()
