<!--
.. title: Inferential Statistics - T-Test, Independent Samples
.. slug: lesson-11
.. date: 2016-10-11 12:35:53 UTC+08:00
.. tags: inferential-statistics, t-test, independent-samples
.. category:
.. link:
.. description:
.. type: text
-->


**Dependent Samples (Repeated Measures)** deals with within-subject designs.  
Types of Dependent Samples:

- Two conditions (a control group and a treatment group, OR two groups with two types of treatment)
- Longitudinal (same subject group measured two different points in time)
- Pre-test, Post-test (subject group measure before and after treatment)

Pros:

- Controls for individual differences:
    - Use fewer subjects
    - More cost-effective
    - Less time-consuming
    - Less expensive

Cons:

- Carry-over effect:
    - The second measurement might be affected by the first treatment
- The order in which treatments were given might influence the results


#Independent Samples:
Independent Samples deals with between-subject designs.
Types of Independent Samples:

- Experimental
- Observational

Pros:

- Control for carry-over effect:
    - The second measurement less likely be affected by the first treatment
- The order in which treatments no longer influence the results

Cons:

- Little/no control for individual differences:
- Need more subjects
- Less cost-effective
- More time-consuming
- More expensive

# Two-Sample Tests
Considering two independent normally distributed samples collected, when we subtract those two data, we get a new dataset.  
\\[
    N ( \mu_{1}, \sigma_{1} ) - N ( \mu_{2}, \sigma_{2} ) = N ( \mu_{1} - \mu_{2}, \sqrt{ \sigma_{1}^2 + \sigma_{2}^2 } )
\\]


The standard deviation, \\( SD \\) would be:
\\[
    SD = \sqrt{ SD_{1}^2 + SD_{2}^ 2 }
\\]

The standard error, \\( SE \\) would be:
\\[
    SE = \sqrt{ \frac{SD_{1}^2}{n_{1}} + \frac{SD_{2}^2}{n_2}}
\\]

The t statistic, \\( t_{statistic} \\) would be:
\\[
    t_{statistic} = \frac{ (\bar{x_{1}} - \bar{x_{2}} ) - (\mu_{1} - \mu_{2})}{ SE }
\\]

The degree of freedom, \\( df \\) would be:
\\[
    df = (n_{1} - 1) + (n_{2} - 1) = n_{1} + n_{2} - 2
\\]
or the smaller value between
\\(
(n_{1} - 1) \text{ and } (n_{2} - 1)
\\).

# Pooled Variance
Pooled variance is a method for estimating variance
given several different samples taken in different circumstances where the mean may vary
between samples but the true variance is assumed to remain the same. The pooled variance is
computed by using
The Pooled Variance, \\( S_{p}^2 \\) would be:
\\[
    S_{p}^2 = \frac{(SS_{x} + SS_{y})}{df_{x} + df_{y}}
\\]
where \\( SS_{x} = \sum (x_{i} - \bar{x})^ 2 \\)
and \\( SS_{y} = \sum (y_{i} - \bar{y})^ 2 \\)

The Standard Error, \\( SE_{(\bar{x}-\bar{y})} \\), using Pooled Variance is:

\\[
    SE_{(\bar{x}-\bar{y})} = \sqrt{ \frac{S_{p}^2}{n_x} + \frac{S_{p}^2}{n_y} }
\\]

The full t statistic \\( t_{statistic} \\) formula would be:
\\[
    t_{statistic} = \frac{ (\bar{x} - \bar{y}) - \delta }{ SE_{(\bar{x}-\bar{y})} }
\\]
\\(\bar{x} - \bar{y} \\) is called the observed difference.
The \\( \delta \\)expected_diff is derived from the Null Hypothesis, \\( H_0 \\), when
\\[
    H_0: \mu_x - \mu_y = \delta
\\]
There are lots of cases where \\( \delta \\) was assumed 0.  

When we use Pooled Variance, we hold the following assumptions:
1. X and Y should be two random samples from two independent populations.   
2. Populations that X and Y come from, should be approximately normal.  This is less important when sample size is really large ( >30).  
3. Sample data can be used to estimate population variances.
4. Population variances should be roughly equal.
