import re

def find_and_multiply_mul_patterns(line):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line)
    results = []

    for match in matches:
        num1, num2 = map(int, match)
        result = num1 * num2
        results.append(result)

    return results

def main():
    lines = open("input.txt", 'r').readlines()
    total_sum = 0
    
    for line in lines:
        line = line.strip()
        results = find_and_multiply_mul_patterns(line)
        total_sum += sum(results)
        
    print(f"Total Sum: {total_sum}")

if __name__ == "__main__":
    main()