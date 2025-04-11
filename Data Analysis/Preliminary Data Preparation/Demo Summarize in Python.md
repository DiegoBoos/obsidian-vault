Basic set up

```Python
# Basic set up

# Clear plots and variables (manually skipped since Jupyter does not allow full reset in script)
# import matplotlib.pyplot as plt
# plt.close('all')

# Clear console (can be done in Jupyter via Ctrl+L or %clear)
# print("\033[H\033[J")

# Remove all variables (only relevant in scripts)
# %reset -f  # Only in IPython

import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)  # equivalent to scipen in R
```

Loading packages

```Python
import pandas as pd
import numpy as np
from scipy import stats
```

Loading the Dataset

```Python
df = pd.read_csv("df.csv", header=0, sep=",")
df = pd.DataFrame(df)
df.head(5)
```

 Rename all the Variables
 
```Python
df_DABO = df.copy()
df_DABO.columns = [col + "_DABO" for col in df.columns]
df_DABO.head(10)
```

Transforming categorical variables to a factor variables

```Python
df_DABO["plant_DABO"] = df_DABO["plant_DABO"].astype("category")
```

Data summary

```Python
from scipy.stats import describe

df_summary_DABO = df_DABO.describe(include="all").T  # Basic summary
df_summary_DABO.round(2)
```