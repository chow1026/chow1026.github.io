<!--
.. title: Validation
.. slug: 13-validation
.. date: 2017-04-20 07:04:10 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

**Cross-validation**, sometimes called **rotation estimation**, is a [model validation][809c5010] technique for assessing how the results of a statistical analysis will generalize to an independent data set. It is mainly used in settings where the goal is prediction, and one wants to estimate how accurately a predictive model will perform in practice. In a prediction problem, a model is usually given a dataset of known data on which training is run (training dataset), and a dataset of unknown data (or first seen data) against which the model is tested (testing dataset).[4] The goal of cross validation is to define a dataset to "test" the model in the training phase (i.e., the validation dataset), in order to limit problems like overfitting, give an insight on how the model will generalize to an independent dataset (i.e., an unknown dataset, for instance from a real problem), etc.

  [809c5010]: https://en.wikipedia.org/wiki/Model_validation "Model Validation"

One round of cross-validation involves partitioning a sample of data into complementary subsets, performing the analysis on one subset (called the training set), and validating the analysis on the other subset (called the validation set or testing set). To reduce variability, multiple rounds of cross-validation are performed using different partitions, and the validation results are averaged over the rounds.

One of the main reasons for using cross-validation instead of using the conventional validation (e.g. partitioning the data set into two sets of 70% for training and 30% for test) is that there is not enough data available to partition it into separate training and test sets without losing significant modelling or testing capability. In these cases, a fair way to properly estimate model prediction performance is to use cross-validation as a powerful general technique.    

In summary, cross-validation combines (averages) measures of fit (prediction error) to derive a more accurate estimate of model prediction performance.    


## Common types of cross-validation    
Two types of cross-validation can be distinguished, exhaustive and non-exhaustive cross-validation.

### Exhaustive cross-validation      
Exhaustive cross-validation methods are cross-validation methods which learn and test on all possible ways to divide the original sample into a training and a validation set.

#### Leave-p-out cross-validation     
Leave-p-out cross-validation (LpO CV) involves using p observations as the validation set and the remaining observations as the training set. This is repeated on all ways to cut the original sample on a validation set of p observations and a training set.

LpO cross-validation requires training and validating the model \\( C_{n}^{p} \\) \\( C_{n}^{p} \\) times, where n is the number of observations in the original sample, and where \\( C_{n}^{p} \\) is the [binomial coefficient][6fb89f77]. For \\( p \\) > 1 and for even moderately large \\( n \\), LpO CV can become computationally infeasible. For example, with \\( n \\) = 100 and \\( p \\) = 30 = 30 percent of 100 (as suggested above), \\( C_{100}^{30} \approx 3\times 10^{25} \\).  

  [6fb89f77]: https://en.wikipedia.org/wiki/Binomial_coefficient "Binomial Coefficient"

#### Leave-one-out cross-validation      
Leave-one-out cross-validation (LOOCV) is a particular case of leave-p-out cross-validation with \\( p \\) = 1. The process looks similar to [jackknife][4074455a], however with cross-validation you compute a statistic on the left-out sample(s), while with jackknifing you compute a statistic from the kept samples only.

  [4074455a]: https://en.wikipedia.org/wiki/Jackknife_resampling "Jackknife Resampling"

LOO cross-validation does not have the same problem of excessive compute time as general LpO cross-validation because \\( C_{n}^{1}=n \\).

### Non-exhaustive cross-validation       
Non-exhaustive cross validation methods do not compute all ways of splitting the original sample. Those methods are approximations of leave-p-out cross-validation.

#### k-fold cross-validation      
In k-fold cross-validation, the original sample is randomly partitioned into k equal sized subsamples. Of the \\( k \\) subsamples, a single subsample is retained as the validation data for testing the model, and the remaining \\( k \\) − 1 subsamples are used as training data. The cross-validation process is then repeated \\( k \\) times (the folds), with each of the k subsamples used exactly once as the validation data. The \\( k \\) results from the folds can then be averaged to produce a single estimation. The advantage of this method over repeated random sub-sampling (see below) is that all observations are used for both training and validation, and each observation is used for validation exactly once. 10-fold cross-validation is commonly used, but in general k remains an unfixed parameter.

For example, setting \\( k \\) = 2 results in 2-fold cross-validation. In 2-fold cross-validation, we randomly shuffle the dataset into two sets \\( d_0 \\) and \\( d_1 \\), so that both sets are equal size (this is usually implemented by shuffling the data array and then splitting it in two). We then train on \\( d_0 \\) and test on \\( d_1 \\), followed by training on \\( d_1 \\) and testing on \\( d_0 \\).

When \\( k \\) = \\( n \\) (the number of observations), the k-fold cross-validation is exactly the leave-one-out cross-validation.

In stratified k-fold cross-validation, the folds are selected so that the mean response value is approximately equal in all the folds. In the case of a dichotomous classification, this means that each fold contains roughly the same proportions of the two types of class labels.

#### Holdout method      
In the holdout method, we randomly assign data points to two sets \\( d_0 \\) and \\( d_1 \\), usually called the training set and the test set, respectively. The size of each of the sets is arbitrary although typically the test set is smaller than the training set. We then train on \\( d_0 \\) and test on \\( d_1 \\).

In typical cross-validation, multiple runs are aggregated together; in contrast, the holdout method, in isolation, involves a single run. While the holdout method can be framed as "the simplest kind of cross-validation", many sources instead classify holdout as a type of simple validation, rather than a simple or degenerate form of cross-validation.

#### Repeated random sub-sampling validation   
This method, also known as Monte Carlo cross-validation, randomly splits the dataset into training and validation data. For each such split, the model is fit to the training data, and predictive accuracy is assessed using the validation data. The results are then averaged over the splits. The advantage of this method (over k-fold cross validation) is that the proportion of the training/validation split is not dependent on the number of iterations (folds). The disadvantage of this method is that some observations may never be selected in the validation subsample, whereas others may be selected more than once. In other words, validation subsets may overlap. This method also exhibits Monte Carlo variation, meaning that the results will vary if the analysis is repeated with different random splits.

As the number of random splits approaches infinity, the result of repeated random sub-sampling validation tends towards that of leave-p-out cross-validation.

In a stratified variant of this approach, the random samples are generated in such a way that the mean response value (i.e. the dependent variable in the regression) is equal in the training and testing sets. This is particularly useful if the responses are dichotomous with an unbalanced representation of the two response values in the data.
