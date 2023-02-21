# Functional req:
# Need to instantiate with initial nodes
# Possibly need to keep tack of existing nodes - so that we can:
#     choose a node for a key
#     remove a node
#
# Need to track corresponding keys (in any order) of a node so that we can:
#     assign its keys to other node(s)
#     we can get all its keys
#
# Need to assign nodes with seq increasing ids (by 1)
import random
from collections import defaultdict

class ConsistentHashing:
    def __init__(self, initialNodes):
        self.next_node_id = 1
        self.nodes = []
        for _ in range(initialNodes):
            self.nodes.append(self.next_node_id)
            self.next_node_id += 1
        self.node_to_keys = defaultdict(set)
        self.keys_to_nodes = defaultdict(set)

    def assign_keys_to_node(self, keys, node):
        for key in keys:
            self.node_to_keys[node].add(key)
            self.keys_to_nodes[key].add(node)

    def getNodeForKey(self, key):
        if key in self.keys_to_nodes and self.keys_to_nodes[key]:
            return random.choice(list(self.keys_to_node[key]))
        else:
            node_to_take_burden = random.choice(self.nodes)
            self.assign_keys_to_node([key], node_to_take_burden)
            return node_to_take_burden

    def removeNode(self, node):
        keys_to_redistribute = self.node_to_keys[node]
        self.node_to_keys[node] = []
        self.nodes.remove(node)

        for key in keys_to_redistribute:
            self.keys_to_nodes[key].remove(node)

        node_to_take_burdern = random.choice(self.nodes)
        self.assign_keys_to_node(keys_to_redistribute, node_to_take_burdern)
        return node_to_take_burdern

    def addNode(self):
        node_to_be_supported = random.choice(self.nodes)
        keys_of_node_to_be_supported = self.node_to_keys[node_to_be_supported]
        new_node_id = self.next_node_id
        self.next_node_id += 1
        self.nodes.append(new_node_id)
        self.assign_keys_to_node(keys_of_node_to_be_supported, new_node_id)
        return (new_node_id, node_to_be_supported)

