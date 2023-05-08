from helper import combine_files
import pandas as pd
from insert_to_sql import *

df_merge = combine_files()
 
# printing data
columns = list(df_merge.columns)
rows = df_merge.values.tolist()
#insert all the fields
insert_fields(columns)
#What is the type of sample that is being collected
create_sample()
#inserting all the samples
for row in rows:
    insert_row(row,columns)