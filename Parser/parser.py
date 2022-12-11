from Grammar.grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar('../Grammar/first_grammar.in')
        self.first = {}
        self.follow = {}
        self.parserTable = {}
        self.numberedProductions = []
        self.get_all_first()
        self.get_all_follow()
        self.number_productions()
        self.generate_parser_table()

    def get_all_first(self):
        for non_term in self.grammar.N:
            self.first[non_term] = self.get_first(non_term)

    def get_all_follow(self):
        for non_term in self.grammar.N:
            self.follow[non_term] = self.get_follow(non_term)

    def get_first(self, non_terminal):
        if non_terminal in self.grammar.E:
            return set(non_terminal)
        aux = set()
        for prod in self.grammar.get_productions_for_non_terminal(non_terminal):
            if prod[0] in self.grammar.E or prod[0] == 'epsilon':
                aux.add(prod[0])
            else:
                for i in range(len(prod)):
                    rule = prod[i]
                    if rule in self.grammar.N:
                        check = True
                        for j in range(i):
                            if 'epsilon' not in self.get_first(prod[j]):
                                check = False
                        if check is True:
                            try:
                                for e in self.get_first(rule):
                                    aux.add(e)
                            except Exception:
                                print("Invalid file! Conflict! ", prod)
                                return

        return aux

    def get_follow(self, non_terminal):
        res = set()
        if non_terminal == self.grammar.S:
            res.add('$')
        for prod in self.grammar.get_productions_containing_non_terminal(non_terminal):
            start = prod[0][0]
            rule = prod[1]
            for i in range(len(rule)):
                term = rule[i]
                if term == non_terminal:
                    if i < (len(rule) - 1):
                        first_next = self.get_first(rule[i + 1])
                        for e in first_next:
                            if e != 'epsilon':
                                res.add(e)
                        if 'epsilon' in first_next:
                            for f in self.get_follow(start):
                                res.add(f)
                    else:
                        # print(non_terminal, start)
                        if start != non_terminal:
                            for f in self.get_follow(start):
                                res.add(f)
        return res

    def number_productions(self):
        index = 1
        for production in self.grammar.P:
            start = production[0]
            rules = production[1]
            for rule in rules:
                self.numberedProductions.append(((start, rule), index))
                index += 1

    def generate_parser_table(self):
        for a in self.grammar.E:
            if a == 'epsilon':
                res = 'acc'
            else:
                res = 'pop'
            self.parserTable[(a, a)] = res

        for mainProd in self.numberedProductions:
            prod = mainProd[0]
            index = mainProd[1]
            for a in self.get_first_concat(prod[1]):
                if isinstance(a, list):
                    a = tuple(a)
                if (prod[0][0], a) in self.parserTable.keys():
                    print("Conflict! M(" + prod[0][0] + "," + a + ")")
                if a != 'epsilon':
                    self.parserTable[(prod[0][0], a)] = (prod[1], index)
            if 'epsilon' in self.get_first_concat(prod[1]):
                for b in self.get_follow(prod[0][0]):
                    if isinstance(b, list):
                        b = tuple(b)
                    if (prod[0][0], b) in self.parserTable.keys():
                        print("Conflict! M(" + prod[0][0] + "," + a + ")")
                    self.parserTable[(prod[0][0], b)] = (prod[1], index)

    def analyze_sequence(self, sequence):
        input_stack = []
        working_stack = []
        output = []

        input_stack.append("$")
        sequence = sequence.split(" ")
        for elem in reversed(sequence):
            input_stack.append(elem)

        working_stack.append("$")
        working_stack.append(self.grammar.S)

        while input_stack[len(input_stack) - 1] != "$" or working_stack[len(working_stack) - 1] != "$":
            input_top = input_stack[len(input_stack) - 1]
            working_top = working_stack[len(working_stack) - 1]
            if (working_top, input_top) in self.parserTable.keys():
                value = self.parserTable[(working_top, input_top)]
                if isinstance(value, tuple) is False and value == "pop":
                    input_stack.pop()
                    working_stack.pop()
                    continue
                else:
                    working_stack.pop()
                    if value[0] != ['epsilon']:
                        production = value[0]
                        for prod in reversed(production):
                            working_stack.append(prod)
                output.append(self.parserTable[(working_top, input_top)])
            else:
                print("Error for " + input_top + " , " + working_top)
                return output
        return output

    def get_first_concat(self, list):
        res = set()
        index = 0
        stop = True
        while stop:
            element = list[index]
            if element in self.grammar.E:
                res.add(element)
                break
            firstList = self.first[element]
            for elem in firstList:
                res.add(elem)
            if 'epsilon' not in firstList:
                stop = False
            index += 1
        return res

    def print_first(self):
        for key in self.first.keys():
            print(key, ' : ', self.first[key])

    def print_follow(self):
        for key in self.follow.keys():
            print(key, ' : ', self.follow[key])

    def print_parser_table(self):
        for key in self.parserTable.keys():
            # print(key, key[0], key[1])
            if self.parserTable[key] == 'pop' or self.parserTable[key] == 'acc':
                print("M( " + key[0] + " , " + key[1] + " ) = " + self.parserTable[key])
            else:
                print("M( " + key[0] + " , " + key[1] + " ) = " + ' '.join(self.parserTable[key][0]) + "," + str(
                    self.parserTable[key][1]))

