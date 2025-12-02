def main():
    with open("aoc2025/day1.txt") as f:
        data = f.read().strip().splitlines()
        print(f"part1: {part1(data)}")
        print(f"part1: {part2(data)}")

def part1(data: list[str]) -> int:
    zeros = 0
    current = 50
    for thing in data:
        if thing[0] == "R":
            current = (current + int(thing[1:])) % 100
        elif thing[0] == "L":
            current = (current - int(thing[1:])) % 100
            if current < 0:
                current += 100
        else:
            raise ValueError(f"Unknown direction: {thing[0]}")
        
        if current == 0:
            zeros += 1
    
    return zeros

def part2(data: list[str]) -> int:
    zeros = 0
    current = 50

    for thing in data:
        if thing[0] == "R":
            for _ in range(int(thing[1:])):
                current += 1
                if current >= 100:
                    current -= 100
                if current == 0:
                    zeros += 1
        elif thing[0] == "L":
            for _ in range(int(thing[1:])):
                current -= 1
                if current < 0:
                    current += 100
                if current == 0:
                    zeros += 1
        else:
            raise ValueError(f"Unknown direction: {thing[0]}")
    
    return zeros

if __name__ == "__main__":
    main()
