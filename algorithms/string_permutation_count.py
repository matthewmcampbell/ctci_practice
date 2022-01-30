# Function to recursively count number of permutations in
# a string.


def permutation(s: str, prefix: str, results):
    if len(s) == 0:
        results.append(prefix)
    else:
        for i in range(len(s)):
            remainder = s[0: i] + s[i + 1:]
            permutation(remainder, prefix + s[i], results)


def permutations(in_str: str):
    results = []
    permutation(in_str, "", results)
    return len(results)


if __name__ == "__main__":
    test_cases = ["jimmy", "dean", "carlos"]
    for test in test_cases:
        print(permutations(test))
