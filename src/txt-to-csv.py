#!/usr/bin/env python

import pyprind
import pandas as pd
import os
import numpy as np

BASE_PATH = 'aclImdb'


def walk_dir_combine_inputs(files_path):
    """
    Walk directory and combine raw imdb files into a dataframe

    aclImdb/train/pos
    aclImdb/train/pos

    aclImdb
    ├── imdbEr.txt
    ├── imdb.vocab
    ├── README
    ├── test
    │   ├── labeledBow.feat
    │   ├── neg
    │   ├── pos
    │   ├── urls_neg.txt
    │   └── urls_pos.txt
    └── train
        ├── labeledBow.feat
        ├── neg
        ├── pos
        ├── unsupBow.feat
        ├── urls_neg.txt
        ├── urls_pos.txt
        └── urls_unsup.txt


    Parameters
    ----------
    files_path

    Returns
    -------

    """
    labels = {'pos': 1, 'neg': 0}
    progress_bar = pyprind.ProgBar(25000)
    df = pd.DataFrame()

    for sub_path in ('pos', 'neg'):
        path = os.path.join(BASE_PATH, files_path, sub_path)
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as infile:
                txt = infile.read()
            df = df.append([[txt, labels[sub_path]]], ignore_index=True)
            progress_bar.update()

    df.columns = ['Review', 'Label']
    np.random.seed(0)

    df = df.reindex(np.random.permutation(df.index))
    return df


dataframe = walk_dir_combine_inputs('train')
dataframe.to_csv(f'Imdb_Reviews_Train.csv', index=False, encoding='utf-8')

dataframe = walk_dir_combine_inputs('test')
dataframe.to_csv(f'Imdb_Reviews_Test.csv', index=False, encoding='utf-8')
