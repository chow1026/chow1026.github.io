<!--
.. title: Overview of A/B Testing
.. slug: lesson1-overview
.. date: 2017-05-08 13:37:59 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## What is AB Testing:
AB Testing is general methodology used online when one wants to test a new product or feature.  


### Example Business Use Case:
Experiment the user's steps on Audacity, explore the customer funnel.  Experiment changing the color of a "Start Now" button from Orange to Pink.  See if the change has any impact on how many student explore  Audacity's courses.  

Therefore, Our initial hypothesis 0: Changing the "Start Now" button _from Orange to Pink_ will increase the number of student exploring the Audacity courses.  

#### Metrics:
What audacity ultimately cares about is: How many total number of students actually complete the courses:

Common Metrics
- Total Number of Courses Completed  (Takes long time to complete course, too long for experiment and for practical business feedback)
- Total number of Clicks (However this doesn't reflect the proportion of it to total visit)
- Click Through Rate [the number of clicks/number of page views] (this is slightly better button doesn't account for users who just visited without clicks, or users who clicks multiple times)
- Click Through Probability [unique visitors who clicks/unique visitors who visits] (This is the best for this use case)

Generally we use "rate" when we want to measure the usability, whereas when we want to measure the total impact we use the "probability".  "Rate" measures usability of a button, ie. how often a user finds and clicks a button when placed on a site (with other buttons and links); ""

Now, our upgraded hypothesis:
Changing the "Start Now" button from _Orange to Pink_ will **increase the click-through probability** of the button.  

### Estimating Click-Through Probability
