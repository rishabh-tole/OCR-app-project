# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import nltk
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"



class Summary():

    def __innit__(self):
        LANGUAGE = "english"

    def summarize_doc(self,bullets=3):
        parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        master = ""
        sentence_counter=0
        for sentence in summarizer(parser.document, bullets):
            print(sentence)
            master = str(master)+str(sentence)
            sentence_counter+=1

        print(sentence_counter)
        return master
    
    def summarize_website(self, url, bullets=3):
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

        stemmer = Stemmer(LANGUAGE)


        summarizer = Summarizer(stemmer)

        summarizer.stop_words = get_stop_words(LANGUAGE)
        master = ""
        for sentence in summarizer(parser.document, bullets):
            master = str(master)+str(sentence)

        return master
