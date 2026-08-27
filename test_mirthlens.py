# test_mirthlens.py
"""
Tests for MirthLens module.
"""

import unittest
from mirthlens import MirthLens

class TestMirthLens(unittest.TestCase):
    """Test cases for MirthLens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MirthLens()
        self.assertIsInstance(instance, MirthLens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MirthLens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
