from transform import parse_nodes


def test_parse_nodes():
    result = parse_nodes("test.mm")

    assert 'terminologia' in result.children.keys()
    l1_node = result.children['terminologia']
    assert 'performance' in l1_node.children.keys()
    l2_node = l1_node.children['performance']
    assert l2_node.p.p.p is None


def test_find_first():
    root = parse_nodes("test.mm")
    (txt, scalabilityNode) = root.find_first("scalability")

    assert txt == "scalability"
    assert scalabilityNode.p.p.p == root


def test_breadcrumbs():
    root = parse_nodes("test.mm")
    (txt, scalabilityNode) = root.find_first("scalability")

    assert scalabilityNode.breadcrumb() == "terminologia/performance/scalability"
