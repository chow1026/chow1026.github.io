<!--
.. title: Inferential Statistics - ANOVA Continued.
.. slug: lesson-13
.. date: 2016-11-03 21:55:35 UTC+08:00
.. tags: inferential-statistics, one-way ANOVA, ANOVA, Tukey HSD, Cohen's D, 
.. category:
.. link:
.. description:
.. type: text
-->
**Multiple Comparison Tests**     
After rejecting the null, we conduct additional testings to determine which sample is truly different and/or if the results is due to sampling errors.  These tests are called Multiple Comparison Tests.      

One of the popular Multiple Comparison Tests is Tukey's Honestly Significant Differences.      
**Tukey's Honestly Significant Differences (HSD)**    
Tukey's HSD is calculated as the following:
\\[
\text{Tukey's HSD} = q * \sqrt{\frac{MS_{within}}{n}} \\\\
q \text{ is looked up with } df_{within} \text{ and } k \text{, the number of treatments/sample groups}   \\\\
n \text{ is the number of samples in one sample group}
\\]   

If the mean difference between/among treatments are greater than Tukey's HSD, the difference is significant.    

Note this is very similar to Z test and T test. For Z tests, the margin of error is:
\\[
\text{Margin of Error} = z * \frac{\sigma}{\sqrt{n}}
\\]

Whereas for t tests, the margin of error is:
\\[
\text{Margin of Error} = t * \frac{s}{\sqrt{n}}
\\]

**Cohen's D for Multiple Comparisons**    
For normal comparisons, Cohen's D is calculated by
\\[
\text{Cohen's D, } d = \frac{\bar{X_1} - \bar{X_2}}{SD_{pooled}}
\\]   

In multiple comparisons, Cohen's D is calculated by
\\[
\text{Cohen's D, } d = \frac{\bar{X_1} - \bar{X_2}}{\sqrt{MS_{within}}}
\\]

Cohen's D is calculated per pair comparisons.  

**\\( \mathbf{\eta ^ 2} \\)**    
\\( \eta ^2 \\) is defined as the proportion of total variance that is due to between-group differences (explained variation).  

\\[
\eta ^2 = \frac{SS_{between}}{SS_{total}} \\\\
      = \frac{SS_{between}}{SS_{between} + SS_{within}}
\\]    

**Reporting Reports of Anova**    
We report the results of F Statistics as the following:     
\\[
   F(df_{between}, df_{within}) = 27 \quad p < 0.05 \quad \eta ^2 = 0.90 \quad \\\\
   \text{p is estimated, by hand} \\\\
   F(df_{between}, df_{within}) = 27 \quad p = 0.001 \quad \eta ^2 = 0.90 \quad \\\\
   \text{exact p value calculated by software} \\\\
\\]


**ANOVA for Groups with Different Sample Sizes**    
Grand mean
\\[
  \text{Grand mean, } \bar{X_G} = \frac{ \sum_{j=0}^k n_j (\bar{x_j}) }{\sum_{j=0}^k n_j } \\\\
  n_j \text{ is sample size for each sample} \\\\  
  k \text{ is number of sample groups}      \\\\
\\]    

SS (Sum of Squares) Between     
\\[
  \text{sum of squares, } SS_{between} = \sum_{j=0}^k n_j (\bar{x_j} - \bar{x_G})^2 \\\\
  n_j \text{ is sample size for each sample}   \\\\
\\]    

SS (Sum of Squares) Within     
\\[
  \text{sum of squares, } SS_{within} = \sum_{i=0}^N (x_i - \bar{x_k})^2 \\\\
  k \text{ is number of sample groups}      \\\\
  N \text{ is total number of all samples of each sample group}     \\\\
\\]    

DF (Degress of Freedom) Between     
\\[
  \text{degrees of freedom, } df_{between} = k - 1 \\\\
  k \text{ is number of sample groups}    \\\\
\\]    

DF (Degress of Freedom) Within     
\\[
  \text{degrees of freedom, } df_{within} = N - k \\\\
  k \text{ is number of sample groups}      \\\\
  N \text{ is total number of all samples of each sample group}     \\\\
\\]    

MS (Mean Squares) Between     
\\[
  \text{Mean square, } MS_{between} = \frac{SS_{between}}{df_{between}}  \\\\
  = \frac{\sum_{j=0}^k n_j (\bar{x_j} - \bar{x_G})^2}{k - 1}
\\]    

MS (Mean Squares) Within     
\\[
\text{Mean square, } MS_{within} = \frac{SS_{within}}{df_{within}}  \\\\
= \frac{\sum_{i=0}^N (x_i - \bar{x_k})^2}{N - k}
\\]    

F Stats
\\[
\text{F Statistics, } F = \frac{MS_{between}}{MS_{within}}  \\\\
= \frac{\sum_{j=0}^k n_j (\bar{x_j} - \bar{x_G})^2 / (k - 1)}{\sum_{i=0}^N (x_i - \bar{x_k})^2 / (N - k)}
\\]   

**\\( \mathbf{\eta ^ 2} \\)**  
\\[
\eta ^2 = \frac{SS_{between}}{SS_{total}} \\\\
      = \frac{SS_{between}}{SS_{between} + SS_{within}}
\\]  


**ANOVA Power**    
Increase POWER in order to avoid Type II statistical error where we fail to reject the null when there is a treatment effect.   

In the case of drug testing, we want to:    
- test **more people**    
- give each drug to **very similar** groups of people    
- test with a **strong** dosage    

**ANOVA Assumptions & Conclusions**     
We assume:    
- **Normality**: the population of which our samples are from are all normally distributed.    
- **Homogeneity of Variance**: the samples come from populations that have equal amount of variability.     
- **Independence of Observations**: The results found from one samples won't affect the others.   

We could have the following exceptions:    
- violate the normality if the sample is large    
- violate the homogeneity of variance if:    
        - almost equal sample sizes    
        - ratio of any two variances doesn't exceed 4       
-
