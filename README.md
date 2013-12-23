# NLTK Slovenian POS tagger

This is a project that uses [IJS JOS-1M corpus][1] to train a part-of-speech tagger for Slovenian language.

## Prepared files

The corpus was processed in several ways to prepare it for NLTK consumption. Partial files are part of this repository.

1. Original corpus

   Original corpus is stored in multple split XML files, which are here stored in `xml` directory.

2. Partial text files

   XML files have been processed and converted into a NLTK readable word/tag format using `convert_xml_to_txt.py` script. The processed files are stored in `txt` directory.

3. NLTK tagged corpus

   Files from `txt` directory have been combined into a single file and stored in `data/tagged_corpus` directory for nltk-trainer consumption.
   
## Training the POS tagger

POS tagger is trained using nltk-trainer project, which is included as a submodule in this project. 

### Install dependencies

```
virtualenv .
pip install -r requirements
pip install numpy
python nltk-trainer/setup.py install
```

### Train

In top project directory run the trainer:

```
python nltk-trainer/train_tagger.py data/tagged_corpus --reader nltk.corpus.reader.tagged.TaggedCorpusReader --
```

It'll take a short while and you should see output in form of

```
loading data/tagged_corpus
15758 tagged sents, training on 15758
training AffixTagger with affix -3 and backoff <DefaultTagger: tag=-None->
training <class 'nltk.tag.sequential.UnigramTagger'> tagger with backoff <AffixTagger: size=11492>
training <class 'nltk.tag.sequential.BigramTagger'> tagger with backoff <UnigramTagger: size=109127>
training <class 'nltk.tag.sequential.TrigramTagger'> tagger with backoff <BigramTagger: size=130795>
evaluating TrigramTagger
accuracy: 0.930942
creating directory out
dumping TrigramTagger to out/sl-tagger.pickle
```

The trained tagger will be deposited in `out` directory with name of `sl-tagger.pickle`.

## Using the POS tagger

POS tagger is stored in form of Python pickle file after creation and you will need NLTK installed.

Usage:

```
import pickle
sl_tagger = pickle.load('out/sl-tagger.pickle)

sl_tagger.tag(["Jaz", "sem", "iz", "okolice", "Ljubljane"])

> [('Jaz', 'ZOP-EI'),
 ('sem', 'GP-SPE-N'),
 ('iz', 'DR'),
 ('okolice', 'SOZER'),
 ('Ljubljane', 'SLZER.')]

```

Note that punctionation should be stripped from words for proper detection. Tag reference is contained in `tag_reference-sl.txt` (slovenian) and `tag_reference-en.txt` files respectively.


 [1]: http://nl.ijs.si/jos/jos1M-sl.html