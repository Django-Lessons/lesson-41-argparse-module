import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'shape',
        choices=('circle', 'square')
    )
    parser.add_argument(
        '-o', '--optimize',
        action="store_true",
        default=False
    )
    args = parser.parse_args()

    if args.optimize:
        print("Optimized algorithm")
    else:
        print("...")


if __name__ == '__main__':
    main()

