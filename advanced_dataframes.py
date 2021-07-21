#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
os.getcwd() # Check current directory's path
os.chdir('/Users/mcrob99/codeup-data-science/numpy-pandas-visualization-exercises')
import numpy as np
import pandas as pd
from env import host, user, password
from pydataset import data
def get_db_url(host = host, user = user, password = password, db = 'employees'):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#%%
sql = '''
SELECT
    emp_no,
    first_name,
    last_name
FROM employees
WHERE gender = 'F'
LIMIT 100
'''

employees = pd.read_sql(sql, get_db_url())
print(employees.describe())
#%%
sql2 = '''
SELECT DISTINCT 
    to_date,
    title
FROM titles
'''

titles = pd.read_sql(sql2, get_db_url())
print(titles.min())
print(titles.max())
#%%
print(titles.head(100).describe())
#%%
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
#%%
print(users.drop('role_id', 1).merge(roles))
#%%
mpg_doc = data('mpg', show_doc = True)
mpg = data('mpg')
print(mpg)
#%%
mpg.rename(columns={'cty': 'city', 'hwy': 'highway'}, inplace = True)
print(mpg['manufacturer'].unique().size)
print(mpg)
#%%
print(mpg['model'].unique().size)
#%%
mpg['average_mileage'] = (mpg.city + mpg.highway) / 2
print(mpg[['average_mileage', 'city', 'highway']])
#%%
mpg['is_automatic'] = (mpg['trans'].str.startswith('auto') == True)
print(mpg.sort_values(by='is_automatic', ascending = False))
#%%
print(mpg.sort_values(by='average_mileage', ascending = False).groupby('manufacturer').agg([min]))
#%%
sql3 = '''
SELECT
    item_price