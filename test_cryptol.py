# test_cryptol.py
"""
Tests for CryptoL module.
"""

import unittest
from cryptol import CryptoL

class TestCryptoL(unittest.TestCase):
    """Test cases for CryptoL class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoL()
        self.assertIsInstance(instance, CryptoL)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoL()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
