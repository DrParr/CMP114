import pingouin as pg
import pandas as pd

# You might need to install the pingouin package
# This is done with > pip install pingouin
# Pip is the python package manager
# If you're using spyder, you need to restart the kernel

pd.set_option('display.float_format', '{:.10f}'.format)

#1. Load your data
df = pd.read_csv("filename.csv")

# 2. Run the Two-Way ANOVA in ONE line
aov = pg.anova(data=df, dv='data_column', between=['group1', 'group2'], detailed=True)

# 3. Print the ANOVA table
print(aov)
