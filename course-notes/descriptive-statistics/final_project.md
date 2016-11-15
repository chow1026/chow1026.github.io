<!--
.. title: Descriptive Statistics Final Project - Random Draws of Card Deck
.. slug: final_project
.. date: 2016-11-14 11:39:38 UTC+08:00
.. tags: final-project,
.. category:
.. link:
.. description:
.. type: text
-->

Instead of working on this project on a google sheet files, I decided to write my own python script to simulate the experiments.  

1) Histogram generated shown as below.     
![Original Cards](/images/descriptive-statistics/original52.png)    
Histogram for original card values are negatively skewed (towards right).    


2) Randomly Drawing 3 Cards     
I wrote python scripts with pandas and matplotlib for the rest of the project.  



3) Distribution of Sum of 3 Randomly Drawn Cards     
**30 Samples of Sum of 3 Randomly Drawn Cards**     
![30 Samples of Sum of 3 Randomly Drawn Cards](/images/descriptive-statistics/sample30.png)   

Statistical Description of this sample with n = 30:    
count  30.000000    
mean   19.866667    
std     5.550603    
min     9.000000    
25%    15.000000    
50%    20.000000    
75%    24.000000    
max    30.000000    


**500 Samples of Sum of 3 Randomly Drawn Cards**        
![500 Samples of Sum of 3 Randomly Drawn Cards](/images/descriptive-statistics/sample500.png)

Statistical Description of this sample with n = 500:    
count  500.000000    
mean    19.542000    
std      5.337529    
min      5.000000    
25%     16.000000    
50%     20.000000    
75%     24.000000    
max     30.000000    

4) As sample size increases, the curve gets more normalized (bell-shaped).     


5) Q:  Within what range will you expect approximately 90% of your draw values to fall? What is the approximate probability that you will get a draw value of at least 20? Make sure you justify how you obtained your values.    

To determine the range where 90% of the values fall, I found the closest corresponding z-value to be 1.28.   Therefore, with the following formula, I determined the range for our sample with 30 draws, and sample with 500 draws.   

\\[  
  z = \frac{ x - \mu }{\sigma} \\\\
  x_{30, 90%} = 26.971442   \\\\
  x_{500, 90%} = 26.374   \\\\
\\]  

To draw at least 20 from each of the samples, the corresponding z values are:    

\\[
  z_{30, >20} = \frac{20 - 19.866667}{5.550603} = 0.024021
  \\\\
  z_{500, >20} = \frac{20 - 19.542000}{5.337529} = 0.085807 \\\\
\\]

For sample with sample size 30, at z = 0.024021, the probability is 0.51 (51%).  That means the change of drawing 3 cards with sum greater than 20 from this sample is 49%.      

For sample with sample size 500, at z = 0.024021, the probability is 0.534 (53.4%).  That means the change of drawing 3 cards with sum greater than 20 from this sample is 46.6%.    

Finally, here's a [link to the z-table](http://www.stat.ufl.edu/~athienit/Tables/Ztable.pdf) for reference.  
