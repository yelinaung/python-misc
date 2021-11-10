"""
__slot__ Magic
"""


class NoSlot:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class WithSlot:
    __slots__ = ["name", "identifier"]

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
