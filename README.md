# BloomFilter
Implémentation d'une classe BloomFilter 

## Pour commencer

Les modules à installer
```sh
pip3 install bitarray
pip3 install pytest
```

## Exemple d'utilisation  

.. code-block:: python

    >>> from pybloom import BloomFilter
    >>> f = BloomFilter(capacity=1000, error_rate=0.001)
    >>> [f.add(x) for x in range(10)]
    [False, False, False, False, False, False, False, False, False, False]
    >>> all([(x in f) for x in range(10)])


```python hl_lines="1 3"
>>> from BloomFilter import BloomFilter
>>> f = BloomFilter(128, 3)
>>> "hello" in f
False
>>> f.add("hello")
>>> "hello" in f
True
```