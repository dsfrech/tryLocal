""" Block Comment
spells = [      # List
    "ridd",
    "wing",
    "avad",
    "expe",
    "nox!",
    "lumo"
]
print(spells[4])

quotes = {      # Dictionary
    "moe":"A wise guys, huh?",
    "larry": "ow!",
    "curly": "nyuk nyuk!",
}
stooge = "curly"
print(stooge, "says:", quotes[stooge])
"""
# Below uses a docstring """Capital letter...end with period"""
# You access the documentation with print(add.__doc__)
def add(value1, value2):
    """Calculate the sum of value1 and value2."""
    return value1 + value2
print(add.__doc__)