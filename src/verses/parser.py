from typing import Optional
from src.verses.nodes import *
from src.verses.tokens import TokenKind, Token
from src.verses.scanner import VerseScanner
from src.utils.mixins import ReprMixin
from src.verses.errors import ParseError

class VerseParser(ReprMixin):
    scanner: VerseScanner
    lookaheads: tuple[Optional[Token], Optional[Token]]

    def __init__(self, scanner: VerseScanner):
        self.scanner = scanner
        self.lookaheads = (None, None)


    def at_eof(self) -> bool:
        if not self.scanner.at_eof():
            return False
        if not self.lookaheads[0]:
            return True
        if self.lookaheads[0].kind == TokenKind.EOF:
            return True
        return False


    def peek_token(self) -> tuple[Token, Token]:
        lookahead1: Optional[Token] = self.lookaheads[0]
        lookahead2: Optional[Token] = self.lookaheads[1]
        if lookahead1 is None:
            lookahead1 = self.scanner.pop_token()
            lookahead2 = self.scanner.pop_token()
        if lookahead2 is None:
            lookahead2 = self.scanner.pop_token()
        self.lookaheads = (lookahead1, lookahead2)
        return self.lookaheads


    def pop_token(self) -> Token:
        tokens = self.peek_token()
        self.lookaheads = (tokens[1], None)
        return tokens[0]


    def pop_or_error(self, target: TokenKind) -> Token:
        result = self.pop_token()
        if result.kind != target:
            index = self.scanner.index
            raise ParseError(index, f'Expected {target}, but got {result.kind}.')
        return result


    def parse_fragment(self) -> NodeFragment:
        string = self.parse_word()
        fragment = NodeFragment(string)
        return fragment


    def parse_joined_fragments(self) -> NodeJoinedFragments:
        fragments: list[NodeWord] = []
        while True:
            token  = self.pop_or_error(TokenKind.STRING)
            string = NodeWord(token.value)
            fragments.append(string)

            lookahead, _ = self.peek_token()
            if lookahead.kind == TokenKind.UNDERSCORE:
                self.pop_token()
                continue
            break
        return NodeJoinedFragments(*fragments)


    def parse_fragment_or_joined_fragments(self) -> NodeJoinedFragments | NodeFragment:
        lookaheads = self.peek_token()
        if lookaheads[1].kind == TokenKind.UNDERSCORE:
            return self.parse_joined_fragments()
        return self.parse_fragment()


    def parse_stressed_fragment(self) -> NodeStressedFragment:
        self.pop_or_error(TokenKind.PLUS)
        fragment = self.parse_fragment_or_joined_fragments()
        stressed = NodeStressedFragment(fragment)
        return stressed


    def parse_uncounted_fragment(self) -> NodeUncountedFragment:
        self.pop_or_error(TokenKind.DOUBLE_DASH)
        fragment_string = self.parse_word()
        fragment_rest = NodeUncountedFragment(fragment_string)
        return fragment_rest


    def parse_fragment_nodes(self) -> NodeFragment | NodeJoinedFragments | NodeStressedFragment | NodeUncountedFragment:
        lookaheads = self.peek_token()
        if lookaheads[0].kind == TokenKind.PLUS:
            return self.parse_stressed_fragment()
        if lookaheads[0].kind == TokenKind.STRING:
            return self.parse_fragment_or_joined_fragments()
        if lookaheads[0].kind == TokenKind.DOUBLE_DASH:
            return self.parse_uncounted_fragment()
        message = 'Could not parse <auto-word>'
        raise ParseError(self.scanner.index, message)


    def parse_fragments(self) -> NodeFragments:
        self.pop_or_error(TokenKind.PIPE)
        strings = []
        while True:
            string_token = self.parse_fragment_nodes()
            strings.append(string_token)
            self.pop_or_error(TokenKind.PIPE)
            first, second = self.peek_token()
            if first.kind == TokenKind.STRING:
                if second.kind == TokenKind.PIPE:
                    continue
                if second.kind == TokenKind.UNDERSCORE:
                    continue
                break
            if first.kind == TokenKind.PLUS:
                continue
            if first.kind == TokenKind.DOUBLE_DASH:
                continue
            break
        return NodeFragments(*strings)


    def parse_word(self) -> NodeWord:
        token  = self.pop_or_error(TokenKind.STRING)
        return NodeWord(token.value)


    def parse_auto_word(self) -> NodeWord | NodeTiedSubwords | NodeUntiedSubwords:
        left_token = self.parse_word()
        left_side  = NodeWord(left_token.value)
        while True:
            lookahead, _ = self.peek_token()
            if lookahead.kind == TokenKind.CIRCUMFLEX:
                self.pop_token()
                right_token  = self.parse_word()
                right_side = NodeWord(right_token.value)
                left_side = NodeTiedSubwords(left_side, right_side)
                continue
            if lookahead.kind == TokenKind.TILDE:
                self.pop_token()
                right_token  = self.parse_word()
                right_side = NodeWord(right_token.value)
                left_side = NodeUntiedSubwords(left_side, right_side)
                continue
            break
        return left_side


    def parse_manual_word(self) -> NodeManualWord:
        self.pop_or_error(TokenKind.OPEN_BRACKET)
        left_token  = self.pop_or_error(TokenKind.STRING)
        left_side = NodeWord(left_token.value)
        strings = [left_side]

        while True:
            token = self.pop_token()
            if token.kind == TokenKind.PIPE:
                right_token = self.pop_or_error(TokenKind.STRING)
                right_side  = NodeWord(right_token.value)
                strings.append(right_side)
                continue
            if token.kind == TokenKind.CLOSE_BRACKET:
                break
            message = 'Could not parse <auto-word>'
            raise ParseError(self.scanner.index, message)
        return NodeManualWord(*strings)


    def parse_stressed_word_or_unstressed_word(self) -> NodeStressedWord | NodeUnstressedWord:
        lookahead, _ = self.peek_token()
        if lookahead.kind == TokenKind.GREATER_THAN:
            self.pop_token()
            token = self.pop_or_error(TokenKind.STRING)
            string = NodeWord(token.value)
            return NodeStressedWord(string)
        if lookahead.kind == TokenKind.LESS_THAN:
            self.pop_token()
            token = self.pop_or_error(TokenKind.STRING)
            string = NodeWord(token.value)
            return NodeUnstressedWord(string)
        message = 'Could not parse <stressed-word>'
        raise ParseError(self.scanner.index, message)


    def parse_full_word(self) -> NodePhrase:
        lookahead, _ = self.peek_token()
        if lookahead.kind == TokenKind.STRING:
            return self.parse_auto_word()
        if lookahead.kind == TokenKind.PIPE:
            return self.parse_fragments()
        if lookahead.kind == TokenKind.OPEN_BRACKET:
            return self.parse_manual_word()
        if lookahead.kind == TokenKind.GREATER_THAN:
            return self.parse_stressed_word_or_unstressed_word()
        if lookahead.kind == TokenKind.LESS_THAN:
            return self.parse_stressed_word_or_unstressed_word()
        message = 'Could not parse <full-word>'
        raise ParseError(self.scanner.index, message)


    def parse_phrase(self) -> NodePhrase:
        left_phrase = self.parse_full_word()
        while True:
            lookahead, _ = self.peek_token()
            if lookahead.kind == TokenKind.ASTERISK:
                self.pop_token()
                right_phrase = self.parse_full_word()
                left_phrase = NodeTiedWords(left_phrase, right_phrase)
                continue
            if lookahead.kind == TokenKind.SLASH:
                self.pop_token()
                right_phrase = self.parse_full_word()
                left_phrase = NodeUntiedWords(left_phrase, right_phrase)
                continue
            break
        return left_phrase


    def parse_verse(self) -> NodeVerse:
        phrases = []
        while not self.at_eof():
            phrase = self.parse_phrase()
            phrases.append(phrase)
        return NodeVerse(*phrases)


    def parse(self) -> NodeVerse:
        return self.parse_verse()
