# Sudoku Wiz

This Python script is designed to solve Sudoku puzzles using a graphical user interface (GUI) interaction. It uses a recursive backtracking algorithm to find a solution for the given Sudoku puzzle and then simulates keyboard presses to display the solved puzzle.

## Usage

1. Run the script `sudokuWiz.py`.

2. You will be prompted to enter the Sudoku grid. Input each row as space-separated integers. Use `0` to represent empty cells.

3. Once the Sudoku puzzle is entered, open your preferred Sudoku app or interface.

4. Click on the first cell of the Sudoku grid to focus on it. This is where the printing will start.

5. After 5 seconds, the script will simulate keyboard presses to print the solved puzzle using the PyAutoGUI library.

## Dependencies

- Python 3.x
- PyAutoGUI library

## Notes

- The script may require adjustments to timing (using `time.sleep()`) for reliable interaction on different systems.
- The PyAutoGUI-based printing is a basic demonstration and might not work seamlessly on all systems or configurations.
