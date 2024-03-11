import argparse
from scrapper import scrape_fbref


def main():
    parser = argparse.ArgumentParser(description='Scrapes FBRef player stats.')
    parser.add_argument('url', metavar='URL', type=str,
                        help='URL of the FBRef page')
    args = parser.parse_args()
    scrape_fbref(args.url)


if __name__ == "__main__":
    main()
