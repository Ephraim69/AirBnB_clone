#!/usr/bin/python3
"""Unittest module for trhe Basemodel Class."""

from models.base_model import BaseModel
from datetime import datetime
import json
import unittest
import uuid
import time


class TestBaseModel(unittest.TestCase):
    """Test Cases for the BaseModel Class"""

    def test_datetime(self):
        """"Tests if updated_at and created_at are
         the same at initaialization
         """
        date_now = datetime.now()
        b = BaseModel()
        diff = b.updated_at - b.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_id(self):
        """Tests for unique user ids."""
        ls = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(ls)), len(ls))

    def test_save(self):
        """Tests the public instance save method"""
        b = BaseModel()
        time.sleep(0.5)
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_3_str(self):
        """Tests for __str__ method."""
        b = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_3_to_dict(self):
        """Tests the public instance method to_dict()."""

        b = BaseModel()
        b.name = "Laura"
        b.age = 23
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["name"], b.name)
        self.assertEqual(d["age"], b.age)
