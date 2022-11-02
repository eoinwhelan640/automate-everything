import pandas as pd
import numpy as np

data = {'AA':[1, np.nan, 3, 4, 5],
        'BB':[10, np.nan, 30, np.nan, np.nan],
        'CC':[100, np.nan, 300, 400, 500]
        }
df = pd.DataFrame(data)
# look at your df and it has a few nulls in places
df

# apply a simple conditional statement, ask where the values in column A of df is more than 2.
# The result is some true/false values representing within column. Think of these as on/off buttons or
# activated/deactivated nodes - True=on, False=off. The first two values are off, the last 3 are on
df["AA"] > 2

# You can use the list of on/off values to index into the dataframe. kind of like saying, give me the rows
# where my values are "activated" based on the condition I gave you (the val in AA being bigger than 2)
df[df["AA"] > 2]
# For now you dont have to worry about loc, just that it does the same thing as the above for indexing.
# When you go onto do more complicated stuff you can use loc better, but for now it's the exact same
df.loc[ df["AA"] > 2]

# So now you're applying your index conditional, then using that to get "on" rows of the full dataframe. With that
# subset of data, you're using isna() to check which values in the whole thing are nulls
# You get out another true/false matrix
# Also doing 'df.AA >2' is exact same as doing 'df["AA"]>2'
df.loc[ df["AA"] > 2]
df.loc[ df["AA"] > 2].isna()

# Now you're saying you just want to see column "BB" where you've applied this test for null values
df.loc[ df["AA"] > 2, "BB"].isna()

# now you're saying, i'm only interested in where my condition is met and specifically the column B and I'm going to
# apply the function "fillna(10000)" here to fill all the nulls in that subset of data - fill with the value 10000
df.loc[ df["AA"] > 2, "BB"].fillna(10000)
# Print the df out and nothing has changed, even though we just filled the values
df

# this is because we never reassigned it, so you need to say
# The subset of my dataframe where AA >2 and specifically under column "BB" = That same section of data but with the
# nulls filled in as 10000
df.loc[ df["AA"] > 2, "BB"] = df.loc[ df["AA"] > 2, "BB"].fillna(10000)
# now can see it changed
df