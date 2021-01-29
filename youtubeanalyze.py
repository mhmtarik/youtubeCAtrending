# %%
import pandas as pd
import seaborn as sns
import numpy as nm
import plotly.express as px
import seaborn as sns
sns.set(style='darkgrid')

# %%
# Importing the data source
ca = pd.read_csv("C:/Users/tarik.mahmood/Documents/PYTHON/youtubeCAtrending/CAvideos.csv")

# %%
# Checking data cols & rows
ca.shape
# %%
# Listing the cols
ca.columns
# %%
# Getting rid of redundant cols.
ca.drop(['video_id','thumbnail_link', 'description'], axis=1, inplace=True)
# %%
