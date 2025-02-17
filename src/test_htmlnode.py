import unittest
from htmlnode import HTMLNODE, LeafNode, ParentNode

class TestHTMLNODE(unittest.TestCase):
    def test_basic_tag(self):
        node = HTMLNODE("p", {}, [], "Hello")
        self.assertEqual(repr(node), '<p>Hello</p>')

    def test_tag_with_props(self):
        node = HTMLNODE("a", {"href": "https://example.com", "target": "_blank"}, [], "Click here")
        self.assertEqual(repr(node), '<a href="https://example.com" target="_blank">Click here</a>')

    def test_empty_props(self):
        node = HTMLNODE("div", {}, [], "")
        self.assertEqual(repr(node), '<div></div>')

    def test_multiple_props(self):
        node = HTMLNODE("button", {"class": "btn btn-primary", "disabled": "true"}, [], "Submit")
        self.assertEqual(repr(node), '<button class="btn btn-primary" disabled="true">Submit</button>')

    def test_no_value(self):
        node = HTMLNODE("br", {}, [], '')
        self.assertEqual(repr(node), '<br></br>')   

    def test_leaf_node(self):
        node = LeafNode("h1", "Hello", {"class": "header"})
        self.assertEqual(node.to_html(), '<h1 class="header">Hello</h1>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", 'child')
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", 'grandchild')
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
