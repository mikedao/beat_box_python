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

def test_insert():
    list = List()

    list.append("doop")
    list.append("deep")
    list.append("dip")
    list.append("dop")

    list.insert(2, "derp")

    assert list.to_string() == "doop deep derp dip dop"

def test_prepend():
    list = List()

    list.append("doop")
    list.append("deep")
    list.append("dip")
    list.append("dop")

    list.prepend("derp")

    assert list.to_string() == "derp doop deep dip dop"

def test_find():
    list = List()

    list.append("doop")
    list.append("deep")
    list.append("dip")
    list.append("dop")

    result = list.find(2 ,1)

    assert result == "deep"

    result = list.find(2, 2)

    assert result == "deep dip"

def test_pop():
    list = List()

    list.append("doop")
    list.append("deep")
    list.append("dip")
    list.append("dop")

    result = list.pop()

    assert result == "dop"

    assert list.to_string() == "doop deep dip"

def test_includes():
    list = List()

    list.append("doop")
    list.append("deep")
    list.append("dip")
    list.append("dop")

    result = list.includes("deep")

    assert result == True

    result = list.includes("derp")

    assert result == False
