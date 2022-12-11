import sys

from Parser.node import Node


class ParserOutput:
    def __init__(self, parser, sequence, output=""):
        self.root = None
        self.parser = parser
        self.node_number = 1
        self.node_list = []
        self.output = output
        self.productions = parser.analyze_sequence(sequence)
        self.generate_tree()

    def generate_tree(self):
        node_stack = []
        prod_index = 0

        node = Node(0, 0, False, self.node_number, self.parser.grammar.S)
        self.node_number += 1
        node_stack.append(node)
        self.node_list.append(node)
        self.root = node
        while len(node_stack) > 0 and prod_index < len(self.productions):
            current = node_stack[len(node_stack) - 1]
            if current.value in self.parser.grammar.E or 'epsilon' in current.value:
                while len(node_stack) > 0 and node_stack[len(node_stack) - 1].has_right is False:
                    node_stack.pop()
                if len(node_stack) > 0:
                    node_stack.pop()
                else:
                    break
                continue

            production = self.productions[prod_index][0]
            self.node_number += len(production) - 1
            for i in range(len(production) - 1, -1, -1):
                if i == 0:
                    sibling = 0
                else:
                    sibling = self.node_number - 1
                child = Node(current.index, sibling, i != len(production) - 1, self.node_number, production[i])
                self.node_number -= 1
                node_stack.append(child)
                self.node_list.append(child)

            self.node_number += len(production) + 1
            prod_index += 1

    def print_tree(self):
        try:
            sorted_node_list = sorted(self.node_list, key=lambda x: x.index)
            for node in sorted_node_list:
                print("Node(" + str(node.index) + "," + node.value + "," + str(node.parent) + "," + str(node.sibling) + ")")
        except Exception as e:
            print(e)

    def print_tree_to_file(self):
        try:
            original_stdout = sys.stdout
            with open(self.output, 'w') as f:
                sys.stdout = f
                sorted_node_list = sorted(self.node_list, key=lambda x: x.index)
                for node in sorted_node_list:
                    print("Node(" + str(node.index) + "," + node.value + "," + str(node.parent) + "," + str(
                        node.sibling) + ")")
                sys.stdout = original_stdout
        except Exception as e:
            print(e)
