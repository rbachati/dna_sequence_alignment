DNA Sequence Alignment Program
This program calculates the optimal alignment between two DNA sequences using different methods to measure similarity.

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

Follow the on-screen instructions:
Set the maximum shift value.
Input DNA sequences directly or provide filenames to load sequences.
File Structure:
similarity_algo.py: The main Python script containing the program.
Algorithms:
The program determines the optimal alignment based on:

Number of Matches: It calculates the number of matching nucleotides between two sequences at each shift value.

Maximum Contiguous Chain: The program also calculates the longest contiguous sequence of matching nucleotides.

Exception Handling:
The program handles file errors and input format errors. If the specified file doesn't exist, it notifies the user.

If the inputted value for maximum shift isn't a valid integer, it prompts the user to re-enter.

Contributions:
Feel free to contribute! Fork the repository, make your changes, and submit a pull request.







