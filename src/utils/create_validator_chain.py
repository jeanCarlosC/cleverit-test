from src.utils.validator_base import ValidatorBase
from typing import List


def create_validator_chain(array_validators: List[ValidatorBase]) -> ValidatorBase:
    main_validator = array_validators[0]
    for i in range(len(array_validators) - 1):
        element = array_validators[i]
        element_next = array_validators[i + 1]
        element.set_next(element_next)
    return main_validator
