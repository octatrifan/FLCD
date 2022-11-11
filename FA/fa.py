class FA:
    def __init__(self, filename):
        self.filename = filename
        self.Q = []
        self.E = []
        self.F = []
        self.q0 = []
        self.S = []
        self.read_file()

    def read_file(self):
        reserved_tokens_file = open(self.filename, 'r')
        lines = reserved_tokens_file.readlines()
        index = 0
        for line in lines:
            if index == 0:
                self.Q = self.read_line(line)
            if index == 1:
                self.E = self.read_line(line)
            if index == 2:
                line = line.replace(" ", "")
                stripped = line.strip()
                self.q0 = stripped.split("=")[-1]

            if index == 3:
                self.F = self.read_line(line)
            index += 1

        index = 5
        while index < len(lines):
            line = lines[index].strip()
            line = line.replace(" ", "")
            S_line = line.split("->")

            first = S_line[0]
            tokens_list1 = first[1:-1]
            tokens = tokens_list1.split(",")

            second = S_line[1]
            tokens_list2 = second[1:-1]
            res = tokens_list2.split(",")

            self.S.append((tokens[0], tokens[1], res))
            index += 1

    def print_fa(self):
        print("Q = ", self.Q)
        print("E = ", self.E)
        print("q0 = ", self.q0)
        print("F = ", self.F)
        print("S = ", self.S)

    def print_menu(self):
        print("\n1. Display set of states")
        print("2. Display alphabet")
        print("3. Display transitions")
        print("4. Display initial state")
        print("5. Display set of final states")
        print("6. Display all")
        print("7. DFA membership for sequece\n")

    def print_set_of_states(self):
        print("Q = ", self.Q)

    def print_alphabet(self):
        print("E = ", self.E)

    def print_initial_state(self):
        print("q0 = ", self.q0)

    def print_final_states(self):
        print("F = ", self.F)

    def print_transitions(self):
        print("S = ", self.S)

    def read_line(self, line):
        split = line.split()
        set = split[-1]
        tokens_list = set[1:-1]
        tokens = tokens_list.split(",")
        return tokens

    def check_sequence_DFA(self, sequence):
        p = self.q0
        for element in sequence:
            state = self.get_next_state(p, element)
            if state is None:
                return False
            if len(state) != 1:
                print("Not DFA!")
                return False
            p = state[0]
        if p in self.F:
            return True
        return False

    def menu_check_sequence_DFA(self):
        sequence = input("Introduce sequence: ")
        print(self.check_sequence_DFA("1string1"))

    def get_next_state(self, initial, transition):
        for elem in self.S:
            if elem[0] == initial:
                if elem[1] == transition or (elem[1] == 'letter' and transition.isalpha()) or (
                        elem[1] == 'digit' and transition.isdigit()) or (
                        elem[1] == 'nzdigit' and transition.isdigit() and transition != '0') or (
                        elem[1] == 'space' and transition == " "
                ):
                    return elem[2]
        return None

    def run_menu(self):
        self.read_file()
        while True:
            self.print_menu()
            choice = int(input("Your choice: "))
            print()
            match choice:
                case 1:
                    self.print_set_of_states()
                case 2:
                    self.print_alphabet()
                case 3:
                    self.print_transitions()
                case 4:
                    self.print_initial_state()
                case 5:
                    self.print_final_states()
                case 6:
                    self.print_fa()
                case 7:
                    self.menu_check_sequence_DFA()
                case _:
                    return
