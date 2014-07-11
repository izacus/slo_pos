# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import slopos

class TestTagger(unittest.TestCase):

    def testSentenceTagging(self):
        tagged = slopos.tag("To je test.")
        self.assertEqual(tagged, [('To', 'ZK-SEI'), ('je', 'GP-STE-N'), ('test', 'SOMETN'), ('.', '.')])

    def testListTagging(self):
        tagged = slopos.tag(["To", "je", "test"])
        self.assertEqual(tagged, [('To', 'ZK-SEI'), ('je', 'GP-STE-N'), ('test', 'SOMETN')])

    def testUnicodeSentenceTagging(self):
        tagged = slopos.tag("To še test.")
        self.assertEqual(tagged, [('To', 'ZK-SEI'), ('še', '-None-'), ('test', 'SOMETN'), ('.', '.')])

if __name__ == "__main__":
    unittest.main()


