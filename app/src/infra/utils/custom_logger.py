class CustomLogger:

    def __init__(self):
        self.__events = {}

    def add_event(self, loc: str, message: str):
        item_num = len(self.__events) + 1
        self.__events[f"{item_num}: {loc}"] = message

    def dumps(self):
        print(self.__events)
