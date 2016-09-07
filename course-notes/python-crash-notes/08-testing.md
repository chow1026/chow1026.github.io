<!--
.. title: Testing Python Code
.. slug: 08-testing
.. date: 2016-09-07 16:55:02 UTC+08:00
.. tags: python-crash-course, testing, unit-test, test-cases, setUp()-method
.. category:
.. link:
.. description:
.. type: text
-->

## Testing a Function ##
- name_function.py
```python
  def get_formatted_name(first, last):
    """ Generated a Neatly formatted full name """
    full_name = first + ' ' + last
    return full_name.title()
```
- names.py
```python
  from name_function import get_formatted_name

  print("Enter 'q' to quit any time.")
  while True:
    first = input("\nFirst Name: ")
    if first == 'q':
      break
    last = input("\nLast Name: ")
    if last == 'q':
      break
    formatted_name = get_formatted_name(fist, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
```

### Unit Tests and Test Cases ###
- A _unit test_ verifies that one specific aspect of a function's behavior is correct.  
- A _test case_ is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations it is expected to handle.  
- A test case with _full coverage_ includes a full range of unit tests covering all the possible ways you can use a function.  Achieving full coverage on a large project can be daunting.  Aim for full coverage only if project starts to see widespread use.  
- test_name_function.py (an example test case for name_function.py)
```python
  import unittest
  from name_function import get_formatted_name

  class NamesTestCase(unittest.TestCase):
    """ Test for 'name_function.py' """

    def test_first_last_name(self):
      """ Do names like 'Janis Joplin' work? """
      formatted_name = get_formatted_name('janis', 'joplin')
      self.assertEqual(formatted_name, 'Janis Joplin')

  unittest.main() # tells python to run the test.
```
- ``` python3 test_name_function.py ``` in CLI to run.  For now, test will pass.  
- name_function.py (modified)
```python
  def get_formatted_name(first, middle, last):
    """ Generated a Neatly formatted full name """
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
```
- ``` python3 test_name_function.py ``` will raise error.
- name_function.py (modified again, to make `middle` optional)
```python
  def get_formatted_name(first, last, middle=''):
    """ Generated a Neatly formatted full name """
    if middle:
      full_name = first + ' ' + middle + ' ' + last
    else:
      full_name = first + ' ' + last
    return full_name.title()
```
- ``` python3 test_name_function.py ``` will pass again.
- test_name_function.py (Add new test to test both cases)
```python
  import unittest
  from name_function import get_formatted_name

  class NamesTestCase(unittest.TestCase):
    """ Test for 'name_function.py' """

    def test_first_last_name(self):
      """ Do names like 'Janis Joplin' work? """
      formatted_name = get_formatted_name('janis', 'joplin')
      self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
      """ Do names like 'Wolfgang Amadeus Mozart' work? """
      formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
      self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

  unittest.main() # tells python to run the test.
```

### A Variety of Assert Methods ###
- assertEqual(a, b) :: Verify if a == b
- assertNotEqual(a, b) :: Verify if a != b
- assertTrue(x) :: Verify if x is True
- assertFalse(x) :: Verify if x is False
- assertIn(_item_, _list_) :: Verify that _item_ is in _list_
- assertNotIn(_item_, _list_) :: Verify that _item_ is NOT in _list_

### Testing a Class ###
- survey.py
```python
  class AnonymousSurvey():
    """ Collect anonymous answers to a survey question. """

    def __init__(self, question):
      """ Store a question, prepare to store responses. """
      self.question =  question
      self.responses = []

    def show_question(self):
      """ Show the survey question """
      print(question)

    def store_response(self, new_response):
      """ Store a single response to the survey. """
      self.responses.append(new_response)

    def show_results(self):
      """ Show all responses that had been given """
      print("Survey results:")
      for response in responses:
        print('- ' + response)
```
- lang_survey.py
```python
  from survey import AnonymousSurvey

  question = "What language did you first learn to speak? " # define question
  survey = AnonymousSurvey(question) # instantiate a survey

  survey.show_question() # show question
  print("Enter 'q' any time to quit. \n")
  while True:
    response = input("Language: ")
    if response == 'q':
      break
    survey.store_response(response)

  print("\nThank you for your participation. ")
  survey.show_results()
```
- test_survey.py (test case for survey.py)
```python
  import unittest
  from survey import AnonymousSurvey

  class TestAnonymousSurvey(unittest.TestCase):
    """ Test Case for class AnonymousSurvey """

    def test_store_single_response(self):
      """ Test that a single response is stored properly """
      question = "What language did you first learn to speak? " # define question
      survey = AnonymousSurvey(question) # instantiate a survey
      survey.store_response('English')

      self.assertIn('English', survey.responses)

    def test_store_three_responses(self):
      """ Test that a single response is stored properly """
      question = "What language did you first learn to speak? " # define question
      survey = AnonymousSurvey(question) # instantiate a survey
      responses = ['English', 'Spanish', 'Mandarin']
      for resp in responses:
        survey.store_response(resp)

      for resp in responses:
        self.assertIn(resp, survey.responses)
```

### The setUp() Method ###
- As shown in the previous test_survey.py, we define question, create new instance of survey and new responses in each test methods.  The unittest.TestCase class has a setUp() method that allows you to reate these objects once and then use them in each of your test methods.  When a setUp() method is included, Python runs the setUp() method before running each method starting with _test__.  Any objects created in the setUp() method will be available in each test method you write.  
- test_survey.py (refactored with setUp() method)
```python
  import unittest
  from survey import AnonymousSurvey

  class TestAnonymousSurvey(unittest.TestCase):
    """ Test Case for class AnonymousSurvey """

    def setUp(self):
      """ Define question, create survey and a set of responses to be used in all test methods """
      question = "What language did you first learn to speak? " # define question
      self.survey = AnonymousSurvey(question) # instantiate a survey
      self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
      """ Test that a single response is stored properly """
      self.survey.store_response('English')
      self.assertIn('English', survey.responses)

    def test_store_three_responses(self):
      """ Test that a single response is stored properly """
      for resp in responses:
        self.survey.store_response(resp)
      for resp in responses:
        self.assertIn(resp, survey.responses)
```
