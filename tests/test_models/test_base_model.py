#!/usr/bin/python3

import unittest
import pep8
import json
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Check documentation"""
    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """Check for method documentation"""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


class TestBaseModelPep8(unittest.TestCase):
    """Check pep8 validation"""
    def test_pep8(self):
        """Test for pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """Set up instances for tests"""
        cls.basemodel = BaseModel()

    def test_id(self):
        """Test id class member"""
        self.assertEqual(str, type(self.basemodel.id))

    def test_created_at(self):
        """Test created_at class method"""
        self.assertEqual(datetime, type(self.basemodel.created_at))

    def test_updated_at(self):
        """Test updated_at class method"""
        self.assertEqual(datetime, type(self.basemodel.updated_at))

    def test_to_dict(self):
        """Test to_dict class method"""
        new_dict = self.basemodel.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.basemodel))

    @classmethod
    def tearDownClass(cls):
        """Remove test instances"""
        pass
