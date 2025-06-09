from dataclasses import dataclass
from enum import Enum



LETTER_CHARACTERS = 'abcdefghijklmnopqrstuvwxyzçàáãâéêíóôõú'



class TokenKind(Enum):
    STRING          = 'string'
    CIRCUMFLEX      = '^'
    TILDE           = '~'
    UNDERSCORE      = '_'
    SLASH           = '/'
    ASTERISK        = '*'
    GREATER_THAN    = '>'
    LESS_THAN       = '<'
    PLUS            = '+'
    PIPE            = '|'
    OPEN_BRACKET    = '['
    CLOSE_BRACKET   = ']'
    EOF             = ''
    DOUBLE_DASH     = '--'



@dataclass
class Token:
    kind: TokenKind
    value: str
