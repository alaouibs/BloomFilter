# BloomFilter
Implémentation d'une classe BloomFilter 

## Pour commencer

Les modules à installer
```sh
pip3 install bitarray
pip3 install pytest
```

## Exemple d'utilisation  

```python hl_lines="1 3"
>>> from BloomFilter import BloomFilter
>>> f = BloomFilter(128, 3)
>>> "hello" in f
False
>>> f.add("hello")
>>> "hello" in f
True
```