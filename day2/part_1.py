def check_valid_line(line):
    if (line[0] > line[1]):
        for current, next in zip(line, line[1:]):
            if (current > next and abs(current - next) <= 3):
                continue
            else:
                return False
    elif (line[0] < line[1]):
        for current, next in zip(line, line[1:]):
            if (current < next and abs(current - next) <= 3):
                continue
            else:
                return False
    else:
        return False
    return True

def main():
    lines = open("input.txt", 'r').readlines()
    valid_lines = 0
    for line in lines:
        line = list(map(int, line.strip().split()))
        if (check_valid_line(line)):
            valid_lines += 1
    print(valid_lines)
    
if __name__ == "__main__":
    main()