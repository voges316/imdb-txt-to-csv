#!/bin/bash

# download and unpack imdb database in current directory
wget -c https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz -O - | tar -xz