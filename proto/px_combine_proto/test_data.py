import numpy as np
import plotly.express as px
import pandas as pd

# some made up data for demos


def aug_tips():
    """ The tips data buf with "calories consumed". """
    tips = px.data.tips()
    calories = np.clip(
        tips["total_bill"] * 30 + np.random.standard_normal(tips.shape[0]) * 100,
        100,
        None,
    )
    tips["calories_consumed"] = calories
    return tips
