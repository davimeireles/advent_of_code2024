import re

def find_and_multiply_mul_patterns(line):

    total = 0
    segments = re.split(r"(do\(\)|don't\(\))", line)
    process = True

    for segment in segments:
        if segment == "do()":
            process = True
        elif segment == "don't()":
            process = False
        else:
            if process:
                pattern = r"mul\((\d+),(\d+)\)"
                matches = re.findall(pattern, segment)

                for match in matches:
                    num1, num2 = map(int, match)
                    result = num1 * num2
                    total += result
   
    return total

def main():
    lines = open("input.txt", 'r').readlines()
    final_value = 0
    
    line = "".join(lines)
    
    final_value = find_and_multiply_mul_patterns(line)
    print(f"Final value: {final_value}")

if __name__ == "__main__":
    main()