"""R-5.10: The constructor for the CaesarCipher class in Code Fragment 5.11
can be implemented with a two-line body by building the forward and backward
strings using a combination of the join method and an appropriate
comprehension syntax. Give such an implementation"""

# essentially this question is asking to rewrite the __init__ into two lines
# one line for the self._forward and one for self._backward.

# within the __init__ function


class CaesarCipher:
    # i like the original better since you avoid idioms for readibility
    def __init__(self, shift) -> None:
        self._forward = "".join(chr((k + shift) % 26 + ord("A")) for k in range(26))
        self._backward = "".join(chr((k - shift) % 26 + ord("A")) for k in range(26))
