from data_structures.binary_tree import BinaryTree
# from data_structures.hashtable import Hashtable


def tree_intersection(tree_a, tree_b):
    shared_nums = set()
    tree_a_keys = {}
    tree_a_values = BinaryTree.pre_order(tree_a)
    tree_b_values = BinaryTree.pre_order(tree_b)

    for a_value in tree_a_values:
        tree_a_keys[a_value] = None
    for b_value in tree_b_values:
        if b_value in tree_a_keys:
            shared_nums.add(b_value)

    return list(shared_nums)
