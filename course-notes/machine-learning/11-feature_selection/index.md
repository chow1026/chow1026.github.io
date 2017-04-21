<!--
.. title: Feature Selection
.. slug: 11-feature_selection
.. date: 2017-04-20 06:59:28 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

In machine learning and statistics, **feature selection**, also known as **variable selection**, **attribute selection** or **variable subset selection**, is the process of selecting a subset of relevant features (variables, predictors) for use in model construction. Feature selection techniques are used for four reasons:      

- simplification of models to make them easier to interpret by researchers/users,     
- shorter training times,      
- to avoid the [curse of dimensionality][0f49ab9b],      
- enhanced generalization by reducing overfitting (formally, reduction of variance)      

  [0f49ab9b]: https://en.wikipedia.org/wiki/Curse_of_dimensionality "Curse of Dimensionality"


The central premise when using a feature selection technique is that the data contains many features that are either _redundant_ or _irrelevant_, and can thus be removed without incurring much loss of information. _Redundant_ or _irrelevant_ features are two distinct notions, since one relevant feature may be redundant in the presence of another relevant feature with which it is strongly correlated.

Feature selection techniques should be distinguished from [feature extraction][c5eb3156]. Feature extraction creates new features from functions of the original features, whereas feature selection returns a subset of the features. Feature selection techniques are often used in domains where there are many features and comparatively few samples (or data points). Archetypal cases for the application of feature selection include the analysis of written texts and DNA microarray data, where there are many thousands of features, and a few tens to hundreds of samples.

  [c5eb3156]: https://en.wikipedia.org/wiki/Feature_extraction "Feature Extraction"

## Introduction    
A feature selection algorithm can be seen as the combination of a search technique for proposing new feature subsets, along with an evaluation measure which scores the different feature subsets. The simplest algorithm is to test each possible subset of features finding the one which minimizes the error rate. This is an exhaustive search of the space, and is computationally intractable for all but the smallest of feature sets. The choice of evaluation metric heavily influences the algorithm, and it is these evaluation metrics which distinguish between the three main categories of feature selection algorithms: wrappers, filters and embedded methods.     

- Wrapper methods use a predictive model to score feature subsets. Each new subset is used to train a model, which is tested on a hold-out set. Counting the number of mistakes made on that hold-out set (the error rate of the model) gives the score for that subset. As wrapper methods train a new model for each subset, they are very computationally intensive, but usually provide the best performing feature set for that particular type of model.      
- Filter methods use a proxy measure instead of the error rate to score a feature subset. This measure is chosen to be fast to compute, while still capturing the usefulness of the feature set. Common measures include the [mutual information][9394457f], the [pointwise mutual information][861467d1], [Pearson product-moment correlation coefficient][f32092b8], inter/intra class distance or the scores of [significance tests][3c05df64] for each class/feature combinations.  Filters are usually less computationally intensive than wrappers, but they produce a feature set which is not tuned to a specific type of predictive model. This lack of tuning means a feature set from a filter is more general than the set from a wrapper, usually giving lower prediction performance than a wrapper. However the feature set doesn't contain the assumptions of a prediction model, and so is more useful for exposing the relationships between the features. Many filters provide a feature ranking rather than an explicit best feature subset, and the cut off point in the ranking is chosen via [cross-validation][7724ae1a]. Filter methods have also been used as a preprocessing step for wrapper methods, allowing a wrapper to be used on larger problems.      
- Embedded methods are a catch-all group of techniques which perform feature selection as part of the model construction process. The exemplar of this approach is the [LASSO][8c14f16c] method for constructing a linear model, which penalizes the regression coefficients with an L1 penalty, shrinking many of them to zero. Any features which have non-zero regression coefficients are 'selected' by the [LASSO][8c14f16c] algorithm. Improvements to the [LASSO][8c14f16c] include Bolasso which bootstraps samples, and FeaLect which scores all the features based on combinatorial analysis of regression coefficients. One other popular approach is the Recursive Feature Elimination algorithm, commonly used with Support Vector Machines to repeatedly construct a model and remove features with low weights. These approaches tend to be between filters and wrappers in terms of computational complexity.       

  [9394457f]: https://en.wikipedia.org/wiki/Mutual_information "Mutual Information"
  [861467d1]: https://en.wikipedia.org/wiki/Pointwise_mutual_information "Pointwise Mutual Information"
  [f32092b8]: https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient "Pearson Product Moment Correlation Coefficient"
  [3c05df64]: https://en.wikipedia.org/wiki/Statistical_hypothesis_testing "Significance Test"
  [7724ae1a]: https://en.wikipedia.org/wiki/Cross-validation_(statistics) "Cross Validation"
  [8c14f16c]: https://en.wikipedia.org/wiki/Lasso_(statistics) "Lasso"


In traditional statistics, the most popular form of feature selection is [stepwise regression][fe987ecc], which is a wrapper technique. It is a [greedy algorithm][e937cee8] that adds the best feature (or deletes the worst feature) at each round. The main control issue is deciding when to stop the algorithm. In machine learning, this is typically done by [cross-validation][7724ae1a]. In statistics, some criteria are optimized. This leads to the inherent problem of nesting. More robust methods have been explored, such as [branch and bound][c4913144] and piecewise linear network.

  [fe987ecc]: https://en.wikipedia.org/wiki/Stepwise_regression "Stepwise Regression"
  [e937cee8]: https://en.wikipedia.org/wiki/Greedy_algorithm "Greedy Algorithm"
  [c4913144]: https://en.wikipedia.org/wiki/Branch_and_bound "Branch and Bound"

## Subset selection      
Subset selection evaluates a subset of features as a group for suitability. Subset selection algorithms can be broken up into Wrappers, Filters and Embedded. Wrappers use a search algorithm to search through the space of possible features and evaluate each subset by running a model on the subset. Wrappers can be computationally expensive and have a risk of over fitting to the model. Filters are similar to Wrappers in the search approach, but instead of evaluating against a model, a simpler filter is evaluated. Embedded techniques are embedded in and specific to a model.

Many popular search approaches use [greedy hill climbing][747aa0d3], which iteratively evaluates a candidate subset of features, then modifies the subset and evaluates if the new subset is an improvement over the old. Evaluation of the subsets requires a scoring metric that grades a subset of features. Exhaustive search is generally impractical, so at some implementor (or operator) defined stopping point, the subset of features with the highest score discovered up to that point is selected as the satisfactory feature subset. The stopping criterion varies by algorithm; possible criteria include: a subset score exceeds a threshold, a program's maximum allowed run time has been surpassed, etc.

  [747aa0d3]: https://en.wikipedia.org/wiki/Hill_climbing "Hill Climbing"

Alternative search-based techniques are based on targeted projection pursuit which finds low-dimensional projections of the data that score highly: the features that have the largest projections in the lower-dimensional space are then selected.

Search approaches include:       

- Exhaustive    
- [Best first][660a5cc0]       
- [Simulated annealing][4d72a9ca]       
- [Genetic algorithm][89177edb]       
- Greedy forward selection        
- Greedy backward elimination              
- [Particle swarm optimization][8435a922]         
- [Targeted projection pursuit][0a3776cb]        
- Scatter Search        
- [Variable Neighborhood Search][5c7c42ac]      

  [660a5cc0]: https://en.wikipedia.org/wiki/Best-first_search "Best First"
  [4d72a9ca]: https://en.wikipedia.org/wiki/Simulated_annealing "Simulated Annealing"
  [89177edb]: https://en.wikipedia.org/wiki/Genetic_algorithm "Genetic Algorithm"
  [8435a922]: https://en.wikipedia.org/wiki/Particle_swarm_optimization "Particle Swarm Optimization"
  [0a3776cb]: https://en.wikipedia.org/wiki/Targeted_projection_pursuit "Targeted Projection Pursuit"
  [5c7c42ac]: https://en.wikipedia.org/wiki/Variable_Neighborhood_Search "Variable Neighborhood Search"

Two popular filter metrics for classification problems are [correlation][cc58bd13] and [mutual information][b06e4233], although neither are true metrics or 'distance measures' in the mathematical sense, since they fail to obey the triangle inequality and thus do not compute any actual 'distance' – they should rather be regarded as 'scores'. These scores are computed between a candidate feature (or set of features) and the desired output category. There are, however, true metrics that are a simple function of the mutual information;[15] see here.

  [cc58bd13]: https://en.wikipedia.org/wiki/Correlation "Correlation"
  [b06e4233]: https://en.wikipedia.org/wiki/Mutual_information "Mutual Information"

Other available filter metrics include:      

- Class separability       
    - Error probability      
    - Inter-class distance      
    - Probabilistic distance      
    - Entropy      
- Consistency-based feature selection      
- Correlation-based feature selection      
