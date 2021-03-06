# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['say_hello', 'say_goodbye', 'HelloSayer']

# Cell
def say_hello(to:str) -> str:
    """Say hello to somebody.

       to: Who to say helo to
    Returns a salutation to
    """
    return f'Hello <b>{to}</b>! 👋'

# Cell
def say_goodbye(to:str) -> str:
    """Say goodbye to somebody.

       to: Who to say helo to
    """
    return f'Bye {to}'

# Cell
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to: str) -> None: self.to = to

    def say(self) -> str:
        "Do the saying"
        return say_hello(self.to)