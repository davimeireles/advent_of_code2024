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

def try_to_fix_line(line):
    def check_and_fix(line, index):
        temp_line = line[:index] + line[index+1:]
        return check_valid_line(temp_line)

    for i in range(len(line)):
        if i > 0:
            prev = line[i-1]
        else:
            prev = None

        current = line[i]

        if i < len(line) - 1:
            next = line[i+1]
        else:
            next = None

        if prev is not None and current is not None and next is not None:
            if (prev < current < next or prev > current > next):
                continue
            else:
                if check_and_fix(line, i-1):
                    return True
                if check_and_fix(line, i):
                    return True
                if check_and_fix(line, i+1):
                    return True
                return False
        elif prev is None:
            if check_and_fix(line, i):
                return True
        elif next is None:
            if check_and_fix(line, i):
                return True
    return False

def main():
    lines = open("input.txt", 'r').readlines()
    valid_lines = 0
    
    for line in lines:
        line = list(map(int, line.strip().split()))
        if (check_valid_line(line)):
            valid_lines += 1
        else:
            if (try_to_fix_line(line)):
                valid_lines += 1
    print(valid_lines)
    
if __name__ == "__main__":
    main()