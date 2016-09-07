<!--
.. title: Lists and Tuples and Dictionaries
.. slug: 03-lists-and-tuples-and-dictionaries
.. date: 2016-08-30 14:29:09 UTC+08:00
.. tags: python-crash-course, lists, tuples
.. category:
.. link:
.. description:
.. type: text
-->

## Lists ##
- Lists are mutable.  Lists can be modified throughout the life of a programme.
- Accessing Element in a List
    - ```bicycles[0]```, ```bicycles[-1]```, ```bicycles[3]```
- Adding Elements to a List
    - ```motorcycles.append('ducati')``` // Add to end of the list
    - ```motorcycles.insert(0, 'ducati')``` // Insert 'ducati' at position 0
- Removing Element from a List
    - ```del motorcycles[1]``` // remove element by index
    - ```last_owned = motorcycles.pop()``` // remove last element in motorcycles list and store as last_owned
    - ```most_expensive = motorcycles.pop(2)``` // remove third element in motorcycles list and store as most_expensive
    - ```motorcycles.remove('yamaha')``` // remove element by value
- Organizing a List
    - ```cars.sort()``` // sorting permanently
    - ```cars.sort(reverse=True)``` // sorting in reverse order, permanently
    - ```sorted(cars)``` // temporarily sort a list
    - ```cars.reverse()``` //simply reverse the order of the list
  - Length of a List
    - ```len(cars)``` // returns integer of element count in the list
- Copying a List
    - ```b = a[:]``` // b copies a, and is separate list from a
- Aliasing a List
    - ```q = p``` // q and p refers to same list object.
- Looping through lists:
    - ``` for x in {list_name}:```
    - ``` for x in range(1, 10): ```


## Tuples ##
- Just like strings, tuples is IMMUTABLE.
- Values of Tuples can be reassigned, or overwritten.  
    - ```tup = ('alice', 'not in', 'wonderland')```
    - ```tup = ('alice', 'now in', 'wonderland') ``` //final value will be the last assigned value.
- Tuples can be looped just like lists.


## Dictionaries ##
- Elements in dictionaries are stored in key-value pairs.
- Value is assessed by key.
- Looping through dictionaries:
    - ``` for x, y in dict.items():``` // looping through x, y {key-value} pairs in dict
    - ``` for ky in dict.keys():``` // looping through all keys of dict dictionary
    - ``` for val in dict.values():``` // looping through all values of dict dictionary
    - ``` set(dict.values()) ``` // build a set by selecting unique items from dict.values()
