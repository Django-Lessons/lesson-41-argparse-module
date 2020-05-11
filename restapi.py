import argparse

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
    parser.parse_args()


if __name__ == '__main__':
    main()
