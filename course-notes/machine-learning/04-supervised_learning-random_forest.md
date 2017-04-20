<!--
.. title: Supervised Learning - Random Forest
.. slug: 05-supervised_learning-random_forest
.. date: 2017-04-04 14:22:30 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Random forests or random decision forests are an [ensemble learning][5001fde4] method for [classification][6ad8669a], regression and other tasks, that operate by constructing a multitude of [decision tree][53c4742d]s at training time and outputting the class that is the [mode][552ede8b] of the classes (classification) or mean prediction ([regression][3a484c39]) of the individual trees. Random decision forests correct for decision trees' habit of [overfitting][4064b7b2] to their training set.

  [5001fde4]: https://en.wikipedia.org/wiki/Ensemble_learning "Ensemble Learning"
  [552ede8b]: https://en.wikipedia.org/wiki/Mode_(statistics) "Mode (Statistics)"
  [6ad8669a]: https://en.wikipedia.org/wiki/Statistical_classification "Statistical Classification"
  [3a484c39]: https://en.wikipedia.org/wiki/Regression_analysis "Regression Analysis"
  [53c4742d]: https://en.wikipedia.org/wiki/Decision_tree_learning "Decision Tree Learning"
  [4064b7b2]: https://en.wikipedia.org/wiki/Overfitting "Overfitting"

The first algorithm for random decision forests was created by Tin Kam Ho using the [random subspace method][f787e2d1], which, in Ho's formulation, is a way to implement the "[stochastic discrimination][156d2781]" approach to classification proposed by Eugene Kleinberg.    

  [f787e2d1]: https://en.wikipedia.org/wiki/Random_subspace_method "Random Subspace"
  [156d2781]: https://en.wikipedia.org/w/index.php?title=Stochastic_discrimination&redirect=no "Stochastic Discrimination (Redirects to https://en.wikipedia.org/wiki/Statistical_classification)"

An extension of the algorithm was developed by Leo Breiman and Adele Cutler, and "Random Forests" is their trademark.  The extension combines Breiman's "[bagging][ff024e25]" idea and random selection of features, introduced first by Ho and later independently by Amit and Geman in order to construct a collection of decision trees with controlled variance.

  [ff024e25]: https://en.wikipedia.org/wiki/Bootstrap_aggregating "Bagging (Redirects to Bootstrap Aggregating)"


# History   
The general method of random decision forests was first proposed by Ho in 1995, who established that forests of trees splitting with oblique hyperplanes, if randomly restricted to be sensitive to only selected feature dimensions, can gain accuracy as they grow without suffering from overtraining. A subsequent work along the same lines  concluded that other splitting methods, as long as they are randomly forced to be insensitive to some feature dimensions, behave similarly. Note that this observation of a more complex classifier (a larger forest) getting more accurate nearly monotonically is in sharp contrast to the common belief that the complexity of a classifier can only grow to a certain level of accuracy before being hurt by overfitting. The explanation of the forest method's resistance to overtraining can be found in Kleinberg's theory of stochastic discrimination.  

The early development of Breiman's notion of random forests was influenced by the work of Amit and Geman  who introduced the idea of searching over a random subset of the available decisions when splitting a node, in the context of growing a single [tree][0fa3b5f7]. The idea of random subspace selection from Ho was also influential in the design of random forests. In this method a forest of trees is grown, and variation among the trees is introduced by projecting the training data into a randomly chosen [subspace][7e0f5c83] before fitting each tree or each node. Finally, the idea of randomized node optimization, where the decision at each node is selected by a randomized procedure, rather than a deterministic optimization was first introduced by Dietterich.

  [7e0f5c83]: https://en.wikipedia.org/wiki/Linear_subspace "Linear Subspace"
  [0fa3b5f7]: https://en.wikipedia.org/wiki/Decision_tree "Decision Tree"

The introduction of random forests proper was first made in a paper by Leo Breiman.  This paper describes a method of building a forest of uncorrelated trees using a CART like procedure, combined with randomized node optimization and bagging. In addition, this paper combines several ingredients, some previously known and some novel, which form the basis of the modern practice of random forests, in particular:       
- Using [out-of-bag error][0515ba73] as an estimate of the [generalization error][6a4b2cee].      
- Measuring variable importance through permutation.     

  [0515ba73]: https://en.wikipedia.org/wiki/Out-of-bag_error "Out of Bag Error"
  [6a4b2cee]: https://en.wikipedia.org/wiki/Generalization_error "Generalization Error"


The report also offers the first theoretical result for random forests in the form of a bound on the generalization error which depends on the strength of the trees in the forest and their correlation.


# Algorithm    
## Preliminaries: decision tree learning    
_Main article: [Decision tree learning][53c4742d]_      
Decision trees are a popular method for various machine learning tasks. Tree learning "come[s] closest to meeting the requirements for serving as an off-the-shelf procedure for data mining", say Hastie et al., because it is invariant under scaling and various other transformations of feature values, is robust to inclusion of irrelevant features, and produces inspectable models. However, they are seldom accurate.

In particular, trees that are grown very deep tend to learn highly irregular patterns: they overfit their training sets, i.e. [have low bias, but very high variance][fe0c227e]. Random forests are a way of averaging multiple deep decision trees, trained on different parts of the same training set, with the goal of reducing the variance.[3]:587–588 This comes at the expense of a small increase in the bias and some loss of interpretability, but generally greatly boosts the performance of the final model.

  [fe0c227e]: https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff "Bias Variance Tradeoff"


## Tree bagging    
_Main article: [Bootstrap aggregating][ff024e25]_       
The training algorithm for random forests applies the general technique of bootstrap aggregating, or bagging, to tree learners.  Given a training set \\(X = x1, ..., xn\\) with responses \\(Y = y1, ..., yn\\), bagging repeatedly (\\(B\\) times) selects a random sample with replacement of the training set and fits trees to these samples:

    For \\(b\\) = 1, ..., \\(B\\):      
        1. Sample, with replacement, \\(B\\) training examples from \\(X, Y\\); call these \\(Xb, Yb\\).       
        2. Train a decision or regression tree fb on \\(Xb, Yb\\).

After training, predictions for unseen samples \\(x'\\) can be made by averaging the predictions from all the individual regression trees on \\(x'\\):    
\\[
\hat f = \frac{1}{B}\;\sum_{b=1}^B\,f_b(x')
\\]     

or by taking the majority vote in the case of decision trees.

This bootstrapping procedure leads to better model performance because it [decreases the variance of the model, without increasing the bias][fe0c227e]. This means that while the predictions of a single tree are highly sensitive to noise in its training set, the average of many trees is not, as long as the trees are not correlated. Simply training many trees on a single training set would give strongly correlated trees (or even the same tree many times, if the training algorithm is deterministic); bootstrap sampling is a way of de-correlating the trees by showing them different training sets.

The number of samples/trees, \\(B\\), is a free parameter. Typically, a few hundred to several thousand trees are used, depending on the size and nature of the training set. An optimal number of trees \\(B\\) can be found using cross-validation, or by observing the [out-of-bag error][0515ba73]: the mean prediction error on each training sample \\(x_i\\), using only the trees that did not have \\(x_i\\) in their bootstrap sample.  The training and test error tend to level off after some number of trees have been fit.



## From bagging to random forests   
_Main article: [Random subspace method][f787e2d1]_     
The above procedure describes the original bagging algorithm for trees. Random forests differ in only one way from this general scheme: they use a modified tree learning algorithm that selects, at each candidate split in the learning process, a [random subset][f787e2d1] of the features. This process is sometimes called "feature bagging". The reason for doing this is the correlation of the trees in an ordinary bootstrap sample: if one or a few features are very strong predictors for the response variable (target output), these features will be selected in many of the \\(B\\) trees, causing them to become correlated. An analysis of how bagging and random subspace projection contribute to accuracy gains under different conditions is given by Ho.

Typically, for a classification problem with \\(p\\) features, \\(\sqrt{\,p}\\) (rounded down) features are used in each split.  For regression problems the inventors recommend \\(p\\)/3 (rounded down) with a minimum node size of 5 as the default.

## ExtraTrees    
Adding one further step of randomization yields extremely randomized trees, or ExtraTrees. These are trained using bagging and the random subspace method, like in an ordinary random forest, but additionally the top-down splitting in the tree learner is randomized. Instead of computing the locally optimal feature/split combination (based on, e.g., [information gain][b44bb27f] or the [Gini impurity][e76a563e]), for each feature under consideration, a random value is selected for the split. This value is selected from the feature's empirical range (in the tree's training set, i.e., the bootstrap sample).  

  [b44bb27f]: https://en.wikipedia.org/wiki/Information_gain "Information Gain"
  [e76a563e]: https://en.wikipedia.org/wiki/Gini_impurity "Gini Impurity"

# Other Useful Reference:
- [Random Tree][8723e963]    
- [Predictive Inference][d14effed]    


  [8723e963]: https://en.wikipedia.org/wiki/Random_tree "Random Tree"
  [d14effed]: https://en.wikipedia.org/wiki/Predictive_inference "Predictive Inference"
