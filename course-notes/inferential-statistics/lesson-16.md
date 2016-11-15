<!--
.. title: Inferential Statistics - Chi-Squared Tests
.. slug: lesson-16
.. date: 2016-11-09 13:10:55 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## Types of Data     
- **Ordinal Data** - ranks with no fixed intervals nor zeros   
- **Interval Data** - ranks with equal intervals     
- **Ratio Data** - ranks with equal intervals and an absolute zero   
- **Nominal/Categorical Data** - data with no numerical values (typically yes/no, in/out, successful/unsuccessful)    


## Types of Tests     
- **Parametric** - hypothesis testing that make assumptions about the parameters of the populations, \\( \mu \\) and \\( \sigma \\).
- **Non-Parametric** - hypothesis testing that do not require population parameters

## Characteristics of Non-Parametric Testings    
- There is no way to calculate a mean or standard deviation      
- The data is based on frequencies or proportions    
- The data is nominal (successful vs unsuccessful, 1 or 0, yes or no, mountain vs beach etc.)    
- The data are not based on Normal distribution    

## \\( \chi^2 \\) Goodness of Fit Test    
How well our observed frequencies 'fit' our expected frequencies?   
\\[
  \chi ^2 = \sum{ \frac{(f_0 - f_e)^2}{f_e} }
\\]
\\( \chi^2 \\) is smaller when the observed value is closer to the expected value.     
\\( \chi^2 \\) is NEVER negative and therefore \\( \chi^2 \\) statistic is one-directional.     

For each category, we have one \\( \chi^2 \\) statistics.  When we have more categories, \\( \chi^2 \\) statistics get bigger with the number of categories.    

## Degrees of Freedom    
For n x m, 2 dimensional nominal data:
\\[
  df = (N_n - 1) * (N_m - 1) \\\\
  \text{where } N_n \text{ and }N_m \text{ are number of columns, and number of rows respectively. }
\\]

## Cramer's V \\( (\phi_c) \\)   
\\[
  \phi_c = \sqrt{\frac{\chi^2}{n(k-1)}}  \\\\
  k \text{ is the smaller number between number of rows or number of columns}\\\\
  n \text{ is the total sample size regardless of treatments}
\\]

## Assumptions and Restrictions for \\(\chi^2\\) Tests    
- Avoid dependent observations.  Independence will be violated if any participants were given two treatments instead of one.     
- Avoid small expected frequencies, therefore in general have a larger number of participants.   Sample size should be at least 20, and each expected cell frequencies should be at least 5.    
