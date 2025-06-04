from graphviz import Digraph

def visualize_ast(ast, filename='ast'):
    dot = Digraph(comment='AST')
    node_id = [0]

    def add_nodes(node, parent=None):
        my_id = str(node_id[0])
        node_id[0] += 1
        label = str(node[0]) if isinstance(node, (list, tuple)) else str(node)
        dot.node(my_id, label)
        if parent is not None:
            dot.edge(parent, my_id)
        if isinstance(node, (list, tuple)):
            for child in node[1:]:
                add_nodes(child, my_id)
    add_nodes(ast)
    dot.render(filename, view=True, format='png')