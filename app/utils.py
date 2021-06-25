from typing import Any, Iterator, Dict, List, Union


def check_iterable(obj: Dict[str, Union[str, List[str]]]) -> bool:
    """check iterable if values are defined"""
    return all(get_values(obj))


def get_values(obj: Any) -> Iterator[str]:
    """get all values of nested dict"""
    values = obj.values() if isinstance(obj, dict) else obj
    for sub_obj in values:
        if isinstance(sub_obj, (list, dict)):
            yield from get_values(sub_obj)
        else:
            yield sub_obj
