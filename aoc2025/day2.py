def main():
    with open("aoc2025/day2.txt") as f:
        data = parse_input(f.read())
    print(f"part1: {part1(data)}")
    # print(f"part2: {part2(data)}")

def part1(data: list[tuple[int, int]]) -> int:
    invalid_ids = []
    for rng in data:
        low_centre_point = len(str(rng[0])) // 2
        if len(str(rng[0])) % 2 == 0:
            low = int(str(rng[0])[:low_centre_point])
            if int(str(low) + str(low)) < rng[0]:
                low += 1
        else:
            low = int("1" + "0" * low_centre_point)
        assert int(str(low) + str(low)) >= rng[0]

        high_centre_point = len(str(rng[1])) // 2
        if len(str(rng[1])) % 2 == 0:
            high = int(str(rng[1])[:high_centre_point])
            if int(str(high) + str(high)) > rng[1]:
                high -= 1
            assert int(str(high) + str(high)) <= rng[1]
        else:
            high = int("9" * high_centre_point)

        # print(f"{low}, {high}")

        for id_half in range(low, high + 1):
            invalid_id = int(str(id_half) * 2)
            # print(invalid_id)
            invalid_ids.append(invalid_id)

    return sum(invalid_ids)


def parse_input(input_str: str) -> list[tuple[int, int]]:
    return [(int(rng.split("-")[0]), int(rng.split("-")[1])) for rng in input_str.strip().split(",")]

if __name__ == "__main__":
    main()
