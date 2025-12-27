# Writing Comments in Python: Best Practices & Techniques

# Single-line comments are written using the # symbol
# This is a single-line comment
error_count = 0  # Initialize error counter

# TODO: Handle case when argument is None

# Avoid writing comments that simply restate what the code already makes clear
# error_count = 0  # Initializing error counter ❌ (too obvious)

# Instead, focus comments on why or how, not what:
# Reset count to zero before processing next batch
error_count = 0

# Multi-line (Block) Comments
# Option 1: Multiple # Symbols
# This block checks the preconditions
# and logs a message if they are met
ready = True
if ready:
    print("Executing...")

# Option 2: Triple Quotes (used sparingly)
'''
This is a block comment
written using triple single quotes
'''

"""
This is another multi-line comment
using triple double quotes
"""

