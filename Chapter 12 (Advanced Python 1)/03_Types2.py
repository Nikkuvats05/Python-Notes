from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]   # A list namw as "number" can only contain int.

#Tuple of a string and an integer
person: Tuple [str, int] = ("Alice", 30)     # A list name as "person" can  contain int and string values also.

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85, 88: "bnc"}  

# Union type for variables that can hold multiple types
identifier: Union [int, str] = "ID123"  # Union means can cointain anytype of data.
identifier = 12345 # Also valid

