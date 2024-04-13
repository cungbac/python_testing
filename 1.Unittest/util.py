from typing import Union

def trim_account_number(val: Union[str, None]) -> str:
    if val is None:
        return ""
    elif len(val) <= 9:
        return val
    else:
        return val[-9:len(val)]