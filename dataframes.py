from pydataset import data
import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})
df['passing_english'] = df.english >= 70
print(df['passing_english'].sort_values(ascending = True))
#%%
print([df['passing_english'].sort_values(), df['math'].sort_values()])
#%%
col1 = ['passing_english', 'name']
print(df[col1].sort_values(by=['passing_english', 'name']))
#%%
print(df[['passing_english', 'english']].sort_values(by=['passing_english', 'english']))
#%%
df['overall_grade'] = (df.math + df.english + df.reading) / 3
print(df)
#%%
mpg = data('mpg')
print(mpg.size)
print(mpg.dtypes)
print(mpg.info)
#%%
print(mpg.describe())
#mpg.rename(columns={'cty': 'city', 'hwy': 'highway'},inplace = True)
print(mpg.head())
#%%
print(mpg['city' > 'highway'])
#%%
mpg['mileage_difference'] = (mpg.highway - mpg.city)
print(mpg.head())
print(mpg['mileage_difference'].sort_values(ascending = False).head().nlargest())
#%%
print(mpg[['class', 'highway']].where(mpg['class'] == 'compact').sort_values(by=['highway'], ascending = False).head(1))
print(mpg[['class', 'highway']].where(mpg['class'] == 'compact').sort_values(by=['highway'], ascending = True).head(1))

#%%
mpg['average_mileage'] = (mpg.city + mpg.highway) / 2
print(mpg.head())
#%%
print(mpg[['manufacturer', 'average_mileage']].where(mpg['manufacturer'] == 'dodge').sort_values(by=['average_mileage'], ascending = True).head(1))
print(mpg[['manufacturer', 'average_mileage']].where(mpg['manufacturer'] == 'dodge').sort_values(by=['average_mileage'], ascending = False).head(1))

#%%
mml = data('Mammals')
print(mml.head(5))
print(mml.size)
#%%
print(mml.info())
print(mml.describe())
#%%
print(mml[['weight', 'speed']].sort_values(by=['speed'], ascending = False).head(1))
print((sum(mml['specials']) / (mml['specials'].size)) * 100)
print(mml[['hoppers', 'speed']].where((mml['speed'] > (mml['speed']).median()) & (mml['hoppers'] == True))\
.sort_values(by=['speed'], ascending = False).dropna().count())