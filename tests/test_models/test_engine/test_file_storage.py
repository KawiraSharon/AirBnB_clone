#!/usr/bin/python3

import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorageDocs(unittest.TestCase):
    """Check documentation"""
    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(FileStorage.__doc__) > 0)


class TestFileStoragePep8(unittest.TestCase):
    """Check for pep8 validation"""
    def test_pep8(self):
        """Test for pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestFileStorage(unittest.TestCase):
    """Test for class FileStorage"""
    @classmethod
    def setUpClass(cls):
        """Set up instances for testing"""
        storage = FileStorage()

    def test_all(self):
        """Test the all method"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Remove test instances"""
        pass
