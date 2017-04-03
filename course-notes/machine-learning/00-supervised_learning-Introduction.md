<!--
.. title: Supervised Learning - Introduction
.. slug: 00-supervised_learning-introduction
.. date: 2017-04-03 14:25:23 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


# Supervised Learning and Classifications

**Supervised learning** is the machine learning task of inferring a function from labeled _training data_. The training data consist of a set of training examples. In supervised learning, each example is a _pair_ consisting of an input object (typically a vector) and a desired output value (also called the _supervisory signal_). A supervised learning algorithm analyzes the training data and produces an inferred function, which can be used for mapping new examples. An optimal scenario will allow for the algorithm to correctly determine the class labels for unseen instances. This requires the learning algorithm to generalize from the training data to unseen situations in a "reasonable" way (see [inductive bias][b08c9d94]).


  [b08c9d94]: https://en.wikipedia.org/wiki/Inductive_bias "Inductive Bias"

The parallel task in human and animal psychology is often referred to as [concept learning][a7be7e7e].

  [a7be7e7e]: https://en.wikipedia.org/wiki/Concept_learning "Concept Learning"

## Overview       
In order to solve a given problem of supervised learning, one has to perform the following steps:

1. Determine the type of training examples. Before doing anything else, the user should decide what kind of data is to be used as a training set. In the case of handwriting analysis, for example, this might be a single handwritten character, an entire handwritten word, or an entire line of handwriting.      
2. Gather a training set. The training set needs to be representative of the real-world use of the function. Thus, a set of input objects is gathered and corresponding outputs are also gathered, either from human experts or from measurements.      
3. Determine the input feature representation of the learned function. The accuracy of the learned function depends strongly on how the input object is represented. Typically, the input object is transformed into a feature vector, which contains a number of features that are descriptive of the object. The number of features should not be too large, because of the [curse of dimensionality][cfa655ec]; but should contain enough information to accurately predict the output.       
4. Determine the structure of the learned function and corresponding learning algorithm. For example, the engineer may choose to use [support vector machines][b692aeef] or [decision trees][9297532d].         
5. Complete the design. Run the learning algorithm on the gathered training set. Some supervised learning algorithms require the user to determine certain control parameters. These parameters may be adjusted by optimizing performance on a subset (called a validation set) of the training set, or via [cross-validation][376db099].          
6. Evaluate the accuracy of the learned function. After parameter adjustment and learning, the performance of the resulting function should be measured on a test set that is separate from the training set.          
7. A wide range of supervised learning algorithms are available, each with its strengths and weaknesses. There is no single learning algorithm that works best on all supervised learning problems (see the [No free lunch theorem][6f02ac4a]).     
8.

  [cfa655ec]: https://en.wikipedia.org/wiki/Curse_of_dimensionality "Curse of Dimensionality"
  [b692aeef]: https://en.wikipedia.org/wiki/Support_vector_machine "Support Vector Machine (SVM)"
  [9297532d]: https://en.wikipedia.org/wiki/Decision_tree_learning "Decision Tree"
  [376db099]: https://en.wikipedia.org/wiki/Cross-validation_(statistics) "Cross Validation"
  [6f02ac4a]: https://en.wikipedia.org/wiki/No_free_lunch_in_search_and_optimization "No Free Lunch Theorem"

There are four major issues to consider in supervised learning:

### Bias-variance tradeoff       

        _Main article: [Bias-variance dilemma][0b76054f]_     

A first issue is the tradeoff between bias and variance. Imagine that we have available several different, but equally good, training data sets. A learning algorithm is biased for a particular input \\( x \\) if, when trained on each of these data sets, it is systematically incorrect when predicting the correct output for \\( x \\) . A learning algorithm has high variance for a particular input \\( x \\) if it predicts different output values when trained on different training sets. The prediction error of a learned classifier is related to the sum of the bias and the variance of the learning algorithm. Generally, there is a tradeoff between bias and variance. A learning algorithm with low bias must be "flexible" so that it can fit the data well. But if the learning algorithm is too flexible, it will fit each training data set differently, and hence have high variance. A key aspect of many supervised learning methods is that they are able to adjust this tradeoff between bias and variance (either automatically or by providing a bias/variance parameter that the user can adjust).

  [0b76054f]: https://en.wikipedia.org/wiki/Bias-variance_dilemma "Bias Variance Dilemma"

###  Function complexity and amount of training data       

The second issue is the amount of training data available relative to the complexity of the "true" function (classifier or regression function). If the true function is simple, then an "inflexible" learning algorithm with high bias and low variance will be able to learn it from a small amount of data. But if the true function is highly complex (e.g., because it involves complex interactions among many different input features and behaves differently in different parts of the input space), then the function will only be learnable from a very large amount of training data and using a "flexible" learning algorithm with low bias and high variance.

### Dimensionality of the input space       

A third issue is the dimensionality of the input space. If the input feature vectors have very high dimension, the learning problem can be difficult even if the true function only depends on a small number of those features. This is because the many "extra" dimensions can confuse the learning algorithm and cause it to have high variance. Hence, high input dimensionality typically requires tuning the classifier to have low variance and high bias. In practice, if the engineer can manually remove irrelevant features from the input data, this is likely to improve the accuracy of the learned function. In addition, there are many algorithms for feature selection that seek to identify the relevant features and discard the irrelevant ones. This is an instance of the more general strategy of dimensionality reduction, which seeks to map the input data into a lower-dimensional space prior to running the supervised learning algorithm.

###  Noise in the output values    

A fourth issue is the degree of noise in the desired output values (the supervisory target variables). If the desired output values are often incorrect (because of human error or sensor errors), then the learning algorithm should not attempt to find a function that exactly matches the training examples. Attempting to fit the data too carefully leads to overfitting. You can overfit even when there are no measurement errors (stochastic noise) if the function you are trying to learn is too complex for your learning model. In such a situation that part of the target function that cannot be modeled "corrupts" your training data - this phenomenon has been called deterministic noise. When either type of noise is present, it is better to go with a higher bias, lower variance estimator.

In practice, there are several approaches to alleviate noise in the output values such as early stopping to prevent overfitting as well as detecting and removing the noisy training examples prior to training the supervised learning algorithm. There are several algorithms that identify noisy training examples and removing the suspected noisy training examples prior to training has decreased generalization error with statistical significance.   

###  Other factors to consider (important)     

Other factors to consider when choosing and applying a learning algorithm include the following:

1. Heterogeneity of the data. If the feature vectors include features of many different kinds (discrete, discrete ordered, counts, continuous values), some algorithms are easier to apply than others. Many algorithms, including Support Vector Machines, linear regression, logistic regression, neural networks, and nearest neighbor methods, require that the input features be numerical and scaled to similar ranges (e.g., to the [-1,1] interval). Methods that employ a distance function, such as nearest neighbor methods and support vector machines with Gaussian kernels, are particularly sensitive to this. An advantage of decision trees is that they easily handle heterogeneous data.       
2. Redundancy in the data. If the input features contain redundant information (e.g., highly correlated features), some learning algorithms (e.g., linear regression, logistic regression, and distance based methods) will perform poorly because of numerical instabilities. These problems can often be solved by imposing some form of regularization.       
3. Presence of interactions and non-linearities. If each of the features makes an independent contribution to the output, then algorithms based on linear functions (e.g., linear regression, logistic regression, Support Vector Machines, naive Bayes) and distance functions (e.g., nearest neighbor methods, support vector machines with Gaussian kernels) generally perform well. However, if there are complex interactions among features, then algorithms such as decision trees and neural networks work better, because they are specifically designed to discover these interactions. Linear methods can also be applied, but the engineer must manually specify the interactions when using them.     
4. When considering a new application, the engineer can compare multiple learning algorithms and experimentally determine which one works best on the problem at hand (see cross validation). Tuning the performance of a learning algorithm can be very time-consuming. Given fixed resources, it is often better to spend more time collecting additional training data and more informative features than it is to spend extra time tuning the learning algorithms.       
5.

The most widely used learning algorithms are [Support Vector Machines][b692aeef], [linear regression][2cc2fe71], [logistic regression][377b1b10], [naive Bayes][3224e296], [linear discriminant analysis][eea42f1c], [decision trees][9297532d], [k-nearest neighbor algorithm][ddd94e19], and [Neural Networks][7f732413] ([Multilayer perceptron][c702143f]).

  [2cc2fe71]: https://en.wikipedia.org/wiki/Linear_regression "Linear Regression"
  [377b1b10]: https://en.wikipedia.org/wiki/Logistic_regression "Logistic Regression"
  [3224e296]: https://en.wikipedia.org/wiki/Naive_Bayes_classifier "Naive Bayes"
  [eea42f1c]: https://en.wikipedia.org/wiki/Linear_discriminant_analysis "Linear Discriminant Analysis"
  [ddd94e19]: https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm "K-Nearest Neighbors Algorithm"
  [7f732413]: https://en.wikipedia.org/wiki/Artificial_neural_network "Artificial Neural Network"
  [c702143f]: https://en.wikipedia.org/wiki/Multilayer_perceptron "Multilayer Perceptron"


In Machine learning, it is very important to train and test two different sets of data.  If we don't do that we could overfit the data.  We could think we know better what is actually going on than we actually know.

Usually when we get a dataset, we use 90% of the data as training data, and save 10% as testing data. When we do reporting, we use the results from the test data, as it more closely resemble real life application / tests on the algorithm.

## Overfitting and Underfitting    
In statistics and machine learning, one of the most common tasks is to fit a "model" to a set of training data, so as to be able to make reliable predictions on general untrained data.

In **overfitting**, a statistical model describes random error or noise instead of the underlying relationship. Overfitting occurs when a model is excessively complex, such as having too many parameters relative to the number of observations. A model that has been overfit has poor predictive performance, as it overreacts to minor fluctuations in the training data.

**Underfitting** occurs when a statistical model or machine learning algorithm cannot capture the underlying trend of the data. Underfitting would occur, for example, when fitting a linear model to non-linear data. Such a model would have poor predictive performance.

The possibility of overfitting exists because the criterion used for training the model is not the same as the criterion used to judge the efficacy of a model. In particular, a model is typically trained by maximizing its performance on some set of training data. However, its efficacy is determined not by its performance on the training data but by its ability to perform well on unseen data. Overfitting occurs when a model begins to "memorize" training data rather than "learning" to generalize from trend. As an extreme example, if the number of parameters is the same as or greater than the number of observations, a simple model or learning process can perfectly predict the training data simply by memorizing the training data in its entirety, but such a model will typically fail drastically when making predictions about new or unseen data, since the simple model has not learned to generalize at all.

The potential for overfitting depends not only on the number of parameters and data but also the conformability of the model structure with the data shape, and the magnitude of model error compared to the expected level of noise or error in the data.

Even when the fitted model does not have an excessive number of parameters, it is to be expected that the fitted relationship will appear to perform less well on a new data set than on the data set used for fitting. In particular, the value of the coefficient of determination will shrink relative to the original training data.

In order to avoid overfitting, it is necessary to use additional techniques (e.g. [cross-validation][4fd5c9b0], [regularization][984c448d], [early stopping][bec64cd1], [pruning][7eba0d3e], [Bayesian priors][ed081a86] on parameters or [model comparison][f8369d08]), that can indicate when further training is not resulting in better generalization. The basis of some techniques is either (1) to explicitly penalize overly complex models, or (2) to test the model's ability to generalize by evaluating its performance on a set of data not used for training, which is assumed to approximate the typical unseen data that a model will encounter.

  [4fd5c9b0]: https://en.wikipedia.org/wiki/Cross-validation_(statistics) "Cross Validation"
  [984c448d]: https://en.wikipedia.org/wiki/Regularization_(mathematics) "Regularization"
  [bec64cd1]: https://en.wikipedia.org/wiki/Early_stopping "Early Stopping"
  [7eba0d3e]: https://en.wikipedia.org/wiki/Pruning_(algorithm) "Pruning"
  [ed081a86]: https://en.wikipedia.org/wiki/Prior_distribution "Bayesian Prior"
  [f8369d08]: https://en.wikipedia.org/wiki/Bayesian_model_comparison "Bayesian Model Comparision"

A good analogy for the overfitting problem is imagine a baby trying to learn what is a window or what is not a window, we start to show him windows and he detects at an initial phase that all windows have glasses, and a frame and you can look outside, some of them may be opened. If we keep showing the same windows the baby may also falsely deduce that all windows are green, and that all green frames are windows. Thus overfitting the problem.
