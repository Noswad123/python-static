class HTMLNODE:
    def __init__(self, tag, props, children, value):
        self.tag = tag
        self.props = props
        self.children = children
        self.value = value

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props = []
        for key, value in self.props.items():
            props.append(f'{key}="{value}"')
        return ' '.join(props)

    def __repr__(self):
        tag_and_props = f'{self.tag} {self.props_to_html()}'.strip(' ')
        return f'<{tag_and_props}>{self.value}</{self.tag}>'

class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props={}):
        super().__init__(tag, props, children, None)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        children_html = ''.join(child.to_html() if isinstance(child, HTMLNODE) else repr(child) for child in self.children)
        tag_and_props = f'{self.tag} {self.props_to_html()}'.strip(' ')
        return f'<{tag_and_props}>{children_html}</{self.tag}>'

class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props={}):
        super().__init__(tag, props, [], value)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return f'{self.value}'

        tag_and_props = f'{self.tag} {self.props_to_html()}'.strip(' ')
        return f'<{tag_and_props}>{self.value}</{self.tag}>'

