def read_file_to_list(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def search_xmas(grid):
    directions = [
        (1, 1),  # down-right
        (1, -1), # down-left
        (-1, 1), # up-right
        (-1, -1) # up-left
    ]
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'A':
                valid = True
                for diagonal_row, diagonal_col in directions:
                    num_row, num_col = row + diagonal_row, col + diagonal_col
                    opposite_diagonal_row, opposite_diagonal_col = -diagonal_row, -diagonal_col
                    opposite_num_row, opposite_num_col = row + opposite_diagonal_row, col + opposite_diagonal_col
                    if not (0 <= num_row < rows and 0 <= num_col < cols and 0 <= opposite_num_row < rows and 0 <= opposite_num_col < cols):
                        valid = False
                        break
                    if not ((grid[num_row][num_col] == 'M' and grid[opposite_num_row][opposite_num_col] == 'S') or 
                            (grid[num_row][num_col] == 'S' and grid[opposite_num_row][opposite_num_col] == 'M')):
                        valid = False
                        break
                if valid:
                    count += 1
    return count
				

def main():
    filename = "input.txt"
    grid = read_file_to_list(filename)
    total_xmas = search_xmas(grid)
    print(f"Total 'X-MAS' found: {total_xmas}")

if __name__ == "__main__":
    main()