class Grammar:
    def __init__(self, filename):
        self.filename = filename
        self.N = set()
        self.E = set()
        self.P = []
        self.read_file()
        if self.validate() is False:
            print("Invalid File!")

    def read_file(self):
        file = open(self.filename, 'r')
        lines = file.readlines()
        index = 0
        for line in lines:
            if index == 0:
                self.N = self.read_line(line)
            if index == 1:
                self.E = self.read_line(line)
            if index == 2:
                line = line.replace(" ", "")
                stripped = line.strip()
                self.S = stripped.split("=")[-1]
            index += 1

        index = 4
        while index < len(lines):
            line = lines[index].strip()
            # line = line.replace(" ", "")
            S_line = line.split("->")

            first = S_line[0]
            first = first.strip()
            first = first.split(" ")

            prod_list = S_line[1]
            prods = prod_list.split("|")
            prod_res = []
            for prod in prods:
                prod = prod.strip()
                list = prod.split(" ")
                prod_res.append(list)
            self.P.append((first, prod_res))
            index += 1

    def read_line(self, line):
        split = line.split()
        set = split[-1]
        tokens_list = set[1:-1]
        tokens = tokens_list.split(",")
        return tokens

    def print_menu(self):
        print("\n1. Display set of nonterminals")
        print("2. Display set of terminals")
        print("3. Display set of productions")
        print("4. Display productions for a given non-terminal")
        print("5. CFG check")

    def print_nonterminals(self):
        print("N = ", self.N)

    def print_terminals(self):
        print("E = ", self.E)

    def print_productions(self):
        print("P = ", self.P)

    def get_productions_for_non_terminal(self, nonterm):
        if nonterm not in self.N:
            print("Non terminal " + nonterm + " does not exist in the list of non terminals")
        for elem in self.P:
            if ' '.join(elem[0]) == nonterm:
                return elem[1]
        return []

    def get_productions_containing_non_terminal(self, nonterm):
        res = []
        for prod in self.P:
            for elem in prod[1]:
                if nonterm in elem:
                    res.append((prod[0], elem))
        return res

    def print_productions_for_non_terminal(self):
        nonterm = input("Input the non-terminal: ")
        if nonterm not in self.N:
            print("Non terminal does not exist in the list of non terminals")
        for elem in self.P:
            if ' '.join(elem[0]) == nonterm:
                print("Productions: ", elem[1])
                return
        print("No productions!")

    def cfg_check(self):
        for elem in self.P:
            if len(elem[0])>1:
                print("Not a single non-terminal!")
                return False
        return True

    def validate(self):
        if len(set(e for e in self.P if self.P.count(e) > 1)):
            print("Duplicates!")
            return False

        if self.S not in self.N:
            print("Starting Symbol should be part of the non-terminals")
            return False

        found_match = False
        for t in self.P:
            if ' '.join(t[0]) == self.S:
                found_match = True

        if not found_match:
            print("Nothing starts from starting symbol")
            return False

        for elem in self.P:
            (symbol, prod_list) = elem
            for prod in prod_list:
                for char in prod:
                    if char not in self.N and char not in self.E:
                        print(char + " is not in the set of non-terminals or terminals")
                        return False
            for prod in symbol:
                if prod not in self.N and prod not in self.E:
                    print(prod + " is not in the set of non-terminals or terminals")
                    return False

    def run_menu(self):
        # self.read_file()
        while True:
            self.print_menu()
            choice = int(input("Your choice: "))
            print()
            match choice:
                case 1:
                    self.print_nonterminals()
                case 2:
                    self.print_terminals()
                case 3:
                    self.print_productions()
                case 4:
                    self.print_productions_for_non_terminal()
                case 5:
                    print(self.cfg_check())
                case _:
                    return

