import string
from dataclasses import dataclass


@dataclass
class Name:
    first: string = ""
    last: string = ""

    # "-> string" ser bara till så att dom retunerar strings och inget annat
    def get_first(self) -> string:
        return self.first

    def get_last(self) -> string:
        return self.last

    def to_string(self) -> string:
        return self.first + " " + self.last

    def set_last(self, new_last) -> string:
        self.last = new_last

    def set_first(self, new_first) -> string:
        self.first = new_first

    def get_short_name(self) -> string:
        return self.first[0] + ". " + self.last
