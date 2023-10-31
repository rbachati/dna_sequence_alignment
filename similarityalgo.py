def get_user_input(prompt):
    return input(prompt)

def validate_sequence(sequence):
    # Check if only characters A,C,G,T are in the sequence
    if any(base.islower() for base in sequence):
        raise ValueError("Invalid character casing. DNA should be represented in capital letters A, C, G, T.")
    
    if not all(base in 'ACGT' for base in sequence):
        raise ValueError("Invalid sequence. Only characters A, C, G, T are allowed.")

def load_sequence_from_file(filename):
    with open(filename, 'r') as file:
        # Read the file, remove any line breaks, and then strip whitespace
        return file.read().replace('\n', '').strip()

def identify_chained_sequences(sequence1, sequence2):
    chained_sequences = []
    chain = ""
    for a, b in zip(sequence1, sequence2):
        if a == b:
            chain += a
        else:
            if chain:
                chained_sequences.append(chain)
                chain = ""
    if chain: # if the chain extends to the end
        chained_sequences.append(chain)
    return chained_sequences

def calculate_matches(sequence1, sequence2, shift):
    # Shift sequence2
    sequence2_shifted = sequence2[-shift:] + sequence2[:-shift]
    matches = sum(1 for a, b in zip(sequence1, sequence2_shifted) if a == b)
    return matches

def calculate_max_contiguous_chain(sequence1, sequence2, shift):
    sequence2_shifted = sequence2[shift:] + " " * shift
    max_chain = 0
    current_chain = 0
    for a, b in zip(sequence1, sequence2_shifted):
        if a == b:
            current_chain += 1
            max_chain = max(max_chain, current_chain)
        else:
            current_chain = 0
    return max_chain

def calculate_best_shift(sequence1, sequence2, max_shift):
    best_shift = 0
    best_matches = count_matches_without_shift(sequence1, sequence2)  # Start with no shift matches
    best_chain = max(identify_chained_sequences(sequence1, sequence2), key=len, default="")
    best_chained_sequences = identify_chained_sequences(sequence1, sequence2)

    for shift in range(1, max_shift + 1):  # Start from 1 since we already considered shift = 0
        sequence2_shifted = sequence2[-shift:] + sequence2[:-shift]
        
        current_matches = sum(1 for a, b in zip(sequence1, sequence2_shifted) if a == b)
        current_chained_sequences = identify_chained_sequences(sequence1, sequence2_shifted)
        current_chain = max(current_chained_sequences, key=len, default="")
        
        if current_matches > best_matches or (current_matches == best_matches and len(current_chain) > len(best_chain)):
            best_shift = shift
            best_matches = current_matches
            best_chain = current_chain
            best_chained_sequences = current_chained_sequences

    return best_shift, best_matches, best_chain, best_chained_sequences

def calculate_from_file_input(max_shift):
    filename1 = get_user_input("Enter filename for Sequence 1: ")
    filename2 = get_user_input("Enter filename for Sequence 2: ")
    try:
        sequence1 = load_sequence_from_file(filename1)
        sequence2 = load_sequence_from_file(filename2)
        validate_sequence(sequence1)
        validate_sequence(sequence2)

        # Matches without any shifts
        matches = count_matches_without_shift(sequence1, sequence2)
        print(f"Matches without any shifts: {matches}")

        # Chained sequences without any shifts
        chained_sequences = identify_chained_sequences(sequence1, sequence2)
        print("Chained sequences without shift:", ', '.join(chained_sequences) if chained_sequences else "None")
        
        # Maximum contiguous chain without any shifts
        max_chain_without_shift = max(chained_sequences, key=len, default="")
        print(f"Maximum contiguous chain without shift: {max_chain_without_shift}")

        # Best chain after performing shifts
        shift, matches, chain, chained_sequences_after_shift = calculate_best_shift(sequence1, sequence2, max_shift)
        print(f"\nAfter applying the best shift of {shift}:")
        print(f"Matches: {matches}")
        print("Chained sequences:", ', '.join(chained_sequences_after_shift) if chained_sequences_after_shift else "None")
        print(f"Maximum Contiguous Chain: {chain}")  # Print the chain

    except FileNotFoundError:
        print(f"Error: {filename1} or {filename2} was not found!")
    except UnicodeDecodeError as ude:
        print(f"Error: Unable to decode file content! Ensure the file is a UTF-8 encoded text file. Error details: {ude}")
    except ValueError as e:
        print(f"Error: {e}") 

def count_matches_without_shift(sequence1, sequence2):
    return sum(1 for a, b in zip(sequence1, sequence2) if a == b)
   
def calculate_from_console_input(max_shift):
    sequence1 = get_user_input("Enter Sequence 1: ")
    sequence2 = get_user_input("Enter Sequence 2: ")
    try:
        
        validate_sequence(sequence1)
        validate_sequence(sequence2)

        # Matches without any shifts
        matches = count_matches_without_shift(sequence1, sequence2)
        print(f"Matches without any shifts: {matches}")

        # Chained sequences without any shifts
        chained_sequences = identify_chained_sequences(sequence1, sequence2)
        print("Chained sequences without shift:", ', '.join(chained_sequences) if chained_sequences else "None")

        # Best chain after performing shifts
        shift, matches, chain, chained_sequences_after_shift = calculate_best_shift(sequence1, sequence2, max_shift)
        print(f"\nAfter applying the best shift of {shift}:")
        print(f"Matches: {matches}")
        print("Chained sequences:", ', '.join(chained_sequences_after_shift) if chained_sequences_after_shift else "None")
        print(f"Maximum Contiguous Chain: {chain}")
    except ValueError as e:
        print(f"Error: {e}")

def main_menu():
    print("1. Set Maximum Shift")
    print("2. Calculate using Console Inputs")
    print("3. Calculate using File Inputs")
    print("4. Exit")

def main():
    max_shift = None
    while True:
        main_menu()
        choice = get_user_input("Select option: ")
        if choice == '1':
            try:
                max_shift = int(get_user_input("Set Maximum Shift: "))
                print(f"Maximum Shift set to {max_shift}")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == '2':
            if max_shift is None:
                print("Please set the Maximum Shift first!")
            else:
                calculate_from_console_input(max_shift)
        elif choice == '3':
            if max_shift is None:
                print("Please set the Maximum Shift first!")
            else:
                calculate_from_file_input(max_shift)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
