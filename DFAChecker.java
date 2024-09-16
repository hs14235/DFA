package DFAChecker;

import java.util.*;
import java.io.*;

public class DFAChecker {
    private Set<Character> alphabet;
    private Set<Character> states;
    private char startState;
    private Set<Character> acceptStates;
    private Map<String, Character> transitions;

    public DFAChecker() {
        alphabet = new HashSet<>();
        states = new HashSet<>();
        acceptStates = new HashSet<>();
        transitions = new HashMap<>();
    }

    public void loadDFA(String filename) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String line;
        int lineNum = 0;
        while ((line = reader.readLine()) != null) {
            lineNum++;
            switch (lineNum) {
                case 1: parseSet(line, alphabet); break;
                case 2: parseSet(line, states); break;
                case 3: startState = parseState(line); break;
                case 4: parseSet(line, acceptStates); break;
                default: parseTransition(line);
            }
        }
        reader.close();
    }

    private void parseSet(String line, Set<Character> set) {
        line = line.replaceAll("[{}\\s]", "");
        for (char c : line.toCharArray()) {
            set.add(c);
        }
    }

    private char parseState(String line) {
        return line.charAt(0);
    }

    private void parseTransition(String line) {
        String[] parts = line.split("->");
        String[] transition = parts[0].substring(1, parts[0].length() - 1).split(",");
        char fromState = transition[0].charAt(0);
        char symbol = transition[1].charAt(0);
        char toState = parts[1].charAt(0);
        transitions.put(fromState + "," + symbol, toState);
    }

    public boolean run(String input) {
        char currentState = startState;
        for (char symbol : input.toCharArray()) {
            if (!alphabet.contains(symbol)) {
                System.out.println("Invalid input symbol: " + symbol);
                return false;
            }
            String key = currentState + "," + symbol;
            if (!transitions.containsKey(key)) {
                System.out.println("No transition for " + key);
                return false;
            }
            currentState = transitions.get(key);
        }
        return acceptStates.contains(currentState);
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        String filename;

        if (args.length > 0) {
            filename = args[0];
        } else {
            System.out.print("Enter the filename: ");
            filename = scanner.nextLine();
        }

        DFAChecker dfa = new DFAChecker();
        dfa.loadDFA(filename);

        while (true) {
            System.out.print("Enter a string to test (or 'exit' to quit): ");
            String input = scanner.nextLine();
            if (input.equals("exit")) {
                break;
            }
            boolean accepted = dfa.run(input);
            System.out.println("String is " + (accepted ? "accepted" : "rejected") + " by the DFA.");
        }

        scanner.close();
    }
}