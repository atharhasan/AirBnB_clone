#!/usr/bin/env python3
"""Verifying Class Review"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class Test_Review(unittest.TestCase):
    """Verifying Class Review"""

    model = Review()

    def test_inhertance(self):
        """Verifying Is Instance"""
        self.assertIsInstance(self.model, Review)
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_attributes(self):
        """Verifying has attrinutes"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "__init__"))

    def test_attribute_a(self):
        """Verifying has attribute"""
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))

    def test_attribute_type(self):
        """Verifying Type of Attributes"""
        self.assertIsInstance(self.model.place_id, str)
        self.assertIsInstance(self.model.user_id, str)
        self.assertIsInstance(self.model.text, str)

    def test_addattr(self):
        """Verifying add attribute"""
        self.model.some = "some"
        self.assertTrue(hasattr(self.model, "some"))


if __name__ == "__main__":
    unittest.main()
