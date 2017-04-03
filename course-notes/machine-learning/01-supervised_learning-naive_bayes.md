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
