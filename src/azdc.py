#-*- coding: UTF-8 -*-
import pandas as pd
src_file = '../Data/raw/AZDC_6-26-2009_2.txt'

def read_content():
  with open(src_file, encoding='utf8') as f:
    lines = list(map(lambda l:l.split('\t')[:-2], f.read().splitlines()))
    column_names = lines[0]
    column_values = lines[1:]
    data = {}
    for i,col_name in enumerate(column_names):
      data[col_name] = [val[i] for val in column_values]
    df = pd.DataFrame(data, columns=column_names)
    df.to_csv('../Data/processed/azdc.csv')

if __name__ == '__main__':
  read_content()
