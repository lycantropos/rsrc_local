from pathlib import Path
from tempfile import (mkdtemp,
                      mktemp)
from typing import Tuple

from hypothesis import strategies

from tests.utils import (temporary_directory_path_string,
                         touch)

existent_directories_paths_strings = strategies.builds(
        mkdtemp,
        dir=strategies.just(temporary_directory_path_string))


def fill_directory(path_string_with_counts: Tuple[str, int, int]) -> str:
    (path_string,
     sub_directories_count,
     sub_files_count) = path_string_with_counts
    for _ in range(sub_directories_count):
        mkdtemp(dir=path_string)
    for _ in range(sub_files_count):
        touch(mktemp(dir=path_string))
    return path_string


sub_directories_counts = strategies.integers(1, 100)
sub_files_counts = strategies.integers(1, 100)
non_empty_directories_paths_strings = (
    strategies.tuples(existent_directories_paths_strings,
                      sub_directories_counts,
                      sub_files_counts).map(fill_directory))
non_existent_paths_strings = strategies.builds(
        mktemp,
        dir=strategies.just(temporary_directory_path_string))


def make_existent(file_path_string: str) -> str:
    touch(file_path_string)
    return file_path_string


existent_files_paths_strings = (non_existent_paths_strings
                                .map(make_existent))
files_paths_strings = (non_existent_paths_strings
                       | existent_files_paths_strings)
paths_strings = existent_directories_paths_strings | files_paths_strings


def path_string_to_url_string(string: str) -> str:
    return Path(string).as_uri()


existent_directories_paths_url_strings = (existent_directories_paths_strings
                                          .map(path_string_to_url_string))
non_existent_paths_url_strings = (non_existent_paths_strings
                                  .map(path_string_to_url_string))
existent_files_paths_url_strings = (existent_files_paths_strings
                                    .map(path_string_to_url_string))
files_paths_url_strings = (non_existent_paths_url_strings
                           | existent_files_paths_url_strings)
paths_urls_strings = (existent_directories_paths_url_strings
                      | files_paths_url_strings)
