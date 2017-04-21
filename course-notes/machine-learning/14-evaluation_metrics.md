<!--
.. title: Evaluation Metrics
.. slug: 14-evaluation_metrics
.. date: 2017-04-20 07:04:44 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


The simplest metric is Accuracy.  It is defined as :

Accuracy = no. of items in a class labeled correctly / all items in that class

There are shortcomings of accuracy:      

- not ideal for skewed classes    
- may want to err on side of guessing innocent   
- may want to err of side of guessing guilty   


## Model Evaluation Metrics

There are 3 different approaches to evaluate the quality of predictions of a model:    

- **Estimator score method**: Estimators have a score method providing a default evaluation criterion for the problem they are designed to solve. This is not discussed on this page, but in each estimator’s documentation.     
- **Scoring parameter**: Model-evaluation tools using [cross-validation][5478f366] (such as model_selection.cross_val_score and model_selection.GridSearchCV) rely on an internal scoring strategy. This is discussed in the section [The scoring parameter: defining model evaluation rules][0caba749].     
- **Metric functions**: The metrics module implements functions assessing prediction error for specific purposes. These metrics are detailed in sections on [Classification metrics][5d91992e], [Multilabel ranking metrics][1c349b23], [Regression metrics][d722d625] and [Clustering metrics][1011cf9e].     

  [5478f366]: http://scikit-learn.org/stable/modules/cross_validation.html#cross-validation "Cross Validation"
  [0caba749]: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter "Scoring Parameter"
  [5d91992e]: http://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics "Classification Metrics"
  [1c349b23]: http://scikit-learn.org/stable/modules/model_evaluation.html#multilabel-ranking-metrics "Multilabel Ranking Metrics"
  [d722d625]: http://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics "Regression Metrics"
  [1011cf9e]: http://scikit-learn.org/stable/modules/model_evaluation.html#clustering-metrics "Clustering Metrics"

Finally, Dummy estimators are useful to get a baseline value of those metrics for random predictions.

For the most common use cases, you can designate a scorer object with the scoring parameter; the table below shows all possible values. All scorer objects follow the convention that **higher return values are better than lower return values**.

**Classification**:       

- confusion matrix
- accuracy   
- average precision     
- precision score    
- recall score    
- f1 score (micro, macro, weighted, samples)    
- roc auc (area under curve)      
- log loss

**Clustering**:       

- adjusted rand score

**Regression**:      

- Mean absolute error
- Mean square error
- Median absolute error
- \\(r^2\\) score


## Confusion Matrix      

In the field of [machine learning][ab888587] and specifically the problem of [statistical classification][f3cec3e0], a **confusion matrix**, also known as an error matrix,[4] is a specific table layout that allows visualization of the performance of an algorithm, typically a [supervised learning][441a8b2c] one (in [unsupervised learning][e05293fc] it is usually called a **matching matrix**). Each column of the matrix represents the instances in a predicted class while each row represents the instances in an actual class (or vice versa).   The name stems from the fact that it makes it easy to see if the system is confusing two classes (i.e. commonly mislabelling one as another).

  [ab888587]: https://en.wikipedia.org/wiki/Machine_learning "Machine Learning"
  [f3cec3e0]: https://en.wikipedia.org/wiki/Statistical_classification "Statistical Classification"
  [441a8b2c]: https://en.wikipedia.org/wiki/Supervised_learning "Supervised Learning"
  [e05293fc]: https://en.wikipedia.org/wiki/Unsupervised_learning "Unsupervised Learning"

It is a special kind of [contingency table][11df1c45], with two dimensions ("actual" and "predicted"), and identical sets of "classes" in both dimensions (each combination of dimension and class is a variable in the contingency table).

  [11df1c45]: https://en.wikipedia.org/wiki/Contingency_table "Contingency Table"

### NOTES FROM UDACITY CLASS:     
**Recall**: True Positive / (True Positive + False Negative). Out of all the items that are truly positive, how many were correctly classified as positive. Or simply, how many positive items were 'recalled' from the dataset.      

**Precision**: True Positive / (True Positive + False Positive). Out of all the items labeled as positive, how many truly belong to the positive class.      

### Terminology and derivations from a confusion matrix

**condition positive (P)** :: the number of real positive cases in the data      

**condition negatives (N)** :: the number of real negative cases in the data

**true positive (TP)** :: eqv. with hit    

**true negative (TN)** :: eqv. with correct rejection    

**false positive (FP)** :: eqv. with [false alarm][97aeffed], [Type I error][156261e9]

  [97aeffed]: https://en.wikipedia.org/wiki/False_alarm "False Alarm"
  [156261e9]: https://en.wikipedia.org/wiki/Type_I_error "Type I Error"

**false negative (FN)** :: eqv. with miss, [Type II error][df7cc0ed]

  [df7cc0ed]: https://en.wikipedia.org/wiki/Type_II_error "Type II Error"

------------------------------------------------------------------------------
[sensitivity][0c430637], [recall][d8a2fbda], [hit rate][2db84899], or [true positive rate (TPR)][26ba1fb2] ::
\\[
  \mathrm{TPR} = \frac{\mathrm{TP}}{P} = \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}}
\\]

  [0c430637]: https://en.wikipedia.org/wiki/Sensitivity_(test) "Sensitivity"
  [d8a2fbda]: https://en.wikipedia.org/wiki/Information_retrieval#Recall "Recall"
  [2db84899]: https://en.wikipedia.org/wiki/Hit_rate "Hit Rate"
  [26ba1fb2]: https://en.wikipedia.org/wiki/Sensitivity_(test) "True Positive Rate (TPR)"

[specificity][2d944914] or [true negative rate (TNR)][9ac5d1d8] ::
\\[
  \mathrm{TNR} = \frac{\mathrm{TN}}{N} = \frac{\mathrm{TN}}{\mathrm{TN} + \mathrm{FP}}
\\]

  [2d944914]: https://en.wikipedia.org/wiki/Specificity_(tests) "Speciticity"
  [9ac5d1d8]: https://en.wikipedia.org/wiki/Specificity_(tests) "True Negative Rate (TNR)"

[precision][20ddb84f] or [positive predictive value (PPV)][76f9d232] ::   
\\[
  \mathrm{PPV} = \frac{\mathrm{TP}}{\mathrm {TP} +\mathrm {FP}}
\\]

  [20ddb84f]: https://en.wikipedia.org/wiki/Information_retrieval#Precision "Precision"
  [76f9d232]: https://en.wikipedia.org/wiki/Positive_predictive_value "Positive Predictive Value"

[negative predictive value (NPV)][3d52a732] ::    
\\[
  \mathrm{NPV} = \frac{\mathrm{TN}}{\mathrm {TN} +\mathrm {FN}}
\\]

  [3d52a732]: https://en.wikipedia.org/wiki/Negative_predictive_value "Negative Predictive Value"

**miss rate** or [false negative rate (FNR)][a7c958b1] ::   
\\[
  \mathrm{FNR} = \frac{\mathrm{FN}}{P} = \frac{\mathrm{FN}}{\mathrm{FN} + \mathrm{TP}} = 1 - \mathrm{TPR}
\\]

  [a7c958b1]: https://en.wikipedia.org/wiki/Type_I_and_type_II_errors#False_positive_and_false_negative_rates "False Negative Rate"

[fall-out][557b0042] or [false positive rate (FPR)][906e32bc] ::    
\\[
  \mathrm{FPR} = \frac{\mathrm{FP}}{N} = \frac{\mathrm{FP}}{\mathrm{FP} + \mathrm{TN}} = 1 - \mathrm{TNP}
\\]

  [557b0042]: https://en.wikipedia.org/wiki/Information_retrieval#Fall-out "Fall Out"
  [906e32bc]: https://en.wikipedia.org/wiki/Information_retrieval#Fall-out "False Positive Rate"

[false discovery rate (FDR)][1e0aaae4] ::     
\\[
  \mathrm{FDR} = \frac{\mathrm{FP}}{\mathrm {FP} +\mathrm {TP}} = 1 - \mathrm{PPV}
\\]

  [1e0aaae4]: https://en.wikipedia.org/wiki/False_discovery_rate "False Discovery Rate"

[false omission rate (FOR)][ab539170]  ::      
\\[
  \mathrm{FOR} = \frac{\mathrm{FN}}{\mathrm {FN} +\mathrm {TN}} = 1 - \mathrm{NPV}
\\]

  [ab539170]: https://en.wikipedia.org/wiki/Positive_and_negative_predictive_values "False Omission Rate"

------------------------------------------------------------------------------
[accuracy (ACC)][ea8c3f4b] ::    
\\[
  \mathrm{ACC} = \frac{\mathrm{TP} + \mathrm{TN}}{ {P} + {N}}
\\]

  [ea8c3f4b]: https://en.wikipedia.org/wiki/Accuracy "Accuracy"

[F1 score][6693849e] :: is the [harmonic mea][34d32e31]n of [precision][20ddb84f] and [sensitivity][0c430637]       
\\[
  F_{1} = 2 \cdot \frac{\mathrm{PPV} \cdot \mathrm{TPR}}{\mathrm{PPV} + \mathrm{TPR}} =  \frac{2\mathrm{TP}}{2\mathrm{TP} + \mathrm{FP} + \mathrm{FN}}
\\]

  [34d32e31]: https://en.wikipedia.org/wiki/Harmonic_mean#Harmonic_mean_of_two_numbers "Harmonic Mean"
  [6693849e]: https://en.wikipedia.org/wiki/F1_score "F1 Score"

[Matthews correlation coefficient (MCC)][05c95ed6] ::     
\\[
  \mathrm{MCC} = \frac{ \mathrm{TP} \times \mathrm{TN} - \mathrm{FP} \times \mathrm{FN} }{ \sqrt{(\mathrm{TP} + \mathrm{FP} )(\mathrm{TP} + \mathrm{FN} )( \mathrm{TN} + \mathrm{FP} )( \mathrm{TN} + \mathrm{FN} )} }
\\]

  [05c95ed6]: https://en.wikipedia.org/wiki/Matthews_correlation_coefficient "Matthews Correlation Coefficient"

[Informedness][09e5aa50] or **Bookmaker Informedness (BM)** ::     
\\[
  \mathrm{BM}  = \mathrm{TPR} + \mathrm{TNR} -1
\\]

  [09e5aa50]: https://en.wikipedia.org/wiki/Informedness "Informedness"

**Markedness (MK)** ::      
\\[
  \mathrm{MK}  = \mathrm{PPV} + \mathrm{NPV} -1
\\]

------------------------------------------------------------------------------


<table class="wikitable" align="center" style="text-align:center; border:none; background:transparent;">
<tbody><tr>
<td colspan="2" style="border:none;"></td>
<td colspan="2" style="background:#eeeebb;"><b>predicted condition</b></td>
</tr>
<tr>
<td style="border:none;"></td>
<td style="background:#dddddd;"><a href="https://en.wikipedia.org/wiki/Statistical_population" title="Statistical population">total population</a></td>
<td style="background:#ffffcc;">prediction positive</td>
<td style="background:#ddddaa;">prediction negative</td>
<td style="background:#eeeecc;"><a href="https://en.wikipedia.org/wiki/Prevalence" title="Prevalence">Prevalence</a> <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ&nbsp;condition positive</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;total population</span></span></span></span></td>
</tr>
<tr>
<td rowspan="2" style="background:#bbeeee;"><b>true<br>
condition</b></td>
<td style="background:#ccffff;">condition<br>
positive</td>
<td style="background:#ccffcc;"><span style="color:#006600;"><b><a href="https://en.wikipedia.org/wiki/True_positive" class="mw-redirect" title="True positive">True Positive (TP)</a></b></span></td>
<td style="background:#eedddd;"><span style="color:#cc0000;"><b><a href="https://en.wikipedia.org/wiki/False_Negative" class="mw-redirect" title="False Negative">False Negative (FN)</a></b></span><br>
(<a href="https://en.wikipedia.org/wiki/Type_II_error" class="mw-redirect" title="Type II error">type II error</a>)</td>
<td style="background:#eeffcc;"><a href="https://en.wikipedia.org/wiki/True_Positive_Rate" class="mw-redirect" title="True Positive Rate">True&nbsp;Positive&nbsp;Rate&nbsp;(TPR)</a>, <a href="https://en.wikipedia.org/wiki/Sensitivity_(tests)" class="mw-redirect" title="Sensitivity (tests)">Sensitivity</a>, <a href="https://en.wikipedia.org/wiki/Recall_(information_retrieval)" class="mw-redirect" title="Recall (information retrieval)">Recall</a>, Probability&nbsp;of&nbsp;Detection <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ TP</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;condition&nbsp;positive</span></span></span></span></td>
<td style="background:#ffeecc;"><a href="https://en.wikipedia.org/wiki/False_Negative_Rate" class="mw-redirect" title="False Negative Rate">False&nbsp;Negative&nbsp;Rate&nbsp;(FNR)</a>, Miss&nbsp;Rate <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ FN</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;condition&nbsp;positive</span></span></span></span></td>
</tr>
<tr>
<td style="background:#aadddd;">condition<br>
negative</td>
<td style="background:#ffdddd;"><span style="color:#cc0000;"><b><a href="https://en.wikipedia.org/wiki/False_Positive" class="mw-redirect" title="False Positive">False&nbsp;Positive&nbsp;(FP)</a></b></span><br>
(<a href="https://en.wikipedia.org/wiki/Type_I_error" class="mw-redirect" title="Type I error">Type I error</a>)</td>
<td style="background:#bbeebb;"><span style="color:#006600;"><b><a href="https://en.wikipedia.org/wiki/True_negative" class="mw-redirect" title="True negative">True Negative (TN)</a></b></span></td>
<td style="background:#eeddbb;"><a href="https://en.wikipedia.org/wiki/False_Positive_Rate" class="mw-redirect" title="False Positive Rate">False&nbsp;Positive&nbsp;Rate&nbsp;(FPR)</a>, <a href="https://en.wikipedia.org/wiki/Information_retrieval" title="Information retrieval"><span class="nowrap">Fall-out</span></a>, Probability&nbsp;of&nbsp;False&nbsp;Alarm <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ FP</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;condition&nbsp;negative</span></span></span></span></td>
<td style="background:#ddeebb;"><a href="https://en.wikipedia.org/wiki/True_Negative_Rate" class="mw-redirect" title="True Negative Rate">True&nbsp;Negative&nbsp;Rate&nbsp;(TNR)</a>, <a href="https://en.wikipedia.org/wiki/Specificity_(tests)" class="mw-redirect" title="Specificity (tests)">Specificity</a> (SPC) <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ TN</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;condition&nbsp;negative</span></span></span></span></td>
</tr>
<tr>
<td style="border:none;"></td>
<td rowspan="2" style="background:#cceecc;border-top:solid grey;border-right:solid grey"><a href="https://en.wikipedia.org/wiki/Accuracy_and_precision" title="Accuracy and precision">Accuracy</a> <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ&nbsp;TP + Σ TN</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;total population</span></span></span></span></td>
<td style="background:#ccffee;border-top:solid grey;"><a href="https://en.wikipedia.org/wiki/Positive_Predictive_Value" class="mw-redirect" title="Positive Predictive Value">Positive&nbsp;Predictive&nbsp;Value&nbsp;(PPV)</a>, <a href="https://en.wikipedia.org/wiki/Precision_(information_retrieval)" class="mw-redirect" title="Precision (information retrieval)">Precision</a> <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ TP</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;prediction&nbsp;positive</span></span></span></span></td>
<td style="background:#eeddee;border-bottom:solid grey;"><a href="https://en.wikipedia.org/wiki/False_omission_rate" class="mw-redirect" title="False omission rate">False&nbsp;Omission&nbsp;Rate&nbsp;(FOR)</a> <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ FN</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;prediction&nbsp;negative</span></span></span></span></td>
<td style="background:#eeeeee;"><a href="https://en.wikipedia.org/wiki/Positive_likelihood_ratio" class="mw-redirect" title="Positive likelihood ratio">Positive&nbsp;Likelihood&nbsp;Ratio&nbsp;<span class="nowrap">(LR+)</span></a> <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">TPR</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">FPR</span></span></span></span></td>
<td rowspan="2" style="background:#dddddd;"><a href="https://en.wikipedia.org/wiki/Diagnostic_odds_ratio" title="Diagnostic odds ratio">Diagnostic&nbsp;Odds&nbsp;Ratio&nbsp;(DOR)</a> <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">LR+</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">LR−</span></span></span></span></td>
</tr>
<tr>
<td style="border:none;"></td>
<td style="background:#cceeff;border-top:solid grey;"><a href="https://en.wikipedia.org/wiki/False_Discovery_Rate" class="mw-redirect" title="False Discovery Rate">False&nbsp;Discovery&nbsp;Rate&nbsp;(FDR)</a> <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ FP</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;prediction&nbsp;positive</span></span></span></span></td>
<td style="background:#aaddcc;border-bottom:solid grey;"><a href="https://en.wikipedia.org/wiki/Negative_Predictive_Value" class="mw-redirect" title="Negative Predictive Value">Negative&nbsp;Predictive&nbsp;Value&nbsp;(NPV)</a> <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">Σ TN</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">Σ&nbsp;prediction&nbsp;negative</span></span></span></span></td>
<td style="background:#cccccc;"><a href="https://en.wikipedia.org/wiki/Negative_likelihood_ratio" class="mw-redirect" title="Negative likelihood ratio">Negative&nbsp;Likelihood&nbsp;Ratio&nbsp;<span class="nowrap">(LR−)</span></a> <span style="font-size:118%;white-space:nowrap;">= <span class="texhtml"><span class="sfrac nowrap" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span style="display:block; line-height:1em; margin:0 0.1em;">FNR</span><span style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">TNR</span></span></span></span></td>
</tr>
</tbody></table>
