<!--
.. title: Inferential Statistics - Hypothesis Testing
.. slug: lesson-9
.. date: 2016-09-20 17:36:10 UTC+08:00
.. tags: inferential-statistics, hypothsis-testing
.. category:
.. link:
.. description:
.. type: text
-->

# Hypothesis Test and Alpha Levels

A Hypothesis test is used to test a claim that someone has about an observation may be different from the known population parameter.  

**Alpha level** (**\\( \alpha \\)**) of a hypothesis test helps us determine the critical region of a distribution.  Refer to [Critical Regions](#critical-region) below.

**Null Hypothesis** is always an equality.  It is the claim we are trying to provide evidence _against_.  We commonly write the null hypothesis as one of the following:
\\[  H_{0} : \mu_{0} = \mu\\\  H_{0} : \mu_{0} \ge \mu\\\  H_{0} : \mu_{0} \le \mu \\]

**Null Hypothesis** is result we are checking against the claim.  This is always some kind of inequality.  We commonly write the alternative hypothesis as one of the following:
\\[  case\;a >> H_{0} : \mu_{0} \neq \mu\\\  case\;b >> H_{0} : \mu_{0} \gt \mu\\\  case\;c >> H_{0} : \mu_{0} \lt \mu \\]

If we know which direction we are checking against the claim, use case b or case c, else we typically use case a.  Case a is a two tailed test, while case b and case c are one tailed tests.  Read more on this [below](#one-tailed-two-tailed).  

# <a id="critical-region" name="critical-region"></a>Critical Regions
When it comes to constructing a hypothesis test, it is best to choose a significant level before the test is performed.  The results of the test can be reported as significant a certain critical level, but it is important that you are not "fishing" for results before seeing the results in your sample.  For additional readings on Hypothesis Testing, here is an [article][b5667722].  

  [b5667722]: http://blog.minitab.com/blog/adventures-in-statistics/understanding-hypothesis-tests:-significance-levels-alpha-and-p-values-in-statistics "Hypothesis Testing"

The corresponding Z-critical values, \\( Z_{critical} \\) at each \\( \alpha \\) level for one-tailed test and two-tailed test respectively:
\\[
\\begin{array}{c|cc}
\alpha & \text{one-tailed} & \text{two-tailed} \\\
\hline
0.05 & 1.67 \; or\; -1.67 & \pm 1.96 \\\
0.01 & 2.32 \; or\; -2.32 & \pm 2.57 \\\
0.001 & 3.08 \; or\; -3.08 & \pm 3.27
\\end{array}
\\]

If we get a sample mean in the critical region, then we decide that most likely those sample means by chance.  The \\( Z_{critical} \\) values are the same that we used to calculate confidence intervals.  

When we do statistical test, we'll set our own criteria for making a decision (in other words, we'll choose an alpha level). Then we decide if the probability of obtaining that sample mean is less than the alpha level (ie. sample means fall in the critical region, and \\(Z\\) is greater than \\(Z_{critical}\\)). Then if there is an evidence of an effect (of the intervention).

Note that we **CANNOT prove** if a hypothesis is true.  We can only obtain evidence to reject the null hypothesis.  

**Example**:
A null hypothesis says "Most (more than 50%) dogs have four legs." and the alternative hypothesis says "Most dogs have less than four legs."

In a sample of 10 dogs, there are 6 dogs with less than four legs.  

In this case we are taking 50% as significance level.  We are able to reject the null hypothesis based on this.  Under a typical statistical test (such as using a 5% significance level), this sample data would be evidence against null hypothesis, but not necessarily enough evidence/information to reject the null hypothesis.  

However, if the definition of null hypothesis was changed to indicate 70% of dogs have four legs, then our current evidence would be enough to reject the null hypothesis to reject the null hypothesis at a 5% significance level.  

# <a id="one-tailed-two-tailed" name="one-tailed-two-tailed"></a> One Tailed and Two Tailed
Take a hypothesis test:
\\[
    H_{0}:
    \begin{cases}
      \mu = \mu_{I},  & \mu_{I} \text{is post intervention}
    \end{cases} \\\
    H_{A}:
    \begin{cases}
      \mu \lt \mu_{I},  & \text{right one-tailed, with } \mu_{I} \text{ greater than } \mu \\\
      \mu \gt \mu_{I},  & \text{left one-tailed, with } \mu_{I} \text{ less than } \mu \\\
      \mu \neq \mu_{I},  & \text{right one-tailed, with } \mu_{I} \text{ greater or less than } \mu
    \end{cases}
\\]

We choose a one-tailed, or directional hypothesis test when we predict a direction of the treatment effect.  Alternatively, when we do not predict the direction of the treatment, we choose the two-tailed or non-directional test.  In general we use two-tailed because it is more conservative.  We are less likely to reject the null when it is true.  It also prevents us from mistaking the wrong direction of the effect.  


# Decision Errors
There are two types of Hypothesis Decision Errors:
**Type I error**: is when you reject the null when the null hypothesis is actually true.  
**Type II error**: is when you fail to reject the null when the null hypothesis is actually false.  
