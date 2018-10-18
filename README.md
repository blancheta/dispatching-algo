

## Python setup for windows
https://www.python.org/downloads/windows/

## Python crash course
### Run a python file :
```
python dispatching_algo.py
```
### Data structure :
#### Dictionary
```
{'id': '199195070', 'name': 'Gautier Le Hir', 'native_languages': ['French'], 'speaking_languages': ['French', 'English']},
```
- is a dictionary
- A dictonary is a set of key:value pairs
- As key, you can use a string, integer. This value is unique
- As value, you can use any data type : (string, integer, boolean, dictionary )
- A dictionary will not remain ordering
```
mydict = {'key': 'value'}
```

To add an element :
```
member['name'] = 'Gautier Le Hir'
```

To get an element :
```
>> print(member['name'])
'Gautier Le Hir'
```
#### List

- native_languages and speaking_languages are lists

- A list is indexed by a number.
- The first index is 0 and so on.
- You can put any type of data inside a list ex : (string, integer, boolean, dictionary )
- The list will remain ordering

```
mylist = ['French']
```

To add an element :
```
>> mylist.append('English')
>> print(mylist)
['French', 'English]
```

ex :

```
languages = ['French', 'English']
```

- To get the first item, you can use languages[0]
- ... the second one, you can use languages[1]

### The best documentation :
https://docs.python.org/3/
#

## Super buddies to find solutions to your questions :
http://google.com and http://stackoverflow.com

If you meet a problem, for sure someone have already asked for it


#### To filter a list of dictionaries in python
https://stackoverflow.com/questions/29051573/python-filter-list-of-dictionaries-based-on-key-value

#### members_attended is a list of dictionary

```
members_attended = [
    {'id': '892310584', 'name': 'Salomé Tournifier', 'native_languages': ['French'], 'speaking_languages': ['English']},
    {'id': '189195070', 'name': 'Gautier Elrih', 'native_languages': ['French'], 'speaking_languages': ['Spanish']},
    {'id': '244502335', 'name': 'Alexandre Blonchet', 'native_languages': ['English'], 'speaking_languages': ['French']},
    {'id': '549752805', 'name': 'Victor Possignini', 'native_languages': ['Spanish'], 'speaking_languages': ['French', 'Italian']},
]
```

## First step :
- Save Native foreign speakers in a list
- Save Native French speakers in a other one

Who we have tonight as native foreign speakers?
2 foreign members
- 1 Spanish
- 1 English

## Second step : Find french-foreigner pairs

- To French people, who want to speak Spanish ?
- Gautier: me

> One group is created

- To French people, who want to speak English ?
- Salomé: me

> One group is created

####Nobody left, everyone is happy

### GUIDELINE :

- Once someone move to a group, he cannot join an other group at the same time

<!--
#For foreign_member in foreign_members:
#    For french_member in french_members :
#        If foreign_member['native_languages'] in french_member['speaking_languages']:
#            a group is created ( a list )
#            french_member and foreign_member move to a group
#            Now, they are not in initial lists
-->

## Enjoy !