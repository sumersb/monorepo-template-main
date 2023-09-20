from jsonapi import *
import unittest


class TestJsonAPI(unittest.TestCase):

    def test_dumps(self):
        self.assertEqual(dumps(complex(1, 2)),
                         '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'
                         )

        self.assertEqual(dumps(range(1, 99, -1)),
                         '{"start": 1, "stop": 99, "step": -1, "__extended_json_type__": "range"}'
                         )
        self.assertEqual(dumps({"name": "Alice", "age": complex(1, 2), "city": "Anytown"}),
                         '{"name": "Alice", "age": {"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}, "city": "Anytown"}')

    def test_loads(self):
        self.assertEqual(loads('{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'),
                         complex(1, 2)
                         )

        self.assertEqual(loads('{"start": 1, "stop": 99, "step": -1, "__extended_json_type__": "range"}'),
                         range(1, 99, -1)
                         )

        self.assertEqual(loads('{"name": "Alice", "age": {"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}, "city": "Anytown"}'),
                         {"name": "Alice", "age": complex(1, 2), "city": "Anytown"})


if __name__ == '__main__':
    unittest.main()
