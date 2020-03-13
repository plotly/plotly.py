---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
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
      Characteristics (ROC) and Precision-Recall (PR) Curves using Plotly on Python.
    display_as: ai_ml
    language: python
    layout: base
    name: ROC and PR Curves
    order: 3
    page_type: example_index
    permalink: python/roc-and-pr-curves/
    thumbnail: thumbnail/ml-roc-pr.png
---

## Basic Binary ROC Curve

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
    labels=dict(x='False Positive Rate', y='True Positive Rate')
)
fig.add_shape(
    type='line', line=dict(dash='dash'), 
    x0=0, x1=1, y0=0, y1=1
)
fig.show()
```

## Multiclass ROC Curve

When you have more than 2 classes, you will need to plot the ROC curve for each class separately. Make sure that you use a [one-versus-rest](https://scikit-learn.org/stable/modules/multiclass.html#one-vs-the-rest) model, or make sure that your problem has a [multi-label](https://scikit-learn.org/stable/modules/multiclass.html#multilabel-classification-format) format; otherwise, your ROC curve might not return the expected results.

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
import plotly.graph_objects as go
import plotly.express as px

np.random.seed(0)

# Artificially add noise to make task harder
df = px.data.iris()
samples = df.species.sample(n=50, random_state=0)
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
    yaxis_title='True Positive Rate'
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
    labels=dict(x='Recall', y='Precision')
)
fig.add_shape(
    type='line', line=dict(dash='dash'), 
    x0=0, x1=1, y0=1, y1=0
)
fig.show()
```

In this example, we use the [average precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html) metric, which is an alternative scoring method to the area under the PR curve.

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, average_precision_score
import plotly.graph_objects as go
import plotly.express as px

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
    yaxis_title='Precision'
)
fig.show()
```
