import argparse


CIRCLE = 'circle'
SQUARE = 'square'


class Square:
    def __init__(self, p1, p2):
        print("Square")


class Circle:
    def __init__(self, p1, center):
        print("Circle")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'shape',
        choices=(CIRCLE, SQUARE)
    )
    parser.add_argument(
        '-o', '--optimize',
        action="store_true",
        default=False
    )
    parser.add_argument(
        '-c', '--center',
        nargs=2,
        metavar=("x", "y")
    )
    parser.add_argument(
        '-p1', '--point1',
        nargs=2,
        metavar=("x", "y")
    )
    parser.add_argument(
        '-p2', '--point2',
        nargs=2,
        metavar=("x", "y")
    )
    args = parser.parse_args()

    if args.optimize:
        print("Optimized algorithm")
    else:
        print("...")

    if args.shape == CIRCLE:
        Circle()
    elif args.shape == SQUARE:
        Square()


if __name__ == '__main__':
    main()

