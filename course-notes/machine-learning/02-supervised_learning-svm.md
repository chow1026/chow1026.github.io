<!--
.. title: Supervised Learning - Support Vector Machine (SVM)
.. slug: 02-supervised_learning-svm
.. date: 2017-04-03 10:11:55 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Support Vector Machine (SVM)      

In [machine learning][d0ba0e61], support vector machines (SVMs, also support vector networks) are supervised learning models with associated learning algorithms that analyze data used for [classification][ea103332] and [regression analysis][f24e6f38]. Given a set of training examples, each marked as belonging to one or the other of two categories, an SVM training algorithm builds a model that assigns new examples to one category or the other, making it a non-[probabilistic][eb8e51a4] [binary][47309b79] [linear classifier][8a0f0125]. An SVM model is a representation of the examples as points in space, mapped so that the examples of the separate categories are divided by a clear gap that is as wide as possible. New examples are then mapped into that same space and predicted to belong to a category based on which side of the gap they fall.

  [ea103332]: https://en.wikipedia.org/wiki/Statistical_classification "Statistical Classification"
  [d0ba0e61]: https://en.wikipedia.org/wiki/Machine_learning "Machine Learning"
  [f24e6f38]: https://en.wikipedia.org/wiki/Regression_analysis "Regression Analysis"
  [eb8e51a4]: https://en.wikipedia.org/wiki/Probabilistic_classification "Probabilistic Classification"
  [47309b79]: https://en.wikipedia.org/wiki/Binary_classification "Binary Classification"
  [8a0f0125]: https://en.wikipedia.org/wiki/Linear_classifier "Linear Classifier"

In addition to performing linear classification, SVMs can efficiently perform a non-linear classification using what is called the kernel trick, implicitly mapping their inputs into high-dimensional feature spaces.

When data are not labeled, supervised learning is not possible, and an [unsupervised learnin][dcbcb5e9]g approach is required, which attempts to find natural [clustering of the data][44d9d562] to groups, and then map new data to these formed groups. The clustering algorithm which provides an improvement to the support vector machines is called support vector clustering and is often[citation needed] used in industrial applications either when data are not labeled or when only some data are labeled as a preprocessing for a classification pass.

  [dcbcb5e9]: https://en.wikipedia.org/wiki/Unsupervised_learning "Unsupervised Learning"
  [44d9d562]: https://en.wikipedia.org/wiki/Cluster_analysis "Cluster Analysis"


## Motivation    
[Classifying data][ea103332] is a common task in [machine learning][d0ba0e61]. Suppose some given data points each belong to one of two classes, and the goal is to decide which class a new data point will be in. In the case of support vector machines, a data point is viewed as a \\( p \\) p-dimensional vector (a list of \\( p \\) p numbers), and we want to know whether we can separate such points with a \\( (p-1) \\) (p-1)-dimensional [hyperplane][acded98f]. This is called a linear classifier. There are many hyperplanes that might classify the data. One reasonable choice as the best hyperplane is the one that represents the largest separation, or [margin][94ae2e4e], between the two classes. So we choose the hyperplane so that the distance from it to the nearest data point on each side is maximized. If such a hyperplane exists, it is known as the maximum-margin hyperplane and the linear classifier it defines is known as a maximum [margin classifier][2e8a96b6]; or equivalently, the [perceptron][8152d8c7] of optimal stability.

  [acded98f]: https://en.wikipedia.org/wiki/Hyperplane_separation_theorem "Hyperplane Separation Theorem"
  [94ae2e4e]: https://en.wikipedia.org/wiki/Margin_(machine_learning) "Margin (Machine Learning)"
  [2e8a96b6]: https://en.wikipedia.org/wiki/Margin_classifier "Margin Classifier"
  [8152d8c7]: https://en.wikipedia.org/wiki/Perceptron "Perceptron"


## Definition      
More formally, a support vector machine constructs a [hyperplane][acded98f] or set of hyperplanes in a high- or infinite-dimensional space, which can be used for classification, regression, or other tasks. Intuitively, a good separation is achieved by the hyperplane that has the largest distance to the nearest training-data point of any class (so-called functional margin), since in general the larger the margin the lower the [generalization error][12d97779] of the classifier.

  [12d97779]: https://en.wikipedia.org/wiki/Generalization_error "Generalization Error"


Whereas the original problem may be stated in a finite dimensional space, it often happens that the sets to discriminate are not [linearly separable][27ba7cf2] in that space. For this reason, it was proposed that the original finite-dimensional space be mapped into a much higher-dimensional space, presumably making the separation easier in that space. To keep the computational load reasonable, the mappings used by SVM schemes are designed to ensure that dot products may be computed easily in terms of the variables in the original space, by defining them in terms of a [kernel function][1e7d23f7] \\( k(x,y) \\) k(x,y) selected to suit the problem.

  [27ba7cf2]: https://en.wikipedia.org/wiki/Linear_separability "Linear Separability"
  [1e7d23f7]: https://en.wikipedia.org/wiki/Positive-definite_kernel "Kernel Function"


## Applications      
SVMs can be used to solve various real world problems:

- SVMs are helpful in [text and hypertext categorization][6eab5d2f] as their application can significantly reduce the need for labeled training instances in both the standard inductive and [transductive][1b5ecac0] settings.
- [Classification of images][8dd6e529] can also be performed using SVMs. Experimental results show that SVMs achieve significantly higher search accuracy than traditional query refinement schemes after just three to four rounds of relevance feedback. This is also true of [image segmentation][96908577] systems, including those using a modified version SVM that uses the privileged approach as suggested by Vapnik.
- [Hand-written characters can be recognized][93b85089] using SVM.
- The SVM algorithm has been widely applied in the biological and other sciences. They have been used to classify proteins with up to 90% of the compounds classified correctly. [Permutation tests][249d9d2b] based on SVM weights have been suggested as a mechanism for interpretation of SVM models.  Support vector machine weights have also been used to interpret SVM models in the past.  Posthoc interpretation of support vector machine models in order to identify features used by the model to make predictions is a relatively new area of research with special significance in the biological sciences.

  [6eab5d2f]: https://en.wikipedia.org/wiki/Document_classification "Text/Document Classification"
  [1b5ecac0]: https://en.wikipedia.org/wiki/Transduction_(machine_learning) "Transduction (Machine Learning)"
  [8dd6e529]: https://en.wikipedia.org/wiki/Computer_vision#Recognition "Image Recognition"
  [96908577]: https://en.wikipedia.org/wiki/Image_segmentation "Image Segmentation"
  [93b85089]: https://en.wikipedia.org/wiki/Handwriting_recognition "Handwriting Recognition"
  [249d9d2b]: https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests "Permutation Tests"


## History        
The original SVM algorithm was invented by Vladimir N. Vapnik and Alexey Ya. Chervonenkis in 1963. In 1992, Bernhard E. Boser, Isabelle M. Guyon and Vladimir N. Vapnik suggested a way to create nonlinear classifiers by applying the kernel trick to maximum-margin hyperplanes.  The current standard incarnation (soft margin) was proposed by Corinna Cortes and Vapnik in 1993 and published in 1995.    
