<!--
.. title: Supervised Learning - Decision Trees
.. slug: 03-supervised_learning-decision_trees
.. date: 2017-04-03 17:14:29 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

A [decision tree][f02321e5] is a [decision support][9f3a1d37] tool that uses a tree-like graph or model of decisions and their possible consequences, including chance event outcomes, resource costs, and utility. It is one way to display an algorithm.

  [9f3a1d37]: https://en.wikipedia.org/wiki/Decision_support_system "Decision Support System"
  [f02321e5]: https://en.wikipedia.org/wiki/Decision_tree "Decision Tree"

Decision trees are commonly used in [operations research][3463a529], specifically in [decision analysis][590f6d9a], to help identify a strategy most likely to reach a goal, but are also a popular tool in machine learning.

  [590f6d9a]: https://en.wikipedia.org/wiki/Decision_analysis "Decision Analysis"
  [3463a529]: https://en.wikipedia.org/wiki/Operations_research "Operations Research"


# Overview     
A decision tree is a [flowchart][d545426c]-like structure in which each internal node represents a "test" on an attribute (e.g. whether a coin flip comes up heads or tails), each branch represents the outcome of the test, and each leaf node represents a class label (decision taken after computing all attributes). The paths from root to leaf represent classification rules.

  [d545426c]: https://en.wikipedia.org/wiki/Flowchart "Flowchart"

In [decision analysis][590f6d9a], a decision tree and the closely related [influence diagram][27ade8b1] are used as a visual and analytical decision support tool, where the expected values (or expected utility) of competing alternatives are calculated.

  [27ade8b1]: https://en.wikipedia.org/wiki/Influence_diagram "Influence Diagram"

A decision tree consists of three types of nodes:

Decision nodes – typically represented by squares
Chance nodes – typically represented by circles
End nodes – typically represented by triangles
Decision trees are commonly used in operations research and [operations management][8f74b16b]. If, in practice, decisions have to be taken online with no recall under incomplete knowledge, a decision tree should be paralleled by a probability model as a best choice model or online selection model algorithm. Another use of decision trees is as a descriptive means for calculating [conditional probabilities][eb23b59b].

  [8f74b16b]: https://en.wikipedia.org/wiki/Operations_management "Operation Management"
  [eb23b59b]: https://en.wikipedia.org/wiki/Conditional_probability "Conditional Probability"

[Decision trees][f02321e5], [influence diagrams][27ade8b1], [utility functions][3662240d], and other decision analysis tools and methods are taught to undergraduate students in schools of business, health economics, and public health, and are examples of operations research or management science methods.

  [3662240d]: https://en.wikipedia.org/wiki/Utility#Utility_functions "Utility Functions"


## Data Impurity and Entropy      
A decision tree is built top-down from a root node and involves partitioning the data into subsets that contain instances with similar values (homogenous). ID3 algorithm uses entropy to calculate the homogeneity of a sample. If the sample is completely homogeneous the entropy is zero and if the sample is an equally divided it has entropy of one.
\begin{aligned}
p &= 0.5\\\\
\therefore\; q &= 1 - p\\\\
&= 0.5\\\\
\end{aligned}

\begin{aligned}
Entropy &= -p\,log_2p -q\,log_2q\\\\
&= -0.5\,log_20.5 -0.5\,log_20.5\\\\
&= 1\\\\
\end{aligned}

To build a decision tree, we need to calculate two types of entropy using frequency tables as follows:     
a) Entropy using the frequency table of one attribute:
\\[
E(S) = - \sum_{i=1}^c\;p_i\,log_2(p_i)
\\]
b) Entropy using the frequency table of two attributes:    
\\[
E(T,X) = - \sum_{c\in X}\;P(c)\,E(c)
\\]


## Information Gain    
The information gain is based on the decrease in entropy after a dataset is split on an attribute. Constructing a decision tree is all about finding attribute that returns the highest information gain (i.e., the most homogeneous branches).    

Step 1: Calculate entropy of the target.    


Step 2: The dataset is then split on the different attributes. The entropy for each branch is calculated. Then it is added proportionally, to get total entropy for the split. The resulting entropy is subtracted from the entropy before the split. The result is the Information Gain, or decrease in entropy.      
\begin{aligned}
Gain(T, X) &= Entropy(T) - Entropy(T,X)\\\\
&= E(T) - E(T,X)
\end{aligned}

Step 3: Choose attribute with the largest information gain as the decision node, divide the dataset by its branches and repeat the same process on every branch.     




Step 4a: A branch with entropy of 0 is a leaf node.     


Step 4b: A branch with entropy more than 0 needs further splitting.     


Step 5: The ID3 algorithm is run recursively on the non-leaf branches, until all data is classified.      
