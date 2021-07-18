import numpy as np
import pandas as pd
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
print(fruits.str.capitalize())
print(fruits.str.count('a'))
print(fruits.str.lower().str.count(r'[aeiou]'))
#%%
max_len = fruits.apply(lambda x: len(x)).max()
print(fruits.where(fruits.str.len() == max_len).sort_values(ascending = True).head(1))
print(fruits.where(fruits.str.len() >= 5).sort_values(ascending = True).head(13))
#%%
double_o = fruits.apply(lambda x: x.count('o') >= 2)
print(fruits[double_o == True])
#%%
vowel_count = fruits.str.lower().str.count(r"[aeiou]")
print(fruits[vowel_count == max(vowel_count)])