<!--
.. title: Supervised Learning - Regression
.. slug: 06-supervised_learning-regression
.. date: 2017-04-20 06:19:50 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

In [statistical modeling][ef2a481e], **regression analysis** is a statistical process for estimating the relationships among variables. It includes many techniques for modeling and analyzing several variables, when the focus is on the relationship between a [dependent variable][cc83122f] and one or more [independent variables][2624b126] (or 'predictors'). More specifically, regression analysis helps one understand how the typical value of the dependent variable (or 'criterion variable') changes when any one of the independent variables is varied, while the other independent variables are held fixed. Most commonly, regression analysis estimates the [conditional expectation][d6719ab8] of the dependent variable given the independent variables – that is, the [average value][cf669dac] of the dependent variable when the independent variables are fixed. Less commonly, the focus is on a [quantile][edcebfb2], or other [location parameter][f38edbff] of the conditional distribution of the dependent variable given the independent variables. In all cases, the estimation target is a function of the independent variables called the **regression function**. In regression analysis, it is also of interest to characterize the variation of the dependent variable around the regression function which can be described by a [probability distribution][a539ee77]. A related but distinct approach is necessary condition analysis (NCA), which estimates the maximum (rather than average) value of the dependent variable for a given value of the independent variable (ceiling line rather than central line) in order to identify what value of the independent variable is necessary but not sufficient for a given value of the dependent variable.

  [ef2a481e]: https://en.wikipedia.org/wiki/Statistical_model "Statistical Model"
  [cc83122f]: https://en.wikipedia.org/wiki/Dependent_variable "Dependent Variable"
  [2624b126]: https://en.wikipedia.org/wiki/Independent_variable "Independent Variable"
  [d6719ab8]: https://en.wikipedia.org/wiki/Conditional_expectation "Conditional Expectation"
  [cf669dac]: https://en.wikipedia.org/wiki/Average_value "Average Value"
  [edcebfb2]: https://en.wikipedia.org/wiki/Quantile "Quantile"
  [f38edbff]: https://en.wikipedia.org/wiki/Location_parameter "Location Parameter"
  [a539ee77]: https://en.wikipedia.org/wiki/Probability_distribution "Probability Distribution"

Regression analysis is widely used for [prediction][c99ca2d9] and [forecasting][2d4533e1], where its use has substantial overlap with the field of machine learning. Regression analysis is also used to understand which among the independent variables are related to the dependent variable, and to explore the forms of these relationships. In restricted circumstances, regression analysis can be used to infer [causal relationships][69696463] between the independent and dependent variables. However this can lead to illusions or false relationships, so caution is advisable;[2] for example, [correlation does not imply causation][98bd98f9].

  [c99ca2d9]: https://en.wikipedia.org/wiki/Prediction "Prediction"
  [2d4533e1]: https://en.wikipedia.org/wiki/Forecasting "Forecasting"
  [69696463]: https://en.wikipedia.org/wiki/Causality "Casual Relationships"
  [98bd98f9]: https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation "Correlation is Not Causation"

Many techniques for carrying out regression analysis have been developed. Familiar methods such as [linear regression][ac959b6f] and [ordinary least squares][e1cbc07d] regression are [parametric][fe26df1a], in that the regression function is defined in terms of a finite number of unknown parameters that are estimated from the data. [Nonparametric regression][e0da2def] refers to techniques that allow the regression function to lie in a specified set of functions, which may be infinite-dimensional.

  [ac959b6f]: https://en.wikipedia.org/wiki/Linear_regression "Linear Regression"
  [e1cbc07d]: https://en.wikipedia.org/wiki/Ordinary_least_squares "Ordinary Least Squares"
  [fe26df1a]: https://en.wikipedia.org/wiki/Parametric_statistics "Parametric Statistics"
  [e0da2def]: https://en.wikipedia.org/wiki/Nonparametric_regression "Non-Parametric Regression"

The performance of regression analysis methods in practice depends on the form of the data generating process, and how it relates to the regression approach being used. Since the true form of the data-generating process is generally not known, regression analysis often depends to some extent on making assumptions about this process. These assumptions are sometimes testable if a sufficient quantity of data is available. Regression models for prediction are often useful even when the assumptions are moderately violated, although they may not perform optimally. However, in many applications, especially with small effects or questions of causality based on observational data, regression methods can give misleading results.


In a narrower sense, regression may refer specifically to the estimation of continuous response variables, as opposed to the discrete response variables used in [classification][fa3e5ee6]. The case of a continuous output variable may be more specifically referred to as **metric regression** to distinguish it from related problems.

  [fa3e5ee6]: https://en.wikipedia.org/wiki/Statistical_classification "Statistical Classification"



## Linear Regression      
In statistics, linear regression is an approach for modeling the relationship between a scalar dependent variable \\(y\\) and one or more explanatory variables (or independent variables) denoted \\(X\\). The case of one explanatory variable is called [simple linear regression][30eb36fa]. For more than one explanatory variable, the process is called _multiple linear regression_. (This term is distinct from [multivariate linear regression][a6893a05], where multiple correlated dependent variables are predicted, rather than a single scalar variable.)

  [30eb36fa]: https://en.wikipedia.org/wiki/Simple_linear_regression "Simple Linear Regression"
  [a6893a05]: https://en.wikipedia.org/wiki/General_linear_model "Multivariate Regression"

In linear regression, the relationships are modeled using [linear predictor functions][67d44f5e] whose unknown model parameters are [estimated][6de9e713] from the data. Such models are called [linear models][7e424994]. Most commonly, the [conditional][0e718466] mean of \\(y\\) given the value of \\(X\\) is assumed to be an [affine function][2b509f2b] of \\(X\\); less commonly, the [median][280b184a] or some other quantile of the conditional distribution of \\(y\\) given \\(X\\) is expressed as a linear function of \\(X\\). Like all forms of regression analysis, linear regression focuses on the [conditional probability distribution][15b457ef] of \\(y\\) given \\(X\\), rather than on the [joint probability distribution][56dd0deb] of \\(y\\) and \\(X\\), which is the domain of [multivariate analysis][16dfa0cd].

  [67d44f5e]: https://en.wikipedia.org/wiki/Linear_predictor_function "Linear Predictor Function"
  [6de9e713]: https://en.wikipedia.org/wiki/Estimation_theory "Estimation Theory"
  [7e424994]: https://en.wikipedia.org/wiki/Linear_model "Linear Model"
  [0e718466]: https://en.wikipedia.org/wiki/Conditional_expectation "Conditional Expectation"
  [2b509f2b]: https://en.wikipedia.org/wiki/Affine_transformation "Affine Transformation"
  [280b184a]: https://en.wikipedia.org/wiki/Median "Median"
  [15b457ef]: https://en.wikipedia.org/wiki/Conditional_probability_distribution "Conditional Probability Distribution"
  [56dd0deb]: https://en.wikipedia.org/wiki/Joint_probability_distribution "Joint Probability Distribution"
  [16dfa0cd]: https://en.wikipedia.org/wiki/Multivariate_analysis "Multivariate Analysis"

Linear regression was the first type of regression analysis to be studied rigorously, and to be used extensively in practical applications. This is because models which depend linearly on their unknown parameters are easier to fit than models which are non-linearly related to their parameters and because the statistical properties of the resulting estimators are easier to determine.

Linear regression has many practical uses. Most applications fall into one of the following two broad categories:

- If the goal is prediction, or forecasting, or error reduction, linear regression can be used to fit a predictive model to an observed data set of \\(y\\) and \\(X\\) values. After developing such a model, if an additional value of \\(X\\) is then given without its accompanying value of \\(y\\), the fitted model can be used to make a prediction of the value of \\(y\\).         
- Given a variable \\(y\\) and a number of variables \\(X_1, \, \ldots, \, X_p \\) that may be related to \\(y\\), linear regression analysis can be applied to quantify the strength of the relationship between \\(y\\) and the \\(X_j\\), to assess which \\(X_j\\) may have no relationship with \\(y\\) at all, and to identify which subsets of the \\(X_j\\) contain redundant information about \\(y\\).        


Linear regression models are often fitted using the [least squares][64ab1652] approach, but they may also be fitted in other ways, such as by minimizing the "lack of fit" in some other [norm][ee1215a7] (as with [least absolute deviations][4df1e406] regression), or by minimizing a penalized version of the least squares [loss function][868b4937] as in [ridge regression][f9b30262] (L2-norm penalty) and [lasso][77862f34] (L1-norm penalty). Conversely, the least squares approach can be used to fit models that are not linear models. Thus, although the terms "least squares" and "linear model" are closely linked, they are not synonymous.

  [64ab1652]: https://en.wikipedia.org/wiki/Least_squares "Least Square"
  [ee1215a7]: https://en.wikipedia.org/wiki/Norm_(mathematics) "Mathematical Norm"
  [4df1e406]: https://en.wikipedia.org/wiki/Least_absolute_deviations "Least Absolute Deviation"
  [868b4937]: https://en.wikipedia.org/wiki/Loss_function "Loss Function"
  [f9b30262]: https://en.wikipedia.org/wiki/Ridge_regression "Ridge Regression"
  [77862f34]: https://en.wikipedia.org/wiki/Lasso_(statistics) "Lasso"

### Introduction     

Given a data set
\\(  \left\\{y_{i},   \, x_{i1}, \, \ldots, \,   x_{ip}  \right\\} \_{i=0}^{n} \\)
of  \\( n \\) statistical units, a linear regression model assumes that the relationship between the dependent variable \\( y_{i} \\) and the _p-vector_ of regressors \\( x_{i} \\) is linear. This relationship is modeled through a disturbance term or error variable \\( \epsilon_i \\)— an unobserved random variable that adds noise to the linear relationship between the dependent variable and regressors.      

Thus the model takes the form
\\[ y_{i} = \beta \_{0}1 + \beta \_{1}x \_{i1} + \cdots + \beta \_{p} x \_{ip} + \varepsilon \_{i} = \mathbf{x} \_{i}^{ \top }{\boldsymbol{\beta}} + \varepsilon \_{i},\qquad i=1,\ldots ,n,   
\\]  

where T denotes the transpose, so that \\( \mathbf{x} \_{i}^{ \top }{\boldsymbol{\beta}} \\) is the inner product between vectors \\( \mathbf{x} \_{i} \\) and \\( \boldsymbol{\beta} \\).

### Assumptions    

Standard linear regression models with standard estimation techniques make a number of assumptions about the predictor variables, the response variables and their relationship. Numerous extensions have been developed that allow each of these assumptions to be relaxed (i.e. reduced to a weaker form), and in some cases eliminated entirely. Some methods are general enough that they can relax multiple assumptions at once, and in other cases this can be achieved by combining different extensions. Generally these extensions make the estimation procedure more complex and time-consuming, and may also require more data in order to produce an equally precise model.       

The following are the major assumptions made by standard linear regression models with standard estimation techniques (e.g. [ordinary least squares][e1cbc07d]):        

- **Weak exogeneity**. This essentially means that the predictor variables x can be treated as fixed values, rather than [random variables][0b4621a8]. This means, for example, that the predictor variables are assumed to be error-free—that is, not contaminated with measurement errors. Although this assumption is not realistic in many settings, dropping it leads to significantly more difficult [errors-in-variables models][dfa746ee].      
- **Linearity**. This means that the mean of the response variable is a [linear combination][79eab8a9] of the parameters (regression coefficients) and the predictor variables. Note that this assumption is much less restrictive than it may at first seem. Because the predictor variables are treated as fixed values (see above), linearity is really only a restriction on the parameters. The predictor variables themselves can be arbitrarily transformed, and in fact multiple copies of the same underlying predictor variable can be added, each one transformed differently. This trick is used, for example, in [polynomial regression][edf39121], which uses linear regression to fit the response variable as an arbitrary [polynomial][aa8a90da] function (up to a given rank) of a predictor variable. This makes linear regression an extremely powerful inference method. In fact, models such as polynomial regression are often "too powerful", in that they tend to overfit the data. As a result, some kind of regularization must typically be used to prevent unreasonable solutions coming out of the estimation process. Common examples are [ridge regression][f9b30262] and [lasso regression][dc7b7ef9]. [Bayesian linear regression][9703face] can also be used, which by its nature is more or less immune to the problem of overfitting. (In fact, [ridge regression][f9b30262] and [lasso regression][dc7b7ef9] can both be viewed as special cases of Bayesian linear regression, with particular types of prior distributions placed on the regression coefficients.)       
- **Constant variance** (a.k.a. **[homoscedasticity][ec6ca2ef]**). This means that different response variables have the same variance in their errors, regardless of the values of the predictor variables. In practice this assumption is invalid (i.e. the errors are heteroscedastic) if the response variables can vary over a wide scale. In order to determine for heterogeneous error variance, or when a pattern of residuals violates model assumptions of homoscedasticity (error is equally variable around the 'best-fitting line' for all points of x), it is prudent to look for a "fanning effect" between residual error and predicted values. This is to say there will be a systematic change in the absolute or squared residuals when plotted against the predicting outcome. Error will not be evenly distributed across the regression line. Heteroscedasticity will result in the averaging over of distinguishable variances around the points to get a single variance that is inaccurately representing all the variances of the line. In effect, residuals appear clustered and spread apart on their predicted plots for larger and smaller values for points along the linear regression line, and the mean squared error for the model will be wrong. Typically, for example, a response variable whose mean is large will have a greater variance than one whose mean is small. For example, a given person whose income is predicted to be \$100,000 may easily have an actual income of \$80,000 or \$120,000 (a standard deviation of around \$20,000), while another person with a predicted income of \$10,000 is unlikely to have the same \$20,000 standard deviation, which would imply their actual income would vary anywhere between -\$10,000 and \$30,000. (In fact, as this shows, in many cases—often the same cases where the assumption of normally distributed errors fails—the variance or standard deviation should be predicted to be proportional to the mean, rather than constant.) Simple linear regression estimation methods give less precise parameter estimates and misleading inferential quantities such as standard errors when substantial heteroscedasticity is present. However, various estimation techniques (e.g. [weighted least squares][9528b01c] and [heteroscedasticity-consistent standard errors][554c9507]) can handle heteroscedasticity in a quite general way. Bayesian linear regression techniques can also be used when the variance is assumed to be a function of the mean. It is also possible in some cases to fix the problem by applying a transformation to the response variable (e.g. fit the logarithm of the response variable using a linear regression model, which implies that the response variable has a log-normal distribution rather than a normal distribution).          
- **Independence of errors**. This assumes that the errors of the response variables are uncorrelated with each other. (Actual statistical independence is a stronger condition than mere lack of correlation and is often not needed, although it can be exploited if it is known to hold.) Some methods (e.g. generalized least squares) are capable of handling correlated errors, although they typically require significantly more data unless some sort of regularization is used to bias the model towards assuming uncorrelated errors. Bayesian linear regression is a general way of handling this issue.
- **Lack of multicollinearity** in the predictors. For standard least squares estimation methods, the design matrix \\( X \\) must have full column rank \\( p \\); otherwise, we have a condition known as [multicollinearity][b0a675e3] in the predictor variables. This can be triggered by having two or more perfectly correlated predictor variables (e.g. if the same predictor variable is mistakenly given twice, either without transforming one of the copies or by transforming one of the copies linearly). It can also happen if there is too little data available compared to the number of parameters to be estimated (e.g. fewer data points than regression coefficients). In the case of multicollinearity, the parameter vector \\( \beta \\) will be non-identifiable—it has no unique solution. At most we will be able to identify some of the parameters, i.e. narrow down its value to some linear subspace of \\( R^p \\). See partial least squares regression. Methods for fitting linear models with multicollinearity have been developed; some require additional assumptions such as "effect sparsity"—that a large fraction of the effects are exactly zero.        
Note that the more computationally expensive iterated algorithms for parameter estimation, such as those used in generalized linear models, do not suffer from this problem—and in fact it's quite normal when handling categorically valued predictors to introduce a separate indicator variable predictor for each possible category, which inevitably introduces multicollinearity.

  [0b4621a8]: https://en.wikipedia.org/wiki/Random_variable "Random Variables"
  [dfa746ee]: https://en.wikipedia.org/wiki/Errors-in-variables_model "Errors in Variable Model"
  [79eab8a9]: https://en.wikipedia.org/wiki/Linear_combination "Linear Combination"
  [edf39121]: https://en.wikipedia.org/wiki/Polynomial_regression "Polynomial Regression"
  [aa8a90da]: https://en.wikipedia.org/wiki/Polynomial "Polynomial"
  [dc7b7ef9]: https://en.wikipedia.org/wiki/Lasso_regression "Lasso Regression"
  [9703face]: https://en.wikipedia.org/wiki/Bayesian_linear_regression "Bayesian Linear Regression"
  [ec6ca2ef]: https://en.wikipedia.org/wiki/Homoscedasticity "Homoscedasticity"
  [9528b01c]: https://en.wikipedia.org/wiki/Weighted_least_squares "Weighted Least Squares"
  [554c9507]: https://en.wikipedia.org/wiki/Heteroscedasticity-consistent_standard_errors "Heteroscedasticity Consistent Standard Errors"
  [b0a675e3]: https://en.wikipedia.org/wiki/Multicollinearity "Multicollinearity"


Beyond these assumptions, several other statistical properties of the data strongly influence the performance of different estimation methods:     
- The statistical relationship between the error terms and the regressors plays an important role in determining whether an estimation procedure has desirable sampling properties such as being unbiased and consistent.       
- The arrangement, or probability distribution of the predictor variables \\( x \\) has a major influence on the precision of estimates of \\( \beta \\). Sampling and design of experiments are highly developed subfields of statistics that provide guidance for collecting data in such a way to achieve a precise estimate of \\( \beta \\).        
