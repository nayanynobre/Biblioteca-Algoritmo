import os
from typing import Callable 

ADMIN_PRIORITY = 1
USER_PRIORITY = 0

def ask(question : str) -> str:
    return input(question)

def ask_num(question : str):
    answer = ask(question)
    return "0" if answer == "" else answer

def ask_int(question : str) -> int:
    return int(ask_num(question))

def ask_float(question : str) -> float:
    return float(ask_num(question))


def say_listed(to_say : list[str]):
    idx = 1
    for say in to_say:
        print(f'{idx}. {say}')
        idx += 1

def ask_dict(to_say : dict[str, any]) -> str:
    while(True):
        to_say_names =  list(to_say)

        say_listed(to_say_names)
        inserted : str = ask('')

        selected = None
        if inserted.isnumeric():
            try:
                chosen = int(inserted)
                selected = to_say_names[chosen - 1]
            except: 
                continue
        else:
            filtered = filter_list(to_say_names, inserted)
            if len(filtered) != 1:
                continue
            selected = filtered[0]

        if not selected:
            continue
            
        return to_say[selected]

def filter_list(to_filter : list[str], filter_by : str):
    return [x for x in to_filter if x.lower().startswith(filter_by.lower())]

def filter_dict(to_filter : dict[str,any], filter_by : str):
    filtered_keys = filter_list(list[to_filter], filter_by)
    result = {}
    for key in filtered_keys:
        result[key] = to_filter[key]
    return result

def filter_dict_list_by_value(to_filter : list[dict[str, any]], filter_by : str, unwrap_fn : Callable[[dict[str,any]],bool]):
    
    result = []
    for dict in to_filter:
        if unwrap_fn(dict).lower().startswith(filter_by.lower()): 
            result.append(dict)
            break
    return result

def read_file(path : str) -> str:
    if not os.path.exists(path):
        open(path, "x+")
    with open(path) as file:
        loaded = ""
        for line in file.readlines():
            loaded += line
        return loaded
    
def write_file(path : str, to_write : str) -> str:
    with open(path, "w") as file:
        file.writelines(to_write)


def find(to_find, target):
    start = 0
    end = len(to_find) - 1

    while start <= end:
        middle = (start + end)/ 2
        midpoint = to_find[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint