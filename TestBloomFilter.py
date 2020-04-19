from __future__ import absolute_import

from BloomFilter import BloomFilter, BloomFilterEvolution
try:
    import StringIO
    import cStringIO
except ImportError:
    pass

import io

import unittest
import random
import tempfile

from bitarray import bitarray 


class TestBloomFilter(unittest.TestCase):
    def test_bloom_creation(self):
        k = 3
        m = 128
        bits = bitarray(m) 
        bits.setall(0) 
        bloom = BloomFilter(m, k)
        self.assertEqual(bloom.k, k)
        self.assertEqual(bloom.size, m)
        self.assertEqual(bloom.bits, bits)
        self.assertEqual(len(bloom.hashFunctions), k)

    def test_bloom_creation_fail(self):
        def _run():
            BloomFilter(128, 4)
        self.assertRaises(Exception, _run)

    def test_hash_indexes(self):
        k = 3
        m = 128
        bloom = BloomFilter(m, k)
        hash_indexes = bloom.hash_indexes('#')
        self.assertEqual(len(hash_indexes), 3)
        for index in hash_indexes:
            self.assertIn(index, range(0, m))
        
    def test_add(self):
        k = 3
        m = 128
        bloom = BloomFilter(m, k)
        bloom.add("#")
        self.assertIn(bloom.bits.count(), range(1, 4))

    def test_contain(self):
        k = 3
        m = 128
        bloom = BloomFilter(m, k)
        self.assertFalse(bloom.test('#'))
        bloom.add("#")
        self.assertTrue(bloom.test('#'))

class TestBloomFilterEvolution(unittest.TestCase):
    def test_bloomEvolution_creation(self):
        m = 128
        capacity = 20
        bits = bitarray(m) 
        bits.setall(0) 
        bloom = BloomFilterEvolution(m, capacity)
        self.assertEqual(bloom.size, m)
        self.assertEqual(bloom.capacity, capacity)
        self.assertEqual(bloom.bits, bits)

    def test_get_hash_count(self):
        bloom1 = BloomFilterEvolution(128, 20)
        bloom2 = BloomFilterEvolution(128, 80)

        self.assertEqual(bloom1.k, 3)
        self.assertEqual(bloom2.k, 1)
if __name__ == '__main__':
    unittest.main()