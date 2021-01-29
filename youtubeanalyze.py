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
# Checking data types
ca.dtypes
# %%
# Checking 2 cols types that need to be updated
ca[['trending_date','publish_time']].head()
# %%
# Update publish time to datetime
ca['publish_time'] = ca['publish_time'].astype('datetime64[ns]')

# %%
# Append '20' in front then reformat trending date & set proper date col order
ca['trending_date'] = ['20'] + ca['trending_date']
ca['trending_date'] = pd.to_datetime(ca['trending_date'], format = "%Y.%d.%m")
# %%

# %%
