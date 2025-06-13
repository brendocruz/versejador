from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import overload
from src.syllables.classes import Syllable



@dataclass
class Word(Iterator):
    _syllables: list[Syllable] = field(default_factory=list)
    _index: int = field(default=0, init=False, repr=False)


    def __len__(self) -> int:
        return len(self._syllables)


    @overload
    def __getitem__(self, key: int) -> Syllable: ...
    @overload
    def __getitem__(self, key: slice) -> list[Syllable]: ...
    def __getitem__(self, key: int | slice) -> Syllable | list[Syllable]:
        return self._syllables[key]


    def __next__(self) -> Syllable:
        if self._index >= len(self._syllables):
            self._index = 0
            raise StopIteration
        index = self._index
        self._index += 1
        return self._syllables[index]


    def text(self) -> str:
        return ''.join([syllable.text() for syllable in self._syllables])


    def stressed(self) -> int:
        for index, syllable in enumerate(self._syllables):
            if syllable.has_stress():
                return index
        return -1


    def span_text(self, index: int) -> tuple[int, int]:
        if index >= len(self._syllables):
            return (-1, -1)

        start = 0
        for syllable in self._syllables[0:index]:
            length = len(syllable.text())
            start += length
        end = start + len(self._syllables[index])
        return (start, end)

    
    def span_syllable(self, start: int, end: int) -> tuple[int, ...]:
        word_length = len(self.text())
        if start < 0 or end > word_length:
            return ()
        if start > end:
            return ()

        upper_bound = 0
        span_ranges = [upper_bound]
        for syllables in self._syllables:
            upper_bound += len(syllables.text())
            span_ranges.append(upper_bound)

        indices = set()
        for index, span in enumerate(zip(span_ranges[:-1], span_ranges[1:])):
            lower_bound, upper_bound = span
            if lower_bound <= start and upper_bound > start:
                indices.add(index)
            if lower_bound <= end and upper_bound > end:
                indices.add(index)

        return tuple(indices)


    def find(self, substr: str) -> tuple[int, ...]:
        ranges      = [0]
        upper_bound = 0
        full_word    = ''

        for syllable in self._syllables:
            text        = syllable.text()
            length      = len(text)
            upper_bound += length
            full_word   += text
            ranges.append(upper_bound)

        match_start = full_word.find(substr)
        match_end   = match_start + len(substr)

        select_indices: list[int] = []
        for match_index in range(match_start, match_end):
            for index in range(len(ranges) - 1, -1, -1):
                if match_index >= ranges[index]:
                    select_indices.append(index)
                    break
        return tuple(select_indices)
