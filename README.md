# Imdb Txt 2 Csv

Working with the [text classification tutorial](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub)
The dataset is built-in to TensorFlow, but I wanted to download it and compare performance to Dotnet's AutoML, 
because 'why not?' The dataset is available online [here](https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz),
but the format is a little odd.

```
./download_untar_imdb_sentiment.sh

tree aclImdb -L 2

    aclImdb/
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
```

Positive review for training are in the 'pos' folder, ex: aclImdb/train/pos/127_7.txt
Dotnet requires a single csv with positive/negative labelled inputs, so this script walks the folders and creates that.

```
 ./txt-to-csv.py
 
    Imdb_Reviews_Test.csv
    Imdb_Reviews_Train.csv
```