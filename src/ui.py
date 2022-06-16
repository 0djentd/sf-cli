import logging
import argparse


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class UI():
    parser: argparse.ArgumentParser
    cli_args: argparse.Namespace

    def __init__(self):
        parser = self.__get_parser()
        logger.debug(parser)
        cli_args = parser.parse_args()
        logger.debug(cli_args)
        self.cli_args = cli_args
        self.parser = parser
        self.__set_logging_level()

    def __set_logging_level(self):
        if self.cli_args.verbose == 1:
            level = logging.INFO
        elif self.cli_args.verbose == 2:
            level = logging.WARNING
        elif self.cli_args.verbose >= 3:
            level = logging.DEBUG
        else:
            level = logging.ERROR
        logging.basicConfig(level=level)

    @staticmethod
    def __get_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        parser.add_argument("-v", "--verbose",
                            action="count", default=0,
                            help="Display additional info")
        parser.add_argument("--db", type=str, required=False, help="db file")

        subparsers = parser.add_subparsers(help='command')

        add = subparsers.add_parser('add', help='Add new flashcard')
        add.add_argument("front", type=str)
        add.add_argument("back", type=str)

        remove = subparsers.add_parser('remove', help='Remove flashcard')
        remove.add_argument("front", type=str)
        remove.add_argument("back", type=str)

        review = subparsers.add_parser('review', help='Review flashcards')
        review.add_argument("-m", "--max", type=int, default=1000)
        return parser
