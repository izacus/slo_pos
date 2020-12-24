from __future__ import print_function
from builtins import bytes

import os
import xml.etree.ElementTree as ET
import glob
import shutil

"""
This script converts XML dataset from JOS1M to NLTK-preferred plain-text set with tags separated by slashes.

It DOES NOT escape slashes so be aware of that.

The files will be grabbed in xml/ directory and will end up in txt/ subdirectory.
"""

def convert_xml_file(filename):
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

def concat_outputs():
    files = glob.glob("txt/jos1M*.txt")
    output_file = os.path.join("data", "tagged_corpus", "slotag.txt")
    print("Concatenating to", output_file)
    with open(output_file, "wb") as out_f:
        for f in files:
            with open(f, "rb") as in_f:
                shutil.copyfileobj(in_f, out_f)

if __name__ == "__main__":
    print("Converting XML files to TXT format...")
    files = glob.glob('xml/jos1M*.xml')
    for f in files:
        convert_xml_file(f)
    print("Concatenating TXT files into a single output...")
    concat_outputs()
    print("Complete.")
