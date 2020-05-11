import argparse


class Square:
    def __init__(self, p1, p2):
        print(
            f"Square created p1=({p1[0]}, {p1[1]}) p2=({p2[0]}, {p2[1]})"
        )


class Product:
    def __init__(self, title, description):
        print(
            f"Product created title='{title}' description='{description}'"
        )


CREATE = 'create'
UPDATE = 'update'
LIST = 'list'
DELETE = 'delete'

PRODUCT = 'product'
SQUARE = 'square'


def main():
    parser = argparse.ArgumentParser(
        description="Manages products and plans over REST API"
    )
    parser.add_argument(
        "operation",
        choices=(CREATE, UPDATE, LIST, DELETE)
    )
    parser.add_argument(
        "model",
        choices=(PRODUCT, SQUARE)
    )
    parser.add_argument(
        "-t", "--title",
        default="Default title"
    )
    parser.add_argument(
        "-d", "--description",
        default="Default description"
    )
    parser.add_argument(
        "-p1", nargs=2,
        help="Upper left coordinate, specified as X Y",
        default=(0, 0)
    )
    parser.add_argument(
        "-p2", nargs=2,
        help="Lower right coordinate, specified as X Y",
        default=(600, 600)
    )
    parser.add_argument(
        "-s", "--tls",
        action="store_true"
    )
    args = parser.parse_args()

    if args.tls:
        print("REST API over TLS")

    if args.operation == CREATE:
        if args.model == PRODUCT:
            Product(title=args.title, description=args.description)
        elif args.model == SQUARE:
            Square(args.p1, args.p2)


if __name__ == '__main__':
    main()
