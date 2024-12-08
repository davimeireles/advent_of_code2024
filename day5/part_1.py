def main():
    lines = open("input.txt", 'r').readlines()
    
    rules_map = {}
    
    for line in lines:
        if (line == "\n"):
            break
        key, value = line.split("|")
        key = key.strip()
        value = value.strip()
        if key not in rules_map:
            rules_map[key] = []
        rules_map[key].append(value)
    
    updates = []
    
    for line in lines:
        if (line.find(",") == -1):
            continue
        else:
            updates.append(list(map(int, line.strip().split(","))))

    middle_numbers = []

    for update in updates:
        is_valid = True
        for i, num in enumerate(update):
            if str(num) in rules_map:
                for j in range(i):
                    if str(update[j]) in rules_map[str(num)]:
                        is_valid = False
                        break
            if not is_valid:
                break
        if is_valid:
            middle_index = len(update) // 2
            middle_number = update[middle_index]
            middle_numbers.append(middle_number)
            print(f"Valid line: {update}, Middle number: {middle_number}")
        else:
            print(f"Invalid line: {update}")

    total_sum = sum(middle_numbers)
    print(f"All middle numbers: {middle_numbers}")
    print(f"Total sum of all middle numbers: {total_sum}")

if __name__ == "__main__":
    main()