<!--
.. title: Inferential Statistics - Estimation
.. slug: lesson-8
.. date: 2016-09-14 12:33:51 UTC+08:00
.. tags: inferential-statistics, estimation
.. category:
.. link:
.. description:
.. type: text
-->

## Lesson 8: Estimation ##
1. Any sampling distribution is a normal distribution.   
2. The sample mean, \\( M \\), approximately equal to the population mean, i.e. \\( M \approx \mu \\).  
3. The standard error of the sample, SE, is approximately equals to:
    \\[ SE = \frac{\sigma}{\sqrt{n}} \\] where \\( n \\) is sample size, and \\( \sigma \\) is standard deviation of the population.  
4. On any sampling distribution, approximately 68% of population falls within \\(\pm 1 \frac{ \sigma }{ \sqrt{n} } \\) of the sample mean \\( M \\).
5. On any sampling distribution, approximately 95% of population falls within \\(\pm 2 \frac{ \sigma }{ \sqrt{n} } \\) of the sample mean \\( M \\).
6. The distance, \\( 2 \frac{ \sigma }{ \sqrt{n} } \\) or is called **Margin of Error**.  
7. **Point estimation** involves the use of sample data to calculate a single value which is to serve as a "best guess" or "best estimate" of an unknown population parameter.
8. An "intervention" is a factor that we expect will change the population parameters.
9. Given the sample mean of a sample with intervention is \\( M \\), \\( M \\) serves as a point estimate of the mean of the whole population if the intervention is applied to the whole population.  However, the exact value of the population mean, \\( \mu \\), does not exactly equal to \\( M \\).   
10. With a **95% Confidence Interval** (2 Standard Error, SE), we estimate the population mean with the same intervention, \\( \mu \\) falls in a range, based on the following:
    \\[ \mu - 2 \frac{ \sigma }{ \sqrt{n}} \lt M \lt \mu + 2 \frac{ \sigma }{ \sqrt{n} } \\]
    \\[ - 2 \frac{ \sigma }{ \sqrt{n}} \lt M - \mu \lt + 2 \frac{ \sigma }{ \sqrt{n} } \\]
    \\[ - M - 2 \frac{ \sigma }{ \sqrt{n}} \lt - \mu \lt - M + 2 \frac{ \sigma }{ \sqrt{n} } \\]
    \\[ M + 2 \frac{ \sigma }{ \sqrt{n}} \gt \mu \gt M - 2 \frac{ \sigma }{ \sqrt{n} } \\]
    \\[  M - 2 \frac{ \sigma }{ \sqrt{n} } \lt \mu \lt M + 2 \frac{ \sigma }{ \sqrt{n}} \\]
11. If we apply the above formula with 1 standard error, 1 SE, that gives us an range of which the population mean (with same intervention), with **68% Confidence Interval**, to be:
    \\[  M - \frac{ \sigma }{ \sqrt{n} } \lt \mu \lt M + \frac{ \sigma }{ \sqrt{n}} \\]
12. The Z-value that bounds 95% of the data is **-1.96 through +1.96**.  That means for a sampling distribution, 95% of the sample means fall within 1.96 standard errors (SE) away from the population mean. It is also the **95% Confidence Interval**.   
13. A **"treatment effect"** occurs when the intervention affects the population mean. When the sample mean is far on the tails of the sampling distribution, and therefore unlikely to have occurred by chance, there is evidence for a treatment effect.
14. If we want a higher confidence interval (CI), say, **98% Confidence Interval**, the z-score should be 2.33.  98% of the sample means fall within 2.33 standard error (SE) away from the population mean.  
15. \\( \pm 2.33 \\) are the critical values of Z for 98% confidence.  
16. \\( \pm 1.96 \\) are the critical values of Z for 95% confidence.
