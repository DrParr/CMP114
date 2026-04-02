import pandas as pd
from scipy.stats import f_oneway, kruskal

# Import the data from 
data = pd.read_csv('')

# we can group the data by drug type
grouped = data.groupby('')

# How many groups do we have? How many in each group?
print(grouped.count())


#=============================================================
# One way ANOVA
#=============================================================




#=============================================================
# Kruskal Wallis
#=============================================================



#=============================================================
# Tukey HSD Post-hoc Test
#=============================================================



#=============================================================
# Dunnett's Post-hoc Test
#=============================================================
