<!--
.. title: Inferential Statistics - T-Test, Dependent Samples
.. slug: lesson-10
.. date: 2016-09-29 13:09:03 UTC+08:00
.. tags: inferential-statistics, t-test, dependent-samples
.. category:
.. link:
.. description:
.. type: text
-->

# T-Test
Z-test works when we know the population parameters such as \\( \mu \\) and \\( \sigma \\).  For any samples drawn from this population, the samples would form a sampling distribution that is a normal distribution, with:
\\[
    mean = \mu  \quad\text{where M is mean of sample means}\\\
    SD = \frac{\sigma}{\sqrt{n}} \quad\text{where n is sample size}
\\]
\\( SD \\) is also known as Standard Error \\( SE \\) which is used for Z score calculation.

For any sample mean, \\( M \\), we can determine where it falls on this sampling distribution by standardizing, aka, finding the z-score \\( Z \\), given its formula below:
\\[
    Z = \frac{M - \mu}{ SE }
\\]

However, much of the times, with sample data, we don't know population \\( \mu \\) and population standard deviation \\( \sigma \\). We only have samples which we must use to draw all our conclusions.  

When working with samples, we usually estimate the population standard deviation using the sample standard deviation with Bassel's correction.  
\\[
  S =  \sqrt{ \frac{ \sum_1^n{ (x_{i} - \bar{x}) ^ 2 }} { n-1 } } \\\
  where S is estimated population standard deviation, n is sample size
\\]

Without population parameters and with only sample data, we end up with a new distribution that is more prone to error, called the t-distribution. The t-distribution is more spread out and thicker in the tails.  

Same principals applies to t-distribution.  When n increases:

- the t-distribution approaches a normal distribution
- the t-distribution gets skinner tails
- S, the estimated population standard deviation, gets closer to the real population standard deviation \\( \mu \\).  


With t-distribution and t-test, we can determine:

1. How different a sample mean is from a population mean
2. How different two sample means are from each other.  These two samples can be either:
    - dependent
    - independent


# Degrees of Freedom

t-distribution are defined by degrees of freedom, \\(df\\), which generally is \\( n - 1 \\) for single dimension data.  The \\(df\\) for 2D or 3D sample is \\[df = (n-1)^d\;\text{where power d is the number of dimension}\\]
Degrees of freedom are the number of pieces of information that can be freely varied, without violating any given restrictions.  It is pieces of independent information to estimate another piece of information. As the degrees of freedom increases, it better approximates the normal distribution.
\\( n - 1 \\) is also known as the effective sample size.  As shown above, it is used to estimate the population standard deviation with Basel's correction.  


# Hypothesis Testing with t-statistics
Like the z-test, if the t-statistic falls far from the mean, where t-statistic is 0, we reject the null. To do so, we compare the sample mean to population mean, by calculating t-statistic.

For one sample t-test, the t-statistic is:
\\[
    t = \frac{\bar{x} - \mu_{0}}{S/\sqrt{n}} \text{where:}\\\
    \bar{x}\text{ is sample mean}\\\
    \mu_{0}\text{ is population mean}\\\
    S \text{ is standard error, aka. standard deviation of sample}\\\
    n \text{ is the sample size}
\\]
The sample mean, \\(\bar{x}\\) is also the point estimate for the population mean.
t-statistics increases when:

- a larger difference between \\(\bar{x}\\) and \\(\mu_{0}\\)
- larger \\( n \\)

For hypothesis testing:

- The **larger** the value of \\(\bar{x}\\), the stronger the evidence that \\(\mu \gt \mu_{0}\\).
- The **smaller** the value of \\(\bar{x}\\), the stronger the evidence that \\(\mu \lt \mu_{0}\\).
- The further the value of \\(\bar{x}\\) from \\(\mu_{0}\\) in either direction, the stronger the evidence that \\(\mu \neq \mu_{0}\\).

We reject the null hypothesis if the t-statistic is less than or greater than the t-critical value, at a given \\( \alpha \\) level.


# P-Value
For one-tailed test, the P-value is the probability above the t-statistic if it is positive, and below the t-statistic if it is negative.  For two tailed test, the p-value will be the sum of probability on both ends.  We reject the null hypothesis when the p-value is less than the \\( \alpha \\) level.

After calculating the t-statistic, we go to [GraphPad][4ad9aaf1] to get the exact P-value. There are also other calculators on [GraphPad][b91c377f] that are worth checking out.  

  [4ad9aaf1]: http://www.graphpad.com/quickcalcs/pValue1/ "P-Value with t and DF"
  [b91c377f]: http://www.graphpad.com/ "GraphPad Calculators"


# Cohen's d
Cohen's d is another common measure of effect size, when comparing means, named after Jacobs Cohen.  It is a **standardized mean difference** that measures the distance between 2 means in standard deviation units.
\\[
    Cohen's d = \frac{\bar{x} - \mu_{0}}{S} \\\
    where\;\bar{x}\text{ is sample mean, }\mu_{0}\text{ is population mean, and }S\text{ is sample standard deviation}
\\]

# Confidence Interval
Confidence interval is the interval where the population mean will probably lie.  
At a given confidence level, or alpha level, we first determine the t-critical value.  
Confidence interval for a two-tailed test is:
\\[
  \\begin{align}
    CI & = M \pm t_{critical, \alpha} \cdot SE_{sample} \\\
    & = M \pm t_{critical, \alpha} \cdot \frac{S}{\sqrt{n}}
  \\end{align}
\\]

# Margin of Error
Margin of Error is one-half width of the confidence interval.  CI's upper bound is sample mean, \\(M + t_{critical} \cdot \frac{S}{\sqrt{n}} \\) plus margin of error; whereas CI's lower bound is sample mean, \\( M - t_{critical} \cdot \frac{S}{\sqrt{n}} \\).  Therefore:
\\[
  Margin\;of\;Error = t_{critical} \cdot \frac{S}{\sqrt{n}}
\\]

# Dependent t-tests
Dependent samples are generated when the same subject takes the test twice.  This is a within subject design.  Examples:

- when same subject is applied two conditions
- subject is given a pre-test and post-test
- longitudinal study (development over time)

The within-subject designs generate paired data.  Then we look at the difference between these two sets of data, \\( D_{i} \\)

# Types of Designs
1. Repeated measures design (eg errors on two types of keyboards)
\\[ H_{0}: \mu_{1} = \mu_{2} \\]
2. Longitudinal design
\\[ H_{0}: \mu_{time1} = \mu_{time2} \\]
3. Pre-test vs Post-test
\\[ H_{0}: \mu_{pre} = \mu_{post} \\]

# Effect Size
In experimental studies, Effect Size refers to the size of a treatment effect.  In non-experimental studies, Effect Size may refer to the strength of the relationships between the variables.  

In the Z-test or one sample t-test, the mean difference is \\( \bar{x} - \mu \\).  Mean differences is great when we variables with easy to understand meanings.

## Types of Effect Size Measures
There are many Effect Size measures, but they all fall into two main groups:

1. Difference Measures:
    - Mean difference
    - standardized difference
        - Cohen's d (in SD units)

2. Correlation Measures:
    - \\( r^2 \\): the proportion (or %) of variation of one variable that is related to ("explained by") another variable.  
        \\[ r^2 = \frac{ t^2 }{ t^2 + df } \\\
            where\; t \text{ is t statistics, not } t_{critical} \text{ and } df \text{ is degree of freedom}
        \\]
    - \\( r^2 \\) is also known as the coefficient of determination.

# Statistical Significance
Statistical Significant means:
- we reject the null
- results are not likely due to chance (sampling error)

# Meaningfulness of Results
- What was being measured?  Do/Does the variable(s) has any practical, social, theoretical importance?
- Effect Size: Small effect size doesn't necessarily mean the results have lower importance, and vice versa, large effect size doesn't necessarily means the results have greater importance.  
- Can we rule out random chance/sampling errors?
- Can we rule out alternative explainations? (lurking variables)
