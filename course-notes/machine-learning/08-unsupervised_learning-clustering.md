<!--
.. title: Unsupervised Learning - Clustering
.. slug: 08-unsupervised_learning-clustering
.. date: 2017-04-20 06:53:05 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## Unsupervised Learning   
**Unsupervised machine learning** is the machine learning task of inferring a function to describe hidden structure from "unlabeled" data (a classification or categorization is not included in the observations). Since the examples given to the learner are unlabeled, there is no evaluation of the accuracy of the structure that is output by the relevant algorithm—which is one way of distinguishing [unsupervised learning][3ca7fa0d] from [supervised learning][024d7e09] and [reinforcement learning][482a50df].

  [024d7e09]: https://en.wikipedia.org/wiki/Supervised_learning "Supervised Learning"
  [3ca7fa0d]: https://en.wikipedia.org/wiki/Unsupervised_learning "Unsupervised Learning"
  [482a50df]: https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforced Learning"

A central case of unsupervised learning is the problem of [density estimation][638da786] in statistics, though unsupervised learning encompasses many other problems (and solutions) involving summarizing and explaining key features of the data.

  [638da786]: https://en.wikipedia.org/wiki/Density_estimation "Density Estimation"

Approaches to unsupervised learning include:

**[Clustering][5505e60e]**      
- [k-means][4211443f]      
- [mixture models][93b9ad6f]      
- [hierarchical clustering][4d01a655]        
**[Anomaly detection][f2e73ecc]**       
**[Neural Networks][046a899c]**     
- [Hebbian Learning][bc904fc7]    
- [Generative Adversarial Networks][8c51cc14]    
**Approaches for learning [latent variable models][226cc8d2]** such as            
- [Expectation-Maximization Algorithm][28fa5236] (EM)
- [Method of moments][f7e01145]
- [Blind signal separation][224f4201] techniques, e.g.,
    - [Principal component analysis][e1469542],       
    - [Independent component analysis][8a8930b0],       
    - [Non-negative matrix factorization][327b3d26],       
    - [Singular value decomposition][e63101da].        

  [5505e60e]: https://en.wikipedia.org/wiki/Data_clustering "Data Clustering"
  [4211443f]: https://en.wikipedia.org/wiki/K-means "K Means"
  [93b9ad6f]: https://en.wikipedia.org/wiki/Mixture_models "Mixture Models"
  [4d01a655]: https://en.wikipedia.org/wiki/Hierarchical_clustering "Hierachical Clustering"
  [f2e73ecc]: https://en.wikipedia.org/wiki/Anomaly_detection "Anomaly Detection"
  [046a899c]: https://en.wikipedia.org/wiki/Artificial_neural_network "Neural Network"
  [82087636]: https://en.wikipedia.org/wiki/Hebbian_Learning "Hebbian Learning"
  [bc904fc7]: https://en.wikipedia.org/wiki/Hebbian_Learning "Hebbian Learning"
  [8c51cc14]: https://en.wikipedia.org/wiki/Generative_Adversarial_Networks "Generative Adversarial Networks"
  [28fa5236]: https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm "Expectation Maximization Algorithm"
  [f7e01145]: https://en.wikipedia.org/wiki/Method_of_moments_(statistics) "Method of Moments"
  [224f4201]: https://en.wikipedia.org/wiki/Blind_signal_separation "Blind Signal Separation"
  [e1469542]: https://en.wikipedia.org/wiki/Principal_component_analysis "Principal Component Analysis (PCA)"
  [8a8930b0]: https://en.wikipedia.org/wiki/Independent_component_analysis "Independent Component Analysis"
  [327b3d26]: https://en.wikipedia.org/wiki/Non-negative_matrix_factorization "Non-Negative Matrix Factorization"
  [e63101da]: https://en.wikipedia.org/wiki/Singular_value_decomposition "Singular Value Decomposition"
  [226cc8d2]: https://en.wikipedia.org/wiki/Latent_variable_model "Latent Variable Model"


## Clustering
**Cluster analysis** or **Clustering** is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense or another) to each other than to those in other groups (clusters). It is a main task of exploratory [data mining][9df920fa], and a common technique for statistical data analysis, used in many fields, including [machine learning][c68a69c4], [pattern recognition][276dfb09], [image analysis][528c1864], [information retrieval][7bc1780d], [bioinformatics][794be0e6], [data compression][acaf9ddb], and [computer graphics][52becfb1].

  [9df920fa]: https://en.wikipedia.org/wiki/Data_mining "Data Mining"
  [c68a69c4]: https://en.wikipedia.org/wiki/Machine_learning "Machine Learning"
  [276dfb09]: https://en.wikipedia.org/wiki/Pattern_recognition "Pattern Recognition"
  [528c1864]: https://en.wikipedia.org/wiki/Image_analysis "Image Analysis"
  [7bc1780d]: https://en.wikipedia.org/wiki/Information_retrieval "Information Retrieval"
  [794be0e6]: https://en.wikipedia.org/wiki/Bioinformatics "Bio-Informatics"
  [acaf9ddb]: https://en.wikipedia.org/wiki/Data_compression "Data Compression"
  [52becfb1]: https://en.wikipedia.org/wiki/Computer_graphics "Computer Graphics"

Cluster analysis itself is not one specific algorithm, but the general task to be solved. It can be achieved by various algorithms that differ significantly in their notion of what constitutes a cluster and how to efficiently find them. Popular notions of clusters include groups with small distances among the cluster members, dense areas of the data space, intervals or particular statistical distributions. Clustering can therefore be formulated as a [multi-objective optimization][087bddf2] problem. The appropriate clustering algorithm and parameter settings (including values such as the distance function to use, a density threshold or the number of expected clusters) depend on the individual data set and intended use of the results. Cluster analysis as such is not an automatic task, but an iterative process of knowledge discovery or interactive multi-objective optimization that involves trial and failure. It is often necessary to modify data preprocessing and model parameters until the result achieves the desired properties.

  [087bddf2]: https://en.wikipedia.org/wiki/Multi-objective_optimization "Multi-Objective Optimization"

Besides the term clustering, there are a number of terms with similar meanings, including _automatic classification_, _numerical taxonomy_, _botryology_ (from Greek βότρυς "grape") and typological analysis. The subtle differences are often in the usage of the results: while in data mining, the resulting groups are the matter of interest, in automatic classification the resulting discriminative power is of interest.

The notion of a "cluster" cannot be precisely defined, which is one of the reasons why there are so many clustering algorithms. There is a common denominator: a group of data objects. However, different researchers employ different cluster models, and for each of these cluster models again different algorithms can be given. The notion of a cluster, as found by different algorithms, varies significantly in its properties. Understanding these "cluster models" is key to understanding the differences between the various algorithms.


Typical cluster models include:          

- Connectivity models: for example, [hierarchical clustering][4d01a655] builds models based on distance connectivity.    
- Centroid models: for example, the [k-means algorithm][3e2393b8] represents each cluster by a single mean vector.      
- Distribution models: clusters are modeled using statistical distributions, such as [multivariate normal distributions][339d84a0] used by the [Expectation-Maximization Algorithm][28fa5236].         
- Density models: for example, DBSCAN and OPTICS defines clusters as connected dense regions in the data space.        
- Subspace models: in Biclustering (also known as Co-clustering or two-mode-clustering), clusters are modeled with both cluster members and relevant attributes.       
- Group models: some algorithms do not provide a refined model for their results and just provide the grouping information.         
- Graph-based models: a clique, that is, a subset of nodes in a graph such that every two nodes in the subset are connected by an edge can be considered as a prototypical form of cluster. Relaxations of the complete connectivity requirement (a fraction of the edges can be missing) are known as quasi-cliques, as in the HCS clustering algorithm.        

  [3e2393b8]: https://en.wikipedia.org/wiki/K-means_algorithm "K Means Algorithm"
  [339d84a0]: https://en.wikipedia.org/wiki/Multivariate_normal_distribution "Multivariate Normal Distribution"

A "clustering" is essentially a set of such clusters, usually containing all objects in the data set. Additionally, it may specify the relationship of the clusters to each other, for example, a hierarchy of clusters embedded in each other. Clusterings can be roughly distinguished as:         

- Hard clustering: each object belongs to a cluster or not         
- Soft clustering (also: [fuzzy clustering][37c07d5f]): each object belongs to each cluster to a certain degree (for example, a likelihood of belonging to the cluster)       

  [37c07d5f]: https://en.wikipedia.org/wiki/Fuzzy_clustering "Fuzzy Clustering"

There are also finer distinctions possible, for example:        

- Strict partitioning clustering: each object belongs to exactly one cluster      
- Strict partitioning clustering with outliers: objects can also belong to no cluster, and are considered outliers       
- Overlapping clustering (also: alternative clustering, multi-view clustering): objects may belong to more than one cluster; usually involving hard clusters        
- Hierarchical clustering: objects that belong to a child cluster also belong to the parent cluster        
- [Subspace clustering][e9db2eee]: while an overlapping clustering, within a uniquely defined subspace, clusters are not expected to overlap        

  [e9db2eee]: https://en.wikipedia.org/wiki/Subspace_clustering "Subspace Clustering"
