import numpy as np
import pandas as pd
import matplotlib.pyplot as matplt

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
print(letters.value_counts().nlargest(n=1, keep="all"))
print(letters.value_counts().nsmallest(n=1, keep="all"))
#%%
def total_vowels(lis):
    count = 0
    for i in lis:
        if i in 'aeiou':
            count = count + 1
    return count

letter_vowels = (letters.apply(total_vowels)).sum()
print(letter_vowels)
print(letters.size - letter_vowels)
print(letters.str.upper())
#%%

top_6 = letters.value_counts().nlargest(n=6, keep='all')
top_6.plot.bar()
#%%
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

print(type(numbers))
print(numbers.size)
numbers_float = numbers.str.replace("$", "").str.replace(",", "").astype(float)
print(numbers_float)
#%%
print(numbers_float.nlargest(n=1, keep="all").values[0])
print(numbers_float.nsmallest(n=1, keep="all").values[0])
print(str(numbers_float.nsmallest(n=1, keep="all").values[0]) + "-" + str(numbers_float.nlargest(n=1, keep="all").values[0]))
#%%
binned = pd.cut(numbers_float, 4, labels=["0 - 1.9M", "1.9M - 2.39M", "2.39 - 3.59",  "3.59M - 4.78M"]).value_counts()
matplt.clf()

binned.plot.bar()

matplt.title('My Binned Data')
matplt.ylabel('Frequency')
matplt.xticks(rotation=0)
matplt.xlabel('Ranged Values')
matplt.show()