---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.7.6
  plotly:
    description: Interpret the results of your classification using Receiver Operating
      Characteristics (ROC) and Precision-Recall (PR) Curves in Python with Plotly.
    display_as: ai_ml
    language: python
    layout: base
    name: ROC and PR Curves
    order: 3
    page_type: u-guide
    permalink: python/roc-and-pr-curves/
    thumbnail: thumbnail/ml-roc-pr.png
---

## Preliminary plots

Before diving into the receiver operating characteristic (ROC) curve, we will look at two plots that will give some context to the thresholds mechanism behind the ROC and PR curves.

In the histogram, we observe that the score spread such that most of the positive labels are binned near 1, and a lot of the negative labels are close to 0. When we set a threshold on the score, all of the bins to its left will be classified as 0's, and everything to the right will be 1's. There are obviously a few outliers, such as **negative** samples that our model gave a high score, and *positive* samples with a low score. If we set a threshold right in the middle, those outliers will respectively become **false positives** and *false negatives*.

As we adjust thresholds, the number of positive positives will increase or decrease, and at the same time the number of true positives will also change; this is shown in the second plot. As you can see, the model seems to perform fairly well, because the true positive rate decreases slowly, whereas the false positive rate decreases sharply as we increase the threshold. Those two lines each represent a dimension of the ROC curve.

```python
import plotly.express as px
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=500, random_state=0)

model = LogisticRegression()
model.fit(X, y)
y_score = model.predict_proba(X)[:, 1]
fpr, tpr, thresholds = roc_curve(y, y_score)

# The histogram of scores compared to true labels
fig_hist = px.histogram(
    x=y_score, color=y, nbins=50,
    labels=dict(color='True Labels', x='Score')
)

fig_hist.show()


# Evaluating model performance at various thresholds
df = pd.DataFrame({
    'False Positive Rate': fpr,
    'True Positive Rate': tpr
}, index=thresholds)
df.index.name = "Thresholds"
df.columns.name = "Rate"

fig_thresh = px.line(
    df, title='TPR and FPR at every threshold',
    width=700, height=500
)

fig_thresh.update_yaxes(scaleanchor="x", scaleratio=1)
fig_thresh.update_xaxes(range=[0, 1], constrain='domain')
fig_thresh.show()
```

## Basic binary ROC curve

Notice how this ROC curve looks similar to the True Positive Rate curve from the previous plot. This is because they are the same curve, except the x-axis consists of increasing values of FPR instead of threshold, which is why the line is flipped and distorted.

We also display the area under the ROC curve (ROC AUC), which is fairly high, thus consistent with our interpretation of the previous plots.

```python
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=500, random_state=0)

model = LogisticRegression()
model.fit(X, y)
y_score = model.predict_proba(X)[:, 1]

fpr, tpr, thresholds = roc_curve(y, y_score)

fig = px.area(
    x=fpr, y=tpr,
    title=f'ROC Curve (AUC={auc(fpr, tpr):.4f})',
    labels=dict(x='False Positive Rate', y='True Positive Rate'),
    width=700, height=500
)
fig.add_shape(
    type='line', line=dict(dash='dash'),
    x0=0, x1=1, y0=0, y1=1
)

fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.update_xaxes(constrain='domain')
fig.show()
```

## ROC curve in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'roc-and-pr-curves', width='100%', height=630)
```

## Multiclass ROC Curve

When you have more than 2 classes, you will need to plot the ROC curve for each class separately. Make sure that you use a [one-versus-rest](https://scikit-learn.org/stable/modules/multiclass.html#one-vs-the-rest) model, or make sure that your problem has a [multi-label](https://scikit-learn.org/stable/modules/multiclass.html#multilabel-classification-format) format; otherwise, your ROC curve might not return the expected results.

```python
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score

np.random.seed(0)

# Artificially add noise to make task harder
df = px.data.iris()
samples = df.species.sample(n=50, random_state=0)
np.random.shuffle(samples.values)
df.loc[samples.index, 'species'] = samples.values

# Define the inputs and outputs
X = df.drop(columns=['species', 'species_id'])
y = df['species']

# Fit the model
model = LogisticRegression(max_iter=200)
model.fit(X, y)
y_scores = model.predict_proba(X)

# One hot encode the labels in order to plot them
y_onehot = pd.get_dummies(y, columns=model.classes_)

# Create an empty figure, and iteratively add new lines
# every time we compute a new class
fig = go.Figure()
fig.add_shape(
    type='line', line=dict(dash='dash'),
    x0=0, x1=1, y0=0, y1=1
)

for i in range(y_scores.shape[1]):
    y_true = y_onehot.iloc[:, i]
    y_score = y_scores[:, i]

    fpr, tpr, _ = roc_curve(y_true, y_score)
    auc_score = roc_auc_score(y_true, y_score)

    name = f"{y_onehot.columns[i]} (AUC={auc_score:.2f})"
    fig.add_trace(go.Scatter(x=fpr, y=tpr, name=name, mode='lines'))

fig.update_layout(
    xaxis_title='False Positive Rate',
    yaxis_title='True Positive Rate',
    yaxis=dict(scaleanchor="x", scaleratio=1),
    xaxis=dict(constrain='domain'),
    width=700, height=500
)
fig.show()
```

## Precision-Recall Curves

Plotting the PR curve is very similar to plotting the ROC curve. The following examples are slightly modified from the previous examples:

```python
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, auc
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=500, random_state=0)

model = LogisticRegression()
model.fit(X, y)
y_score = model.predict_proba(X)[:, 1]

precision, recall, thresholds = precision_recall_curve(y, y_score)

fig = px.area(
    x=recall, y=precision,
    title=f'Precision-Recall Curve (AUC={auc(fpr, tpr):.4f})',
    labels=dict(x='Recall', y='Precision'),
    width=700, height=500
)
fig.add_shape(
    type='line', line=dict(dash='dash'),
    x0=0, x1=1, y0=1, y1=0
)
fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.update_xaxes(constrain='domain')

fig.show()
```

In this example, we use the [average precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html) metric, which is an alternative scoring method to the area under the PR curve.

```python
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, average_precision_score

np.random.seed(0)

# Artificially add noise to make task harder
df = px.data.iris()
samples = df.species.sample(n=30, random_state=0)
np.random.shuffle(samples.values)
df.loc[samples.index, 'species'] = samples.values

# Define the inputs and outputs
X = df.drop(columns=['species', 'species_id'])
y = df['species']
y_onehot = pd.get_dummies(y, columns=model.classes_)

# Fit the model
model = LogisticRegression(max_iter=200)
model.fit(X, y)
y_scores = model.predict_proba(X)

# Create an empty figure, and iteratively add new lines
# every time we compute a new class
fig = go.Figure()
fig.add_shape(
    type='line', line=dict(dash='dash'),
    x0=0, x1=1, y0=1, y1=0
)

for i in range(y_scores.shape[1]):
    y_true = y_onehot.iloc[:, i]
    y_score = y_scores[:, i]

    precision, recall, _ = precision_recall_curve(y_true, y_score)
    auc_score = average_precision_score(y_true, y_score)

    name = f"{y_onehot.columns[i]} (AP={auc_score:.2f})"
    fig.add_trace(go.Scatter(x=recall, y=precision, name=name, mode='lines'))

fig.update_layout(
    xaxis_title='Recall',
    yaxis_title='Precision',
    yaxis=dict(scaleanchor="x", scaleratio=1),
    xaxis=dict(constrain='domain'),
    width=700, height=500
)
fig.show()
```

## References

Learn more about `px`, `px.area`, `px.hist`:
* https://plot.ly/python/histograms/
* https://plot.ly/python/filled-area-plots/
* https://plot.ly/python/line-charts/
