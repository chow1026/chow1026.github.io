<!--
.. title: Inferential Statistics - Regressions
.. slug: lesson-15
.. date: 2016-11-08 15:00:58 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

##Linear Regressions     
Line of best fit forms a line to help us:    
- describe data    
- make predictions     

**Observed Y vs Expected Y**     
**Expected Y** \\( \hat{y} \\) are the ones calculated/predicted based on the best fit regression line.    
**Observed Y** \\( y \\) are collected data or real-life data.    
**Residual** is the difference between Observed value and Expected value.  

A few ways to find the line of best fit:    
- Find a line to minimize the sum of residuals.   The problem with this approach is sometimes, negative and positive residuals cancel each other out.       
- Find a line that minimize the sum of **absolute** residuals.    
- Find a line that minimize the sum of squared residuals, \\( \sum{(y - \hat{y})} \\)

When we use calculus to determine the slope, b:  
\\[
  b = \frac{\sum{(y_i - \bar{y})(x_i - \bar{x})}}{\sum{(x_i - \bar{x})^2}} \\\\
  = r (\frac{S_y}{S_x}) \\\\
  \text{where } r \text{ is Pearson's Correlation Coefficient and }\\\\
   S \text{ are standard deviations of } x \text{ and } y.
\\]

We have decided to symbolize the regression line by y = bx + a, where b represents the slope and a represents the y-intercept.
Since \\( b = r(\frac{S_y}{S_x}) \\), we can also symbolize the regression line like this:    
\\[ y = r(\frac{S_y}{S_x})x + a \\]

**Pearson's Correlation Coefficient \\( r \\)**    
A high \\(r\\) value indicates a strong correlation. This could contribute to high \\(r^2 \\) value, which indicates the percentage of differences in Y is due to differences in X.  

**Standard Error of Estimates**    
Standard error of estimates:   
\\[
SE = \sqrt{ \frac{\sum (y - \hat{y})^2}{N-2}}
\\]

**Factors that Affect the Regressions**   
- outliers affect the value of r, correlation Coefficient
- outliers also affect the linear regression line
-
