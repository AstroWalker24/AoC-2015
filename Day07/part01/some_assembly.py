import sys

# Increase recursion limit to handle large circuits
sys.setrecursionlimit(10**6)

# Memoization dictionary to store computed values for wires
memo = {}

def findValue(wire, gates):
    # Check if the value is already computed
    if wire in memo:
        return memo[wire]
    
    # If wire is a number, return its integer value
    if wire.isdigit():
        return int(wire)
    
    # Find the gate that produces the signal for this wire
    for gate in gates:
        if gate[2] == wire:
            op_type = gate[3]

            # Gate type: ASSIGN
            if op_type == 'ASSIGN':
                value = findValue(gate[0], gates)

            # Gate type: NOT
            elif op_type == 'NOT':
                value = ~findValue(gate[0], gates) & 0xFFFF  # Mask to 16 bits

            # Gate type: AND
            elif op_type == 'AND':
                value = findValue(gate[0], gates) & findValue(gate[1], gates)

            # Gate type: OR
            elif op_type == 'OR':
                value = findValue(gate[0], gates) | findValue(gate[1], gates)

            # Gate type: LSHIFT
            elif op_type == 'LSHIFT':
                value = findValue(gate[0], gates) << int(gate[1])

            # Gate type: RSHIFT
            elif op_type == 'RSHIFT':
                value = findValue(gate[0], gates) >> int(gate[1])

            # Store the result in memo and return
            memo[wire] = value & 0xFFFF  # Mask to 16 bits
            return memo[wire]
    
    # If no gate produces this wire, raise an error
    raise ValueError(f"Wire {wire} not found in any gate")

def parseInput(content):
    content = content.strip().split('\n')
    gates = []

    for line in content:
        words = line.split()
        if 'AND' in line or 'OR' in line or 'LSHIFT' in line or 'RSHIFT' in line:
            gates.append((words[0], words[2], words[4], words[1]))
        elif 'NOT' in line:
            gates.append((words[1], None, words[3], 'NOT'))
        elif '->' in line:
            gates.append((words[0], None, words[2], 'ASSIGN'))
    
    return gates

def main():
    with open('inp.txt') as f:
        content = f.read()
    gates = parseInput(content)
    # Compute the value of wire 'a'
    result = findValue('a', gates)
    print(f"Signal to wire 'a': {result}")

if __name__ == "__main__":
    main()
