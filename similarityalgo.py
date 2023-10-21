def main_menu():
    print("1. Set Maximum Shift")
    print("2. Calculate using File Inputs")
    print("3. Exit")

def get_user_input(prompt):
    return input(prompt)

def load_sequence_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def calculate_matches(sequence1, sequence2, shift):
    # Shift sequence2
    sequence2_shifted = sequence2[shift:] + " " * shift
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
    best_matches = 0
    best_chain = 0

    for shift in range(0, max_shift + 1):
        current_matches = calculate_matches(sequence1, sequence2, shift)
        current_chain = calculate_max_contiguous_chain(sequence1, sequence2, shift)
        
        if current_matches > best_matches or (current_matches == best_matches and current_chain > best_chain):
            best_shift = shift
            best_matches = current_matches
            best_chain = current_chain

    return best_shift, best_matches, best_chain

def calculate_from_file_input(max_shift):
    filename1 = get_user_input("Enter filename for Sequence 1: ")
    filename2 = get_user_input("Enter filename for Sequence 2: ")
    try:
        sequence1 = load_sequence_from_file(filename1)
        sequence2 = load_sequence_from_file(filename2)
        shift, matches, chain = calculate_best_shift(sequence1, sequence2, max_shift)
        print(f"Best shift: {shift}, Matches: {matches}, Maximum Contiguous Chain: {chain}")
    except FileNotFoundError:
        print("File not found!")
    except ValueError:
        print("File format is incorrect!")
        

def calculate_from_console_input(max_shift):
    sequence1 = get_user_input("Enter Sequence 1: ")
    sequence2 = get_user_input("Enter Sequence 2: ")
    shift, matches, chain = calculate_best_shift(sequence1, sequence2, max_shift)
    print(f"Best shift: {shift}, Matches: {matches}, Maximum Contiguous Chain: {chain}")

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