def read_file_to_list(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def search_xmas(grid):
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0), 
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
    word = "XMAS"
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                for dr, dc in directions:
                    found = True
                    for k in range(1, len(word)):
                        nr, nc = r + dr * k, c + dc * k
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == word[k]:
                            continue
                        else:
                            found = False
                            break
                    if found:
                        count += 1
    return count

def main():
    filename = "input.txt"
    grid = read_file_to_list(filename)
    total_xmas = search_xmas(grid)
    print(f"Total 'XMAS' found: {total_xmas}")

if __name__ == "__main__":
    main()