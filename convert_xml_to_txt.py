from __future__ import print_function
from builtins import bytes

import os
import xml.etree.ElementTree as ET
import glob

"""
This script converts XML dataset from JOS1M to NLTK-preferred plain-text set with tags separated by slashes.

It DOES NOT escape slashes so be aware of that.

The files will be grabbed in xml/ directory and will end up in txt/ subdirectory.
"""

def convert_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    out_filename = os.path.join("txt", os.path.basename(filename)) + ".txt"
    f = open(out_filename, "wb")
    print("Converting %s => %s" % (filename, out_filename))

    for div in root:
        for paragraph in div:
            for sentence in paragraph:
                for element in sentence:
                    tag = element.tag[-1]
                    if tag == 'w':
                        f.write(element.text.encode('utf-8'))
                        f.write(bytes(b'/'))
                        f.write(bytes(element.attrib["msd"], encoding="utf-8"))
                    elif tag == 'S':
                        f.write(bytes(b' '))
                    elif tag == 'c':
                        f.write(element.text.encode('utf-8'))
            f.write(bytes(b'\n\n'))
    f.close()


if __name__ == "__main__":
    files = glob.glob('xml/jos1M*.xml')
    for f in files:
        convert_file(f)
    print("Complete.")
