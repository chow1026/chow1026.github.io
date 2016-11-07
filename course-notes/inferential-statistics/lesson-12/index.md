<!--
.. title: Inferential Statistics - One-Way ANOVA
.. slug: lesson-12
.. date: 2016-10-14 10:25:32 UTC+08:00
.. tags: inferential-statistics, one-way ANOVA, ANOVA
.. category:
.. link:
.. description:
.. type: text
-->

In lesson 11, we learned to perform t-tests for two independent samples.  However, in real statistical studies, there are a lot of times we need to compare more than two independent samples.  When we have \\( n \\) independent samples, the number of t-tests we need to perform are:
<!-- {n+1 \choose 2k} == \binom{n+1}{2k} -->
\\[
  \text{no of t-tests with n samples} = \binom{n}{2} = \frac{n!}{2!(n-2)!}
\\]

However, the same concept of t-test applies here.  Remember t is defined by a function of the distance apart from each other and the variability of each sample.
\\[
  t_{statistic} = \frac{ \bar{X_1} - \bar{X_2}}{ \sqrt{ \frac{ S_p^2 }{ n_1 } + \frac{ S_p^2 }{ n_2 }}}
\\]
When we compare 3 or more samples, we compare distance/variability between means (as numerator) and some kind of sample error (as the denominator)

**Think about this:**   
Q: How can we compare three or more samples?   
A: Find the average squared deviation of each sample means.

Q: Will the **Grand Mean**, mean of the sample means be the same as the mean of all values in each sample?   
A: Sometimes.  Only when the sample sizes are equal for each sample, that the Grand Mean will be the same.

**Between Group Variability**   
Between group variability is the variability between/among samples.     
Q: What conclusions can we draw from the deviation of each sample mean from the mean of the means?   
A: The smaller the distance between sample means, the less likely the population means will defer significantly.  Vice versa the greater the distance between sample means, the more likely population means will differ significantly.  

**Within Group Variability**   
Within group variability is the variability of the individual samples within a sample.    
The greater the variability of each individual sample, the less likely population means will differ significantly.  (thinner, non overlapping normal distribution.)   
The smaller the variability of each individual sample, the more likely population means will differ significantly.  (wider, overlapping normal distribution)

Since we are analyzing the variabilities between samples and within samples, we call this Analysis of Variability (ANOVA).  We have one way ANOVA when we have one independent variable (sometimes called a factor)  

**F Statistics**   
F statistics is the ratio of between group variability (numerator) to the within group variability (denominator)
If the between group variability is big, it constitutes to big F statistics, which results in rejecting the null hypothesis and accepting the alternative hypothesis.  
Whereas if the within group variability is large, it makes the F statistics small, which results in accepting the null hypothesis and rejecting the alternative hypothesis.

\\[
F = \frac{ \text{between group variability}}{ \text{within group variability}} \\\\  
  = \frac{ \sum_{j=0}^k n_j (\bar{x_j} - \bar{x_G})^2 / (k-1)}{\sum_{i=0}^N  (x_i - \bar{x_k})^2 / (N-k) } \\\\
  n_j \text{ is sample size for each sample}   \\\\
  = \frac{ n \sum_{j=0}^k (\bar{x_j} - \bar{x_G})^2 / (k-1)}{\sum_{i=0}^N (x_i - \bar{x_k})^2 / (N-k) } \text{when sample size is same for all samples}  \\\\
  k \text{ is number of sample groups}      \\\\
  N \text{ is total number of all samples of each sample group}     \\\\
\\]

F can also be formulated as
\\[
F = \frac{SS_{between} / df_{between}}{SS_{within} / df_{within}} \text{ where } SS \text{ stands for Sum of Squares }      \\\\
  = \frac{MS_{between}}{MS_{within}} \text{ where } MS \text{ stands for Mean Square }
\\]

Note that \\(df_{between}\\) is \\( k - 1 \\) while \\(df_{within}\\) is \\( N - k \\)

If we add \\(df_{between}\\) and \\(df_{within}\\) up, we get \\( N - 1\\) which is the total degree of freedom \\(df_{total}\\)
\\[
df_{total} = df_{between} + df_{within} \\\\
= N - 1
\\]

Similarly, the total variation \\(SS_{total}\\) is the sum of \\(SS_{between}\\) and \\(SS_{within}\\).  
\\[
SS_{total} = SS_{between} + SS_{within} \\\\
= \sum{(x_i - \bar{x_G}) ^ 2}
\\]
