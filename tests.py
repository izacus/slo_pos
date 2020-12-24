# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import slopos

class TestTagger(unittest.TestCase):

    def setUp(self):
        slopos.load_from_path("prebuilt/sl-tagger.pickle")

    def testSentenceTagging(self):
        tagged = slopos.tag("To je test.")
        self.assertEqual(tagged, [('To', 'ZK-SEI'), ('je', 'GP-STE-N'), ('test', 'SOMETN'), ('.', '-None-')])

    def testListTagging(self):
        tagged = slopos.tag(["To", "je", "test"])
        self.assertEqual(tagged, [('To', 'ZK-SEI'), ('je', 'GP-STE-N'), ('test', 'SOMETN')])

    def testUnicodeSentenceTagging(self):
        tagged = slopos.tag("V kožuščku zelene lisice stopiclja jezen otrok.")
        self.assertEqual(tagged, [('V', 'DM'), ('kožuščku', 'SOMEM'), ('zelene', 'PPNZER'), ('lisice', 'SOZER,'),
                                  ('stopiclja', 'GGNSTE'), ('jezen', 'PPNMEIN'), ('otrok', 'SOMEI.'), ('.', '-None-')])

if __name__ == "__main__":
    unittest.main()


