<!--
.. title: Principle Component Analysis
.. slug: 12-pca
.. date: 2017-04-20 07:00:11 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Principal component analysis (PCA) is a statistical procedure that uses an [orthogonal transformation][fa83c00f] to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components (or sometimes, principal modes of variation). The number of principal components is less than or equal to the smaller of the number of original variables or the number of observations. This transformation is defined in such a way that the first principal component has the largest possible variance (that is, accounts for as much of the variability in the data as possible), and each succeeding component in turn has the highest variance possible under the constraint that it is [orthogonal][490c3c35] to the preceding components. The resulting vectors are an uncorrelated [orthogonal basis set][8aa4b6ae]. PCA is sensitive to the relative scaling of the original variables.

  [fa83c00f]: https://en.wikipedia.org/wiki/Orthogonal_transformation "Orthogonal Transformation"
  [490c3c35]: https://en.wikipedia.org/wiki/Orthogonal "Orthogonal"
  [8aa4b6ae]: https://en.wikipedia.org/wiki/Orthogonal_basis_set "Orthogonal Basis Set"

PCA is mostly used as a tool in [exploratory data analysis][1667466d] and for making [predictive models][53b428e6]. PCA can be done by [eigenvalue decomposition][df649d02] of a data [covariance][12d67faf] (or [correlation][68af379c]) matrix or [singular value decomposition][b1d1c217] of a [data matrix][42aedaa0], usually after mean centering (and normalizing or using Z-scores) the data matrix for each attribute. The results of a PCA are usually discussed in terms of component scores, sometimes called factor scores (the transformed variable values corresponding to a particular data point), and loadings (the weight by which each standardized original variable should be multiplied to get the component score).

  [1667466d]: https://en.wikipedia.org/wiki/Exploratory_data_analysis "Exploratory Data Analysis"
  [53b428e6]: https://en.wikipedia.org/wiki/Predictive_modeling "Predictive Model"
  [df649d02]: https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix "Eigenvalue Decomposition"
  [12d67faf]: https://en.wikipedia.org/wiki/Covariance "Covariance"
  [68af379c]: https://en.wikipedia.org/wiki/Correlation "Correlation"
  [b1d1c217]: https://en.wikipedia.org/wiki/Singular_value_decomposition "Singular Value Decomposition"
  [42aedaa0]: https://en.wikipedia.org/wiki/Data_matrix_(multivariate_statistics) "Data Matrix"

PCA is the simplest of the true [eigenvector][be6376a0]-based multivariate analyses. Often, its operation can be thought of as revealing the internal structure of the data in a way that best explains the variance in the data. If a multivariate dataset is visualised as a set of coordinates in a high-dimensional data space (1 axis per variable), PCA can supply the user with a lower-dimensional picture, a projection of this object when viewed from its most informative viewpoint. This is done by using only the first few principal components so that the dimensionality of the transformed data is reduced.

  [be6376a0]: https://en.wikipedia.org/wiki/Eigenvectors "Eigenvectors"

PCA is closely related to [factor analysis][7a6ed2f7]. Factor analysis typically incorporates more domain specific assumptions about the underlying structure and solves eigenvectors of a slightly different matrix.

  [7a6ed2f7]: https://en.wikipedia.org/wiki/Factor_analysis "Factor Analysis"

PCA is also related to [canonical correlation analysis][cca943ce] (CCA). CCA defines coordinate systems that optimally describe the cross-covariance between two datasets while PCA defines a new [orthogonal coordinate system][0fef7bce] that optimally describes variance in a single dataset.

  [cca943ce]: https://en.wikipedia.org/wiki/Canonical_correlation "Canonical Correlation"
  [0fef7bce]: https://en.wikipedia.org/wiki/Orthogonal_coordinate_system "Orthogonal Coordinate System"
