# Python 3 program to build Bloom Filter 
import math 
import hashlib 
from bitarray import bitarray 

from random import Random

class BloomFilter(object): 
    ''' 
    Class for Bloom filter, using SHA-1, SHA-256 et SHA-512 hash functions from hashlib module
    '''
    def __init__(self, size, k):
        ''' 
        size : int 
            bit array size
        k : int 
            number of hash functions to use 
        '''
        if k > 3 or k < 1:
            raise Exception('Must specify value of k between 1 and 3')
        self.k = k
        self.size = size
        self.bits = bitarray(self.size) 
        self.bits.setall(0) 
        self.hashFunctions = [hashlib.sha1, hashlib.sha256, hashlib.sha512]

    def hash_indexes(self,item):
        ''' 
        execute hash functions for an item and return an array of indexes
        '''
        ret = []
        for i in range(self.k):
            ret.append(int(self.hashFunctions[i](item.encode("utf-8")).hexdigest(), 16) % self.size)
        return ret

    def add(self, item):
        ''' 
        Add an item in the filter 
        '''
        dupe = True
        for i in self.hash_indexes(item):
            if dupe and not self.bits[i]:
                dupe = False
            self.bits[i] = True
        return dupe

    def test(self, item):
        ''' 
        Check for existence of an item in filter 
        '''
        for i in self.hash_indexes(item):
            if not self.bits[i]:
                # if any of bit is False then,its not present in filter 
                # else there is probability that it exist 
                return False
        return True

class BloomFilterEvolution(BloomFilter):
    ''' 
    Class BloomFilterEvolution inherited from BloomFilter, using SHA-1, SHA-256 et SHA-512 hash functions from hashlib module
    the number of hash functions is calculated in order to minimize the number of collisions
    '''
    def __init__(self, size, capacity):
        ''' 
        size : int 
            bit array size
        capacity : int 
            number of items expected to be stored in bloom filter 
        '''
        BloomFilter.__init__(self, size, 3)
        self.capacity = capacity
        self.k = self.get_hash_count(size, capacity)

    @classmethod
    def get_hash_count(self, size, capacity): 
        ''' 
        Return the hash function(k) to be used using 
        following formula 
        k = (m/n) * lg(2) 
  
        size : int 
            size of bit array 
        capacity : int 
            number of items expected to be stored in filter 
        '''
        k = min(int((size/capacity) * math.log(2)), 3)
        return k

