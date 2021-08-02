from dataclasses import dataclass

@dataclass
class Company:
    index: int
    company: str

# NOTE: other option was to do this, but it does not provide the IDE with much help
"""
class Company:
    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])

    def __getattribute__(self, name: str):
        return getattr(self, name)
"""