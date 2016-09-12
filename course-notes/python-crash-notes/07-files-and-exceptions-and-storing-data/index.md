<!--
.. title: Files and Exceptions and Storing Data
.. slug: 07-files-and-exceptions-and-storing-data
.. date: 2016-09-07 15:05:56 UTC+08:00
.. tags: python-crash-course, files, exceptions, storing-data
.. category:
.. link:
.. description:
.. type: text
-->

## Files ##
### Filepath ###
- A _relative path_ is a to look for a given location relative to the directory where the currently running program file is stored.  
- An _absolute path_ is exactly the file location on your computer, regardless of where the program being executed is stored.  
- ``` os.getcwd ``` returns current working directory.  Remember to ```import os```.

### Reading an Entire File ###
- pi_digits.txt
```
3.1415926535
  8979323846
  2643383279
```
- file_reader.py
```python
  with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```
- output:
```
3.1415926535
  8979323846
  2643383279

```
- Note that output has an extra blank line, because read() returns an empty string when it reaches the end of the file.  To remove the extra blank line, use rstrip().  --> ```print(contents.rstrip())```

### Reading a File Line by Line ###
- file_reader.py
```python
  filename = 'pi_digits.txt'
  with open(filename) as file_object:
    for line in file_object:
      print(line.rstrip()) # rstrip() removes the blank lines from .read()
```

### Making a List of Lines from a File ###
- file_reader.py
```python
  filename = 'pi_digits.txt'
  with open(filename) as file_object:
    lines = file_object.readlines()

  for line in lines:
    print(line.rstrip()) # rstrip() removes the blank lines from .read()
```

### Working with a File's Contents ###
- file_reader.py
```python
  filename = 'pi_digits.txt'
  with open(filename) as file_object:
    lines = file_object.readlines()

  pi_string = ''
  for line in lines:
    pi_string += line.rstrip() # rstrip() removes the blank lines from .read()

  print(pi_string) # prints 3.1415926535  8979323846  2643383279
  print(len(pi_string)) # prints 36 due to blank spaces for 2nd and 3rd lines

  for line in lines:
    pi_string += line.strip() # strip all blank spaces and lines

  print(pi_string) # prints 3.141592653589793238462643383279
  print(len(pi_string)) # prints 32 due to blank spaces for 2nd and 3rd lines

```

### Writing to a File ###
- write_message.py
```python
  filename = 'writing.txt'
  with open(filename, 'w') as file_object: # 'w' denote writing mode
    file_object.write("I test writing.")
    file_object.write("I test writing second line.")

  # Both these sentences will be written in one /same line.  
```
- Insert line break.  
```python
  filename = 'writing.txt'
  with open(filename, 'w') as file_object: # 'w' denote writing mode
    file_object.write("I test writing. \n")
    file_object.write("I test writing second line. \n")

  # Both these sentences will be written in separate line.  
```

### Appending to a File ###
- write_message.py
```python
  filename = 'writing.txt'
  with open(filename, 'a') as file_object: # 'a' denotes append
    file_object.write("I test writing more.")
    file_object.write("I test writing the last line.")

  # Both these sentences will be appended to previous file content.  
```

## Exceptions ##
- Python uses exceptions to manage errors that arise during a program's execution.  It is advisable to write code that handles exceptions properly so the program continues running.  If not, the program will halt and show a _traceback_, which includes a report of the exception that was raised.
- A couple of common Python exceptions are ZeroDivisionError and FileNotFound exceptions.

### try-except-else block ###
- division.py (example of try-except block)
```python
  print("Give me two numbers, I will divide them.")
  print("Enter 'q' to quit.")

  while True:
    first_num = input("\nFirst Number: ")
    if first_num == 'q':
      break
    sec_num = input("\nSecond Number: ")
    if sec_num == 'q':
      break

    try:
      answer = int(first_num) / int(sec_num)
    except ZeroDivisionError:
      print("You can't divide by 0!")
    else: # proceed if no ZeroDivisionError exception
      print answer
```
- alice.py (example of handling FileNotFound exception)
```python
  filename = 'alice.txt'

  try:
    with open(filename) as fobj:
      contents = fobj.read()
  except FileNotFoundError:
    msg = "Sorry, the file " + filename + " doesn't exist. "
    print(msg)
  else:
    words = contents.split()
    word_count = len(words)
    print("The file " + filename + " has about " + str(word_count) + " words.")
```
- word_count.py (example of working with multiple files)
```python
  def count_words(filename):
    """ Count the approximate number of words in a file """
    try:
      with open(filename) as fobj:
        contents = fobj.read()
    except FileNotFoundError:
      msg = "Sorry, the file " + filename + " doesn't exist. "
      print(msg)
    else:
      words = contents.split()
      word_count = len(words)
      print("The file " + filename + " has about " + str(word_count) + " words.")

  filename = 'alice.txt'
  count_words(filename)

  filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
  for filename in filenames:
    count_words(filename)
```

### Failing silently ###
- word_count.py
```python
  def count_words(filename):
    """ Count the approximate number of words in a file """
    try:
      with open(filename) as fobj:
        contents = fobj.read()
    except FileNotFoundError:
      pass # pass is used to silent the error.  Often times used as a placeholder as well.
    else:
      words = contents.split()
      word_count = len(words)
      print("The file " + filename + " has about " + str(word_count) + " words.")

  filename = 'alice.txt'
  count_words(filename)

  filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
  for filename in filenames:
    count_words(filename)
```

## Storing Data ##
### json.dump() and json.load() ###
- num_write.py
```python
  import json

  nums = [2, 3, 5, 7, 11, 13]
  filename = 'prime.json'
  with open(filename, 'w') as fobj:
    json.dump(nums, fobj)
```
- num_read.py
```python
  import json

  filename = 'prime.json'
  with open(filename) as fobj:
    primes = json.load(fobj)

  print(primes)
```
