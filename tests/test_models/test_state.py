#!/usr/bin/python3
"""Class State tests"""
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class Test_State(unittest.TestCase):
    """Class State Verifying"""

    model = State()

    def test_instance(self):
        """Test Is Instance"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model, State)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_attributes(self):
        """Verifying has attribute"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "__init__"))

    def test_attributes_a(self):
        """Verifying has attribute"""
        self.assertTrue(hasattr(self.model, "name"))

    def test_attribute_type(self):
        """Verifying Type of attr"""
        self.assertIsInstance(self.model.name, str)

    def test_addattr(self):
        """Verifying add attribute"""
        self.model.some = "some"
        self.assertTrue(hasattr(self.model, "some"))


if __name__ == "__main__":
    unittest.main()
