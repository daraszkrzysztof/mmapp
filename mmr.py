#!/usr/bin/env python3

import xml.etree.ElementTree as ETree
import sys


def remove_node(mmFile, searchText, childSubstring):
    with open(mmFile, 'rb') as sourceFile:
        tree = ETree.parse(sourceFile)
        root = tree.getroot()
        pathQuery = ".//node[@TEXT='{}']".format(searchText)
        foundElement = root.findall(pathQuery)

    foundElement.reverse()

    if not foundElement or foundElement is None:
        print("couldn't find parent element or it doesn't have children")
    else:
        for childElement in foundElement:
            if childElement.attrib.get("TEXT").startswith(childSubstring):
                foundElement.remove(childElement)
                resultData = ETree.tostring(root)
                resultFile = open(mmFile, "w")
                resultFile.write(resultData.decode("utf-8"))


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print('Requires : file name, parent node name, child name substring, instead of ', len(sys.argv))
        exit()

    mmFile = sys.argv[1]
    searchText = sys.argv[2]
    childSubstring = sys.argv[3]

    remove_node(mmFile, searchText, childSubstring)
