from pathlib import Path


def implication(antecedent: bool, consequent: bool) -> bool:
    return not antecedent or consequent


def equivalence(left_statement: bool, right_statement: bool) -> bool:
    return not left_statement ^ right_statement


def touch(file_path_string: str) -> None:
    Path(file_path_string).touch()
