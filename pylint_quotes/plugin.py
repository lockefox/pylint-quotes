"""Module which defines the required register method
for Pylint plugins.
"""

def register(linter):
    """Required method to auto register this checker.

    Args:
        linter: Main interface object for Pylint plugins.
    """
    from pylint_quotes.checker import StringQuoteChecker
    linter.register_checker(StringQuoteChecker(linter))
