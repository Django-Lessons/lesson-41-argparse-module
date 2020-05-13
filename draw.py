import argparse


CIRCLE = 'circle'
SQUARE = 'square'


class Square:
    def __init__(self, p1, p2):
        print("Square")


class Circle:
    def __init__(self, p1, radius):
        print(f"Circle center=({p1[0]}, {p1[1]}) radius={radius}")


def circle_func(args):
    Circle(args.center, args.radius)


def square_func(args):
    Square(args.point1, args.point2)


def handle_circle_args(subparsers):
    parser = subparsers.add_parser(CIRCLE)

    parser.add_argument(
        "radius"
    )
    parser.add_argument(
        "-c", "--center", nargs=2,
        help="Center of the circle",
        default=(0, 0),
        metavar=("x", "y")
    )
    parser.set_defaults(func=circle_func)


def handle_square_args(subparsers):
    parser = subparsers.add_parser(SQUARE)

    parser.add_argument(
        "-p1", "--point1",
        nargs=2,
        help="Upper left coordinate, specified as X Y",
        default=(0, 0),
        metavar=("x", "y")
    )
    parser.add_argument(
        "-p2", "--point2",
        nargs=2,
        help="Lower right coordinate, specified as X Y",
        default=(600, 600)
    )
    parser.set_defaults(func=square_func)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', '--optimize',
        action="store_true",
        default=False
    )

    subparsers = parser.add_subparsers()

    handle_circle_args(subparsers)
    handle_square_args(subparsers)

    args = parser.parse_args()
    args.func(args)

    if args.optimize:
        print("Optimized algorithm")
    else:
        print("...")


if __name__ == '__main__':
    main()

