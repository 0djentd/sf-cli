import logging
import argparse
import curses
import re


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class UI():
    parser: argparse.ArgumentParser
    cli_args: argparse.Namespace

    def __init__(self):
        parser = self.__get_parser()
        cli_args = parser.parse_args()
        self.cli_args = cli_args
        self.parser = parser

    @staticmethod
    def __get_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        parser.add_argument("-v", type=bool, default=False, help="Display additional info")
        parser.add_argument("--db", type=str,   required=False, help="db file")

        subparsers = parser.add_subparsers(help='command')

        add = subparsers.add_parser('add', help='Add new flashcard')
        add.add_argument("front", type=str, required=True)
        add.add_argument("back", type=str, required=True)

        remove = subparsers.add_parser('remove', help='Remove flashcard')
        remove.add_argument("front", type=str, required=False)
        remove.add_argument("back", type=str, required=False)

        review = subparsers.add_parser('review', help='Review flashcards')
        review.add_argument("-m", "--max", type=int, default=1000)
        return parser
