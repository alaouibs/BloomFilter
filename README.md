# BloomFilter
Implémentation d'une classe BloomFilter 

## Pour commencer

```sh
pip3 install -r requirements.txt 
```

## Exemple d'utilisation  

```python hl_lines="1 3"
>>> from BloomFilter import BloomFilter
>>> f = BloomFilter(128, 3)
>>> f.test("hello")
False
>>> f.test("hello")
True
```