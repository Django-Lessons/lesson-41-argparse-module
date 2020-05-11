import argparse


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
PLAN = 'plan'


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
        choices=(PRODUCT, PLAN)
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
        "-s", "--tls",
        action="store_true"
    )
    args = parser.parse_args()

    if args.tls:
        print("REST API over TLS")

    if args.operation == CREATE:
        if args.model == PRODUCT:
            Product(title=args.title, description=args.description)


if __name__ == '__main__':
    main()
