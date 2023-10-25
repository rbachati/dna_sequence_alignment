DNA Sequence Alignment Program
This program calculates the optimal alignment between two DNA sequences using different methods to measure similarity.

Approach to the DNA Sequence Alignment Problem
1. Input Collection:
Console Input: The program provides an interface for users to manually input two DNA sequences.

File Input: Users can also specify filenames, and the program will fetch the sequences from these files.

2. Setting the Maximum Shift:
Before the alignment calculations can begin, the user needs to specify a maximum shift value. This determines the maximum number of positions by which one sequence can be shifted relative to the other.

3. Initialization:
Start by assuming the best alignment is when both sequences are not shifted (i.e., shift value is zero). Record the number of matching nucleotides in this position as well as the longest contiguous matching chain.

4. Shifting and Comparing:
For each possible shift value up to the maximum:

Shift one of the sequences by the current shift value.
Compare the nucleotides of the two sequences.
Count the number of matches for this shift.
Also, identify the longest contiguous matching sequence (chain) for this shift.

5. Identifying Optimal Alignment:
After considering all possible shifts:

Find the shift that maximized the number of matching nucleotides.

In case of a tie (where two shifts have the same number of matches), prefer the shift with the longest contiguous matching chain.

6. Display Results:
Present to the user:

The shift value that resulted in the best alignment.

The number of matches for this alignment.

The sequence and length of the longest contiguous chain for this alignment.

7. Error Handling:
File Errors: Check if the provided filenames exist. If not, inform the user.

Input Validation: Ensure that sequences are valid DNA sequences (consisting of A, T, C, G). Also, ensure the maximum shift value is a valid integer.

8. Repeat or Exit:
Provide the user with an option to analyze another pair of sequences or exit the program.


Features:
Set Maximum Shift: Users can set a user-defined maximum shift, indicating how many positions they would like the sequences to be shifted for optimal alignment. The program will not run the calculations unless this value is set.

Console Inputs: Users can directly input DNA sequences through the terminal.

File Inputs: Alternatively, users can also provide two separate filenames for the sequences to be loaded and analyzed.

Usage:
Clone the repository:
git clone <repository_url>
cd <repository_directory>

Run the program:
python similarity_algo.py


Contributions:
Feel free to contribute! Fork the repository, make your changes, and submit a pull request.
