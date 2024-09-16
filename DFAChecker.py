import re

class DFA:
    def __init__(self):
        self.alphabet = set()
        self.states = set()
        self.start_state = None
        self.accept_states = set()
        self.transitions = {}

    def load_dfa(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.parse_set(lines[0], self.alphabet)
            self.parse_set(lines[1], self.states)
            self.start_state = self.parse_state(lines[2])
            self.parse_set(lines[3], self.accept_states)
            for line in lines[4:]:
                self.parse_transition(line.strip())

    def parse_set(self, line, set_):
        line = re.sub(r'[{}\s]', '', line)
        for char in line:
            set_.add(char)

    def parse_state(self, line):
        return line.strip()[0]

    def parse_transition(self, line):
        parts = line.split('->')
        from_state, symbol = parts[0][1:-1].split(',')
        to_state = parts[1].strip()
        self.transitions[(from_state, symbol)] = to_state

    def run(self, input_str):
        current_state = self.start_state
        for symbol in input_str:
            if symbol not in self.alphabet:
                print(f"Invalid input symbol: {symbol}")
                return False
            if (current_state, symbol) not in self.transitions:
                print(f"No transition for ({current_state}, {symbol})")
                return False
            current_state = self.transitions[(current_state, symbol)]
import re

class DFA:
    def __init__(self):
        self.alphabet = set()
        self.states = set()
        self.start_state = None
        self.accept_states = set()
        self.transitions = {}

    def load_dfa(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.parse_set(lines[0], self.alphabet)
            self.parse_set(lines[1], self.states)
            self.start_state = self.parse_state(lines[2])
            self.parse_set(lines[3], self.accept_states)
            for line in lines[4:]:
                self.parse_transition(line.strip())

    def parse_set(self, line, set_):
        line = re.sub(r'[{}\s]', '', line)
        for char in line:
            set_.add(char)

    def parse_state(self, line):
        return line.strip()[0]

    def parse_transition(self, line):
        parts = line.split('->')
        from_state, symbol = parts[0][1:-1].split(',')
        to_state = parts[1].strip()
        self.transitions[(from_state, symbol)] = to_state

    def run(self, input_str):
        current_state = self.start_state
        for symbol in input_str:
            if symbol not in self.alphabet:
                print(f"Invalid input symbol: {symbol}")
                return False
            if (current_state, symbol) not in self.transitions:
                print(f"No transition for ({current_state}, {symbol})")
                return False
            current_state = self.transitions[(current_state, symbol)]
        return current_state in self.accept_states

def main():
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else input("Enter the filename: ")
    dfa = DFA()
    dfa.load_dfa(filename)

    while True:
        input_str = input("Enter a string to test (or 'exit' to quit): ")
        if input_str == 'exit':
            break
        accepted = dfa.run(input_str)
        print(f"String is {'accepted' if accepted else 'rejected'} by the DFA.")

if __name__ == "__main__":
    main()
