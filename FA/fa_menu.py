class Menu:
    def __init__(self):
        self.Q = []
        self.E = []
        self.F = []
        self.q0 = []
        self.S = []

    def read_file(self):
        reserved_tokens_file = open("fa.in", 'r')
        lines = reserved_tokens_file.readlines() 
        index=0
        for line in lines:
            if index == 0:
                self.Q = self.read_line(line)
            if index == 1:
                self.E = self.read_line(line)
            if index == 2:
                stripped = line.strip()
                self.q0 = stripped.split("=")[-1]
                
            if index == 3:
                self.F = self.read_line(line)    
            index+=1    

        index = 5
        while index<len(lines):
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
            index+=1


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
        print("6. Display all\n")  
        


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
                case _:
                    return