#!/bin/sh
python nltk-trainer/train_tagger.py data/tagged_corpus --reader nltk.corpus.reader.tagged.TaggedCorpusReader --filename slopos/sl-tagger.pickle
