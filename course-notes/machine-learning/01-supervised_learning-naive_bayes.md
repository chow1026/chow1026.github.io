<!--
.. title: Supervised Learning - Naive Bayes
.. slug: 01-supervised_learning-naive_bayes
.. date: 2017-03-28 11:34:18 UTC+08:00
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


# Naive Bayes Classifier / Algorithm    

In [machine learning][abfec984], naive Bayes classifiers are a family of simple [probabilistic classifier][16d45015]s based on applying [Bayes' theorem][12e12648] with strong (naive) [independence][6f57f0b5] assumptions between the features.

  [abfec984]: https://en.wikipedia.org/wiki/Machine_learning "Machine Learning"
  [16d45015]: https://en.wikipedia.org/wiki/Probabilistic_classification "Probabilistic Classifier"
  [12e12648]: https://en.wikipedia.org/wiki/Bayes%27_theorem "Bayes' Theorem"
  [6f57f0b5]: https://en.wikipedia.org/wiki/Independence_(probability_theory) "Independence Probability Theory"

Naive Bayes has been studied extensively since the 1950s. It was introduced under a different name into the text retrieval community in the early 1960s, and remains a popular (baseline) method for text categorization, the problem of judging documents as belonging to one category or the other (such as spam or legitimate, sports or politics, etc.) with word frequencies as the features. With appropriate pre-processing, it is competitive in this domain with more advanced methods including support vector machines. It also finds application in automatic medical diagnosis.

Naive Bayes classifiers are highly scalable, requiring a number of parameters linear in the number of variables (features/predictors) in a learning problem. [Maximum-likelihood training][a5404f35] can be done by evaluating a closed-form expression,[1]:718 which takes linear time, rather than by expensive iterative approximation as used for many other types of classifiers.

  [a5404f35]: https://en.wikipedia.org/wiki/Maximum_likelihood_estimation "Maximum Likelihood Training"

In the statistics and computer science literature, Naive Bayes models are known under a variety of names, including simple Bayes and independence Bayes.  All these names reference the use of Bayes' theorem in the classifier's decision rule, but naive Bayes is not (necessarily) a Bayesian method.

Despite their naive design and apparently oversimplified assumptions, naive Bayes classifiers have worked quite well in many complex real-world situations. In 2004, an analysis of the Bayesian classification problem showed that there are sound theoretical reasons for the apparently implausible efficacy of naive Bayes classifiers.  Still, a comprehensive comparison with other classification algorithms in 2006 showed that Bayes classification is outperformed by other approaches, such as [boosted trees][5b57bac3] or [random forests][2085bee1].  

  [5b57bac3]: https://en.wikipedia.org/wiki/Gradient_boosting#Gradient_tree_boosting "Boosted Trees"
  [2085bee1]: https://en.wikipedia.org/wiki/Random_forest "Random Forests"

An advantage of naive Bayes is that it only requires a small number of training data to estimate the parameters necessary for classification.  



## Bayes Rules:

Prior Probability * Test Evidence (in Probability) = Posterior Probability

Cancer Example:     
Prior Probabilities:
P(C) = 0.01  {Prior Cancer Probability is 1%}
\therefore P(NC) = 1 - P(C) = 0.99


Test Evidence, Sensitivity and Specificity Probabilities
Test Sensitivity, P(Pos|C) = 0.9
\therefore, P(Neg|C) = 1 - 0.9 = 0.1
Test specificity, P(Neg|NC) = 0.9
\therefore, P(Pos|NC) = 1 - 0.9 = 0.1

Joint Probability
P(C, Pos) = P(C) * P(Pos|C) = 0.009
P(NC, Pos) = P(NC) * P(Pos|NC) = 0.099

P(Pos) = P(C|Pos) + P(NC|Pos) = 0.009 + 0.099 = 0.108

Normalized Posterior Probability
P(C|Pos) = P(C, Pos) / P(Pos) =  0.009 / 0.108 = 0.0833
P(NC|Pos) = P(NC, Pos) / P(Pos) =  0.099 / 0.108 = 0.9167


Legends:
P(C) = Prior Cancer Probability, in this case 1%
P(NC) = Prior non-Cancer Probability, 1-P(C), in this case 99%
P(C, Pos) = Joint probability that one having cancer AND tested positive
P(NC, Pos) = Joint probability that one does not have cancer AND tested positive
P(C|Pos) => Posterior probability of having cancer given one is tested positive
P(NC|Pos) => Posterior probability of NOT having cancer given one is tested positive
P(Pos|C) => Test sensitivity, Probability of tested positive if one has cancer
P(Neg|NC) => Test specificity, Probability of tested negative if one has NO cancer.

## Common Usage     

Naive Bayes is a pretty good algorithm for text learning.  Naive Bayes is called "Naive" because it works with _words_ at various _length_, but ignores _word order_.    

## Pros:    
- Easy to implement      
- Simple and efficient to run      
- Big / Great feature spaces      


## Cons:
- It could break when phrases that encompasses multiple words that have distinctive meanings don't really work well.  For example Chicago Bulls will be interpreted as "Chicago" and "Bulls", but that's not what Chicago Bulls is.
