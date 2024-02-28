import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", "-t", action=argparse.BooleanOptionalAction)

args = parser.parse_args()

if args.test:
    print("!!")
else:
    print("??")