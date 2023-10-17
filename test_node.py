from node import Node

def test_node():
    node = Node("plop")
    
    assert node.__class__ == Node
    assert node.data == "plop"
    assert node.next == None

