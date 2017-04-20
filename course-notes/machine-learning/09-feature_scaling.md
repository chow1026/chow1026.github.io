<!--
.. title: Feature Scaling
.. slug: 09-feature_scaling
.. date: 2017-04-20 06:53:53 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## Introduction

Feature scaling is a method used to standardize the range of independent variables or features of data. In [data processing][d8df68d4], it is also known as data normalization and is generally performed during the data preprocessing step.

  [d8df68d4]: https://en.wikipedia.org/wiki/Data_processing "Data Processing"

Since the range of values of raw data varies widely, in some [machine learning][260a192e] algorithms, objective functions will not work properly without [normalization][7b57696d]. For example, the majority of [classifiers][7bfee429] calculate the distance between two points by the [Euclidean distance][ce5a8c4d]. If one of the features has a broad range of values, the distance will be governed by this particular feature. Therefore, the range of all features should be normalized so that each feature contributes approximately proportionately to the final distance.

  [260a192e]: https://en.wikipedia.org/wiki/Machine_learning "Machine Learning"
  [7b57696d]: https://en.wikipedia.org/wiki/Normalization_(statistics) "Normalization"
  [7bfee429]: https://en.wikipedia.org/wiki/Statistical_classification "Classifiers"
  [ce5a8c4d]: https://en.wikipedia.org/wiki/Euclidean_distance "Euclidean Distance"

Another reason why feature scaling is applied is that [gradient descent][68a95e42] converges much faster with feature scaling than without it.

  [68a95e42]: https://en.wikipedia.org/wiki/Gradient_descent "Gradient Descent"


## Methods

### Rescaling     
The simplest method is rescaling the range of features to scale the range in [0, 1] or [−1, 1]. Selecting the target range depends on the nature of the data. The general formula is given as:

\\( x' = \frac{x- \text{min}(x)} {{\text{max}}(x)-{\text{min}}(x)} \\)

where \\(  x \\) is an original value, \\( x' \\) is the normalized value. For example, suppose that we have the students' weight data, and the students' weights span [160 pounds, 200 pounds]. To rescale this data, we first subtract 160 from each student's weight and divide the result by 40 (the difference between the maximum and minimum weights).

### Standardization     
In machine learning, we can handle various types of data, e.g. audio signals and pixel values for image data, and this data can include multiple [dimensions][c4b557f1]. Feature standardization makes the values of each feature in the data have zero-mean (when subtracting the mean in the numerator) and unit-variance. This method is widely used for normalization in many machine learning algorithms (e.g., [support vector machines][bc4f9bb9], [logistic regression][c8c8c387], and [neural networks][ff1bcf26]). This is typically done by calculating [standard scores][76c50914]. The general method of calculation is to determine the distribution mean and standard deviation for each feature. Next we subtract the mean from each feature. Then we divide the values (mean is already subtracted) of each feature by its standard deviation.

  [c4b557f1]: https://en.wikipedia.org/wiki/Dimensions "Dimensions"
  [bc4f9bb9]: https://en.wikipedia.org/wiki/Support_vector_machine "Support Vector Machine"
  [c8c8c387]: https://en.wikipedia.org/wiki/Logistic_regression "Logistic Regression"
  [ff1bcf26]: https://en.wikipedia.org/wiki/Neural_network "Neural Network"
  [76c50914]: https://en.wikipedia.org/wiki/Standard_score "Standard Score"

\\( x'= \frac{x-{\bar {x}}}{\sigma } \\)

Where \\(  x \\) is the original feature vector, \\( \bar {x} \\) is the mean of that feature vector, and \\( \sigma \\)  is its standard deviation.

### Scaling to unit length     
Another option that is widely used in machine-learning is to scale the components of a feature vector such that the complete vector has length one. This usually means dividing each component by the [Euclidean length][af4f30b9] of the vector. In some applications (e.g. Histogram features) it can be more practical to use the L1 norm (i.e. Manhattan Distance, City-Block Length or [Taxicab Geometry][1aa9e702]) of the feature vector:

  [1aa9e702]: https://en.wikipedia.org/wiki/Taxicab_Geometry "Taxicab Geometry"
  [af4f30b9]: https://en.wikipedia.org/wiki/Euclidean_length "Euclidean Length"

\\(  x'= \frac {x}{||x||} \\)
This is especially important if in the following learning steps the Scalar Metric is used as a distance measure.
