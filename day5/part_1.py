def main():
    lines = open("main_test.txt", 'r').readlines()
    
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
            continue;
        else:
            updates.append(line.strip().split())
        
    for update in updates:
        print(f"update: {update}")

if __name__ == "__main__":
    main()