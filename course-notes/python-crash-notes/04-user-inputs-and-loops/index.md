<!--
.. title: User Input and Loops
.. slug: 04-user-inputs-and-loops
.. date: 2016-08-30 15:00:52 UTC+08:00
.. tags: python-crash-course, loops, user-input
.. category:
.. link:
.. description:
.. type: text
-->
## User Input ##
- usr_input = input("Tell me XXX") // get user input as string

## Loops ##
### For Loop ###
- ``` for x in {list_name}:``` // loop through list_name list
- ``` for x in range(1, 10): ``` //  loop from 1 through 9, but NOT 10
- ``` for ky, val in {dictionary}.items():``` // loop through key value pair in dictionary

### While Loop ###
- ``` while {list_name}: ``` // loop as long as list isn't empty
```python
      i = 0
      while i < 5:
        // do something
        i += 1
```

### Breaking Loop ###
- To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.  
```python
      i = 0
      while True:
        if x == {some condition}:
          break
        else:
          // do something
```

### Skip but Continue Looping ###
- Rather than breaking out of a loop entirely without executing the rest of its code, use the continue statement to go back to the loop
```python
      i = 0
      while i < 10:
        i += 1
        if i % 2 == 0:
          continue
        print(i)
```
