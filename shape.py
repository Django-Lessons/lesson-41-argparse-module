import argparse


class Square:
    def __init__(self, p1, p2):
        print(
            f"Square created p1=({p1[0]}, {p1[1]}) p2=({p2[0]}, {p2[1]})"
        )


class Circle:
    def __init__(self, p1, radius):
        print(
            f"Circle p1=({p1[0]}, {p1[1]}) radius='{radius}'"
        )


SQUARE = 'square'
CIRCLE = 'circle'


def square_func(args):
    if args.optimize:
        print("Optimized rendering")

    for item in range(0, args.count):
        Square(args.p1, args.p2)


def square_args(subparsers):
    square_par = subparsers.add_parser('square')

    square_par.add_argument(
        "-p1", nargs=2,
        help="Upper left coordinate, specified as X Y",
        default=(0, 0),
        metavar=("x", "y")
    )
    square_par.add_argument(
        "-p2", nargs=2,
        help="Lower right coordinate, specified as X Y",
        default=(600, 600)
    )
    square_par.set_defaults(func=square_func)


def circle_func(args):
    if args.optimize:
        print("Optimized rendering")

    for item in range(0, args.count):
        Circle(args.center, args.radius)


def circle_args(subparsers):
    circle_par = subparsers.add_parser('circle')
    circle_par.add_argument(
        "--center", nargs=2,
        help="Center of the circle",
        default=(0, 0),
        metavar=("x", "y")
    )
    circle_par.add_argument(
        "radius"
    )
    circle_par.set_defaults(func=circle_func)


def main():
    parser = argparse.ArgumentParser(
        description="Renders geometrical shapes"
    )
    parser.add_argument(
        "-o", "--optimize",
        action="store_true"
    )
    parser.add_argument(
        "--output",
        help="Path to the file where to render shapes"
    )
    parser.add_argument(
        "--count",
        type=int,
        help="Number of shapes to render",
        default=1
    )
    subparsers = parser.add_subparsers()
    circle_args(subparsers)
    square_args(subparsers)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()

