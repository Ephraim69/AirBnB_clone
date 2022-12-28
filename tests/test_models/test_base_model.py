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

