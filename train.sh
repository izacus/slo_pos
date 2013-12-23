#!/bin/sh
python nltk-trainer/train_tagger.py data/tagged_corpus --reader nltk.corpus.reader.tagged.TaggedCorpusReader --filename out/sl-tagger.pickle