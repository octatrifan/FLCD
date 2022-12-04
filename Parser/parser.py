from Grammar.grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar('../Grammar/first_grammar.in')
        self.first = {}
        self.follow = {}
        self.get_all_first()
        self.get_all_follow()

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
                            for e in self.get_first(rule):
                                aux.add(e)
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

    def print_first(self):
        for key in self.first.keys():
            print(key, ' : ', self.first[key])

    def print_follow(self):
        for key in self.follow.keys():
            print(key, ' : ', self.follow[key])
