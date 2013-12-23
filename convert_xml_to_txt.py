import xml.etree.ElementTree as ET
import glob

"""
This script converts XML dataset from JOS1M to NLTK-preferred plain-text set with tags separated by slashes.

It DOES NOT escape slashes so be aware of that.
"""

def convert_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    f = open(filename + ".txt", "wb")

    for div in root:
        for paragraph in div:
            for sentence in paragraph:
                for element in sentence:
                    tag = element.tag[-1]
                    if tag == 'w':
                        f.write(element.text.encode('utf-8'))
                        f.write('/')
                        f.write(element.attrib["msd"])
                    elif tag == 'S':
                        f.write(' ')
                    elif tag == 'c':
                        f.write(element.text.encode('utf-8'))
            f.write('\n\n')
    f.close()


files = glob.glob('jos1M*.xml')

for f in files:
    print "Converting", f
    convert_file(f)
