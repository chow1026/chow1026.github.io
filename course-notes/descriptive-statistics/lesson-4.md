<!--
.. title: Descriptive Statistics - Variability
.. slug: lesson-4
.. date: 2016-08-17 11:29:46 UTC+08:00
.. tags: descriptive-statistics, variability
.. category:
.. link:
.. description:
.. type: text
-->

## Lesson 4: Variability ##
### General Ideas of Variability###

1. **Range**: The maximum data point minus the minimum data point.  
2. **Wide Spread**: The data set has shorter and wider distribution.
3. **Consistency**: When a data is more consistent, it forms taller and narrower distribution.  
4. Outlier(s) usually widen the range of distribution and INCREASES variability.  Statisticians usually cut off outliers.
5. 1st Quartile, **\\( Q_{1} \\)**, is the 25% of the distribution, while 3rd Quartile, **\\( Q_{3} \\)**, is the 75% of the distribution.  2nd Quartile, also known as Median, is the 50% of the distribution.  
6. **Interquartile Range**:
    - **\\(IQR =  Q_{3} - Q_{1} \\)**
7. Facts about **\\(IQR \\)**:
    - About 50% of data lies between IQR.
    - IQR may or may not be affected by every value in the dataset.  
    - IQR is NOT affected by outliers.
8. A data point is considered an outlier if any of the below is true:
    - \\[ x_{outlier} < Q_{1} - 1.5*IQR \\]
    - \\[ x_{outlier} > Q_{3} - 1.5*IQR \\]

### Box Plots ###
1. Key Elements of Box Plots:
    - Max, Min (two handles of the box)
    - \\( Q_{1} \\), \\( Q_{3} \\), \\( Q_{2} \\) (aka Median) forms the box, with Median in the center "splitting" the box.
    - Outliers, drawn as dots next to /outside of Max and/or Min.  
2. Box plots sometimes don't tell about the distribution model of data.  The box plot for normal, bimodal, or uniform distribution are the same.
3. Although usually the mean lies between \\( Q_{1} \\) and \\( Q_{3} \\), it may lie outside of it, if there are outliers.

### Measuring Variability ###
1. To measure variability, we find the average distance between each data value and the mean.
2. \\[ Deviation, \delta = x_{i} - \bar{x} \\]
3. Average Deviation, \\(\bar{\delta}\\):
    - \\[ \bar{\delta} = \frac{ \sum_{i=0}^N{  \lvert{x_{i} - \bar{x} } \rvert }}{N}\\]
    - \\[ \bar{\delta} = \frac{ \sum_{i=0}^N{\lvert\bar{x} - x_{i}\rvert}}{N} \\]
    - \\[ \bar{\delta} = \sum_{i=0}^N{\frac{ \lvert \bar{x} - x_{i} \rvert }{N}} \\]
4. Squared Deviation, \\( \delta^2 \\):
    - \\[ \delta^2 = {\lvert{x_{i} - \bar{x} } \rvert}^2 \\]
5. Sum of Squares, \\( \sum_{i=0}^N(\delta^2) \\), aka \\( SS \\):
    - \\[ SS = \sum_{i=0}^N{({x_{i} - \bar{x}})^2} \\]
6. Variance, \\( \sigma^2 \\), which is simply the Mean of \\( SS \\), \\( \bar{SS} \\) is:
    - \\[ \sigma^2 = \frac{\sum_{i=0}^N{{({x_{i} - \bar{x}})}^2}}{N} \\]
7. Standard Deviation, \\( \sigma \\), is the square root of variance.  
    - \\[ \sigma = \sqrt{\frac{\sum_{i=0}^N{{({x_{i} - \bar{x}})}^2}}{N}} \\]
8. Why Standard Deviation? In a perfectly normal distribution where mean equals to median equals to mode, 68% of the data values would fall between \\( -1 \sigma \\) and \\( +1 \sigma \\), 95% of the data values will fall between \\( -2 \sigma \\) and \\( +2 \sigma \\)
9. When a sample is taken from a population, the sample standard deviation is usually smaller than true standard deviation, \\( \sigma \\), of the population.  To correct that, we apply Bessel's Correction.  The corrected/estimation sample standard deviation, denoted as \\( s \\), and corresponding variance, will have the formulas below:
    - \\[ s^2 = \frac{\sum_{i=0}^N{{({x_{i} - \bar{x}})}^2}}{N -1} \\]
    - \\[ s = \sqrt{\frac{\sum_{i=0}^N{{({x_{i} - \bar{x}})}^2}}{N-1}} \\]
