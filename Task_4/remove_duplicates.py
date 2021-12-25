def remove_duplicates(original_dict):
    none_duplicates_dict = {}
    remove_keys = []
    for key, value in original_dict.items():
        if value in none_duplicates_dict.values():
            remove_keys.append(key)
            continue
        none_duplicates_dict[key] = value
    return none_duplicates_dict, remove_keys


def main():
    original_dict = {'id1': 
                        {'name': ['Sara'], 
                            'group': ['quantitative'], 
                            'subjects': ['english, python, science']
                        },
                    'id2': 
                        {'name': ['David'], 
                            'group': ['quantitative'], 
                            'subjects': ['english, python, science']
                        },
                    'id3': 
                            {'name': ['Sara'], 
                            'group': ['quantitative'], 
                            'subjects': ['english, python, science']
                        },
                    'id4': 
                        {'name': ['Surya'], 
                            'group': ['quantitative'], 
                            'subjects': ['english, python, science']
                        },
                    }
    print(original_dict)
    none_duplicates_dict, remove_keys = remove_duplicates(original_dict)
    print(none_duplicates_dict)
    print(remove_keys)
    

if __name__ == "__main__":
    main()
