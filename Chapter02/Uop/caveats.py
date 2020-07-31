from collections import UserList


def wrong_user_display(user_metadata: dict = {"name": "john", "age": 30}):
    # name = user_metadata.pop("name")
    # age = user_metadata.pop("age")
    name = user_metadata["name"]
    age = user_metadata["age"]

    return f"{name} {age}"


def Correct_user_display(user_metadata: dict = None):
    user_metadata = user_metadata or {"name": "john", "age": 30}

    name = user_metadata.pop("name")
    age = user_metadata.pop("age")

    return f"{name} {age}"


class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] {value}"


class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] {value}"
