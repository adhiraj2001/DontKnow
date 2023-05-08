import mysql.connector
import os
import glob
import pandas as pd
def convert_to_int(my_string):
    ascii_values = [str(ord(char)) for char in my_string]
    power = 0
    val = 0
    for ele in ascii_values:
        val += int(ele) * (10 ** power)
        power += 1
    return val



def combine_files():
    data_folder = './'
    dataset = 'CamCAN-IDPs'

    df_ref = pd.DataFrame()

    df_list = []

    for x in sorted(glob.glob(f'{data_folder}/{dataset}/*.tsv', recursive = True)):
        name = x.rsplit('.', 1)[0].split('-', 4)[-1]
        hs = name.rsplit('-', 1)[-1]
        df = pd.read_csv(x, sep='\t')
            # df = df.iloc[:1, :4]
        df.rename(columns={df.columns[0]: 'subject_id'}, inplace = True)
        df.rename(columns={df.columns[-(1 + (hs == 'rh'))]: f"{name}_{df.columns[-(1 + (hs == 'rh'))]}"}, inplace = True)
        df.rename(columns={df.columns[-(2 + (hs == 'rh'))]: f"{name}_{df.columns[-(2 + (hs == 'rh'))]}"}, inplace = True)
        #print(df)
        df_list.append(df)

    
    df_merge = df_list[0]
    for i in range(1,len(df_list)):
        df_merge = pd.merge(df_merge, df_list[i], on='subject_id')

    return df_merge