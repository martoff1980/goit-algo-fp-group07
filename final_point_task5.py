from collections import deque
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import math


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def basic_bypass(node):
    current = node
    if current is None:
        return current

    if current.left is None:
        return current

    if current.right is None:
        return current

    if current.left.val > current.right.val:
        if (current.left.val > current.val):
            temp = current.val
            temp_color = collection_colors[current.id]
            temp_left = current.left.val
            temp_left_color = collection_colors[current.left.id]
            current.left.val = temp
            current.left.color = temp_color
            current.val = temp_left
            current.color = temp_left_color
        return current

    else:
        if (current.right.val > current.val):
            temp = current.val
            temp_color = collection_colors[current.id]
            temp_right = current.right.val
            temp_right_color = collection_colors[current.right.id]
            current.right.val = temp
            current.right.color = temp_color
            current.val = temp_right
            current.color = temp_right_color

        return current


def left_bypass(node):
    current = node

    if current.left.left.val > current.left.val:
        if current.left.left.val > current.left.right.val:
            temp = current.left.val
            temp_color = collection_colors[current.left.id]
            temp_left = current.left.left.val
            temp_left_color = collection_colors[current.left.left.id]
            current.left.left.val = temp
            current.left.left.color = temp_color
            current.left.val = temp_left
            current.left.color = temp_left_color
        else:
            temp = current.left.val
            temp_color = collection_colors[current.left.id]
            temp_right = current.left.right.val
            temp_right_color = collection_colors[current.left.right.id]
            current.left.right.val = temp
            current.left.right.color = temp_color
            current.left.val = temp_right
            current.left.color = temp_right_color
        return current

    else:
        if (current.left.right.val > current.left.val):
            temp = current.left.val
            temp_color = collection_colors[current.left.id]
            temp_right = current.left.right.val
            temp_right_color = collection_colors[current.left.right.id]
            current.left.right.val = temp
            current.left.right.color = temp_color
            current.left.val = temp_right
            current.left.color = temp_left_color
        return current


def right_bypass(node):
    current = node
    if current.right.right is None:
        if current.right.left.val > current.right.val:
            temp = current.right.left.val
            temp_color = collection_colors[current.right.left.id]
            temp_left = current.right.val
            temp_left_color = collection_colors[current.right.id]
            current.right.val = temp
            current.right.color = temp_color
            current.right.left.val = temp_left
            current.right.left.color = temp_left_color
        return current

    if current.right.left.val > current.right.right.val:
        if current.right.left.val > current.right.right.val:
            temp = current.right.val
            temp_color = collection_colors[current.right.id]
            temp_left = current.right.left.val
            temp_left_color = collection_colors[current.right.left.id]
            current.right.val = temp_left
            current.right.color = temp_left_color
            current.right.left.val = temp
            current.right.left.color = temp_color
        return current

    else:
        if current.right.right.val > current.right.val:
            temp = current.right.val
            temp_color = collection_colors[current.right.id]
            temp_right = current.right.right.val
            temp_right_color = collection_colors[current.right.right.id]
            current.right.right.val = temp
            current.right.right.color = temp_color
            current.right.val = temp_right
            current.right.color = temp_right_color

        return current


def generate_color(index):
    # Генерує колір у форматі RGB залежно від порядкового номера.
    color_value = hex(min(255, index * 15))[2:].zfill(2)
    color_value1 = hex(index * 45)[2:].zfill(2)
    return f"#{color_value}96{color_value1}"


def generate_colors(tree_root):
    stack = [tree_root]
    colors = {}
    index = 0

    while stack:
        node = stack.pop()
        if node:
            colors[node.id] = generate_color(index)
            index += 1
            stack.append(node.right)
            stack.append(node.left)

    return colors


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
# Відображення дерева
draw_tree(root)


# Відображення кольорів дерева
collection_colors = generate_colors(root)

# Проходи винонуються знизу до верху за допомогою DFS
# На вершині пераміди вузел зі значенням Макс=10
# Проходи будуть навідь зайвими, але це зроблено навмисно
# для розуміння побудови бінарних дерев
root = left_bypass(root)
draw_tree(root)

root = right_bypass(root)
draw_tree(root)

root = basic_bypass(root)
draw_tree(root)

root = left_bypass(root)
draw_tree(root)

root = right_bypass(root)
draw_tree(root)

root = basic_bypass(root)
draw_tree(root)
