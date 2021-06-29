



from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import nltk
nltk.download("punkt")

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 10


def summarize_website(url):
  parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    
  stemmer = Stemmer(LANGUAGE)

  summarizer = Summarizer(stemmer)
  summarizer.stop_words = get_stop_words(LANGUAGE)

  for sentence in summarizer(parser.document, SENTENCES_COUNT):
      
      print(" - ",sentence)