import argparse
import random
import re

import yaml


def read_ruleset(file_path):
    with open(file_path, 'rt') as input_file:
        rules_dict = yaml.load(input_file, Loader=yaml.FullLoader)
    return rules_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Initialize pattern matching NLP")
    parser.add_argument('--ruleset_path', metavar='ruleset_path', type=str, nargs=1,
                        help='Path to the ruleset yaml file', required=True)
    args = parser.parse_args()
    ruleset_dict = read_ruleset(args.ruleset_path[0])
    try:
        default_resp = ruleset_dict.pop('Default')
    except KeyError:
        default_resp = ['I do not understand']

    while True:
        print(">")
        sentence = input()
        if sentence.lower() == "bye":
            print("Good bye! I hope I helped you!")
            break
        for regex, resp in ruleset_dict.items():
            match = re.search(regex, sentence, re.IGNORECASE)
            if match:
                response_format = resp[random.randrange(len(resp))]
                print(response_format.format(*match.groups()))
                break
        else:
            response = default_resp[random.randrange(len(default_resp))]
            print(response)
