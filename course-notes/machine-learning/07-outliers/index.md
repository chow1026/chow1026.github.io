<!--
.. title: Outliers
.. slug: 07-outliers
.. date: 2017-04-20 06:51:18 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

In statistics, an outlier is an observation point that is distant from other observations. An outlier may be due to variability in the measurement or it may indicate experimental error; the latter are sometimes excluded from the data set.

Outliers can occur by chance in any distribution, but they often indicate either [measurement error][6daa0a61] or that the population has a [heavy-tailed distribution][aa1e1c92]. In the former case one wishes to discard them or use statistics that are robust to outliers, while in the latter case they indicate that the distribution has high skewness and that one should be very cautious in using tools or intuitions that assume a normal distribution. A frequent cause of outliers is a mixture of two distributions, which may be two distinct sub-populations, or may indicate 'correct trial' versus 'measurement error'; this is modeled by a [mixture model][ea7ad48c].

  [6daa0a61]: https://en.wikipedia.org/wiki/Measurement_error "Measurement Error"
  [aa1e1c92]: https://en.wikipedia.org/wiki/Heavy-tailed_distribution "Heavy Tailed Distribution"
  [ea7ad48c]: https://en.wikipedia.org/wiki/Mixture_model "Mixture Model"

In most larger samplings of data, some data points will be further away from the sample mean than what is deemed reasonable. This can be due to incidental systematic error or flaws in the theory that generated an assumed family of probability distributions, or it may be that some observations are far from the center of the data. Outlier points can therefore indicate faulty data, erroneous procedures, or areas where a certain theory might not be valid. However, in large samples, a small number of outliers is to be expected (and not due to any anomalous condition).

Outliers, being the most extreme observations, may include the sample maximum or sample minimum, or both, depending on whether they are extremely high or low. However, the sample maximum and minimum are not always outliers because they may not be unusually far from other observations.

Naive interpretation of statistics derived from data sets that include outliers may be misleading. For example, if one is calculating the average temperature of 10 objects in a room, and nine of them are between 20 and 25 degrees Celsius, but an oven is at 175 °C, the median of the data will be between 20 and 25 °C but the mean temperature will be between 35.5 and 40 °C. In this case, the median better reflects the temperature of a randomly sampled object (but not the temperature in the room) than the mean; naively interpreting the mean as "a typical sample", equivalent to the median, is incorrect. As illustrated in this case, outliers may indicate data points that belong to a different population than the rest of the sample set.

Estimators capable of coping with outliers are said to be robust: the median is a robust statistic of central tendency, while the mean is not. However, the mean is generally more precise estimator.
