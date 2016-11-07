<!--
.. title: Inferential Statistics - Correlations
.. slug: lesson-14
.. date: 2016-11-07 13:33:58 UTC+08:00
.. tags: inferential-statistics, Correlations
.. category:
.. link:
.. description:
.. type: text
-->

**Relationships**     
How one variable is related to the other?

**Variable X and Y**      
X is often referred to as the predictor, explanatory, independent variable.      

Y is often referred as the outcome, response, dependent variable.  

Scatterplot is a popular/ most common way to show relationship of X and Y variables.      

**Strong Relationships**      
Strong relationships usually have less scattered plots.  If we draw an eclipse surrounding the data points, the smaller the ratio of minor axis to the major axis, the stronger the relationship is.  

**Direction of Relationships**         
Positively related - Y responses in the same direction as X changes; Negatively related - Y responses in opposite directions of X changes.

**Correlation Coefficient, (r)**      
Also known as Pierson's r.  

r is a fraction, with the covariance of x and y (how much do they vary together) as the numerator, and the product of standard deviation of x  and standard deviation of y as the denominator.  
\\[
  r = \frac{cov(x,y)}{ S_x * S_y } = \frac{cov_{x,y}}{ S_x * S_y }
\\]    
r measures the strength of a relationship, by measuring how closely the data falls along a straight line.      

Even though r is a ratio, it is not interpreted as a percentage.  However, \\(r^2\\) is a percentage of the variation in y explained by variation in x.  \\(r^2\\) is called the coefficient determination.       

**True Correlation of Population, rho, \\( \rho \\)**       
We usually perform hypothesis testing with t-tests.
\\[
  H_{0} : \rho = 0 \\\\
  H_{1} : \rho \gt 0 \\\\
  H_{1} : \rho \lt 0 \\\\
  H_{1} : \rho \ne 0
\\]

**Causation vs Correlations**      
**Causation** - One variable caused another to happen.     

**Correlation** - There is a relationship between two variables.  But there are lots of lurking variables.  For example, there are two variables X and Y.  They could have a relationship because both of them are influenced by variable A, or Y is influenced by X **through** variable A.  In this case, variable A is called the mediating variable.  

To make a causal statement:   
     - the independent variable would have to occur BEFORE the dependent variable.  
     - have to rule out other lurking variables too

**Fallacies**    
Ambiguous Temporal Precedence - we don't know which variable happens first.     
Third variable problem      
Post-hoc fallacy      


**t value and Correlation Coefficient, (r)**     
t value and r:
\\[
  t = \frac{r  \sqrt{N-2}}{\sqrt{1-r^2}}
\\]
where \\(df\\) is \\( N - 2 \\)
