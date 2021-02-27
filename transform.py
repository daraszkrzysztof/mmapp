#!/usr/bin/env python3
import re
import xml.etree.ElementTree as ETree
from xml.etree.ElementTree import Element


class Layer(object):

    def __init__(self, children, parent=None):
        self.children = {
            child.attrib["TEXT"]: child.findall("./node")
            for child in children
        }
        self.p = parent

    def breadcrumb(self) -> str:
        stack = []
        parent = self.p
        current_layer = self
        while parent:
            for key, value in parent.children.items():
                if current_layer == value:
                    stack.append(key)
                    break
            current_layer = parent
            parent = current_layer.p

        return '/'.join(stack[::-1])

    def find_first(self, expr: str):

        queue = []
        queue.append(self)

        while len(queue) > 0:
            layer = queue.pop();
            for key in layer.children.keys():
                if re.search(expr, key, re.IGNORECASE):
                    return key, layer.children[key]
                else:
                    queue.append(layer.children[key])


def transform(root: Element, tagName: str) -> Layer:
    root = root.findall("./{}".format(tagName))
    root_layer = Layer(root)
    layer = root_layer
    stack = []
    while True:
        for item in layer.children.items():
            if len(item[1]) > 0:
                stack.append((layer, item))

        if len(stack) == 0:
            break

        layer_tuple = stack.pop()

        parent_layer = layer_tuple[0]
        node = layer_tuple[1]
        layer = Layer(node[1], parent_layer);
        parent_layer.children[node[0]] = layer

    return root_layer


def parse_nodes(path: str) -> Layer:
    tree = ETree.parse(path)
    root = tree.getroot()
    return transform(root, "node")
