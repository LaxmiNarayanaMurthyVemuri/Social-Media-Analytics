import pandas as pd
import numpy as np
cart={"product":["Mobile","Laptop","Washingmachine","car"],"price":[20000,45000,47000,120000],"Type":["electriconics","elect","cleaning","Machine"]}
df=pd.DataFrame(cart)
varname=df.loc[df["price"]==20000]
print(varname["price"])