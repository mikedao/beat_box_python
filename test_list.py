from list import List
from node import Node

def test_list():
    list = List()

    assert list.__class__ == List
    assert list.head == None

def test_append():
    list = List()
    
    list.append("doop")

    assert list.head.__class__ == Node

def test_count():
    list = List()

    list.append("doop")
    list.append("deep")
    list.append("dip")
    list.append("dop")

    assert list.count() == 4

def test_to_string():
    list = List()

    list.append("doop")
    list.append("deep")
    list.append("dip")
    list.append("dop")

    assert list.to_string() == "doop deep dip dop"
