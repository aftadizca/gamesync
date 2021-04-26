import argparse
from gamelist import add_game


parser = argparse.ArgumentParser()
parser.add_argument(
    "-add",
    type=str,
    action="store",
    nargs=2,
    metavar=("NAME", "LOCATION"),
    help="add game to sync",
)
# parser.add_argument("-add", action="store_true", help="add game to sync")

args = parser.parse_args()

if args.add:
    add_game(args.add[0], args.add[1])


# if __name__ == "__main__":
#     print(args)