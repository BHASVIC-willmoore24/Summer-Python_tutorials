

# Enums are a set of names linked to value.
# Allows for constants, as Python does not include a way of enforcing a variable to not change

from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State['INACTIVE'])
print(list(State))
