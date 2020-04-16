from BloomFilter import BloomFilter, BloomFilterEvolution
from random import shuffle 
  
m = 128 
k = 3

bloomf = BloomFilter(m,k) 
  
# words to be added 
word_present = ['abound','abounds','abundance','abundant','accessable', 
                'bloom','blossom','bolster','bonny','bonus','bonuses', 
                'coherent','cohesive','colorful','comely','comfort', 
                'gems','generosity','generous','generously','genial'] 
  
# word not added 
word_absent = ['bluff','cheater','hate','war','humanity', 
               'racism','hurt','nuke','gloomy','facebook', 
               'geeksforgeeks','twitter'] 
  
for item in word_present: 
    bloomf.add(item) 

shuffle(word_present) 
shuffle(word_absent) 

test_words = word_present[:10] + word_absent 

for word in test_words: 
    if word in bloomf: 
        if word in word_absent: 
            print("'{}' est un faux positif !".format(word)) 
        else: 
            print("'{}' est probablement présent !".format(word)) 
    else: 
        print("'{}' n'est définitivement pas présent !".format(word)) 
        assert word in word_absent
        assert word not in word_present
print('\n')

bloom1 = BloomFilterEvolution(128, 20)
bloom2 = BloomFilterEvolution(128, 80)

print(str(bloom1.k) + " algorithmes de hachage sont nécessaires pour minimiser les chances de collisions si l'on insère 20 éléments dans un tableau de 128 cases")
print(str(bloom2.k) + " algorithmes de hachage sont nécessaires pour minimiser les chances de collisions si l'on insère 20 éléments dans un tableau de 128 cases")