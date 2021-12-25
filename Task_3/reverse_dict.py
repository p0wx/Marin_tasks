from collections import defaultdict

def reverce_dict(original_dict):
    reversed_dict = defaultdict(list)
    for key, list_values in original_dict.items():
        for value in list_values:
            reversed_dict[value].append(key)
    return dict(reversed_dict)


def main():
    original_dict = {
        "move": ["liikuttaa"],
        "hide": ["piilottaa", "salata"],
        "six": ["kuusi"],
        "fir": ["kuusi"]
    }
    print(original_dict)
    reversed_dict = reverce_dict(original_dict)
    print(reversed_dict)


if __name__ == "__main__":
    main()
