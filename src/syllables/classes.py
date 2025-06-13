from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Optional, overload
from src.syllables.structs import ALL_ONSET_DIGRAPHS



@dataclass
class Syllable:
    prefix:   str = field(default_factory=str, kw_only=True)
    onset:    str = field(default_factory=str, kw_only=True)
    nucleus:  str = field(default_factory=str, kw_only=True)
    coda:     str = field(default_factory=str, kw_only=True)
    stress:  bool = field(default=False, kw_only=True)

    
    def __len__(self) -> int:
        return len(self.text())


    def text(self) -> str:
        return f'{self.prefix}{self.onset}{self.nucleus}{self.coda}'


    def parts(self) -> list[str]:
        return [self.prefix, self.onset, self.nucleus, self.coda]


    def has_onset(self) -> bool:
        return self.onset != ''


    def has_coda(self) -> bool:
        return self.coda != ''


    def has_nucleus(self) -> bool:
        return self.nucleus != ''


    def has_diphthong(self) -> bool:
        return len(self.nucleus) > 1


    def has_onset_digraph(self) -> bool:
        return self.onset in ALL_ONSET_DIGRAPHS


    def has_onset_cluster(self) -> bool:
        if len(self.onset) <= 1:
            return False
        if self.onset in ALL_ONSET_DIGRAPHS:
            return False
        return True


    def has_coda_cluster(self) -> bool:
        return len(self.coda) > 1


    def has_stress(self) -> bool:
        return self.stress



@dataclass
class PoeticSyllable(Iterator):
    _items:   list[Syllable] = field(default_factory=list)
    prefix:     Optional[str] = field(default=None, kw_only=True)
    stress:              bool = field(default=False, kw_only=True)
    mergeable:           bool = field(default=True, kw_only=True)
    _index:               int = field(init=False, repr=False)


    def __post_init__(self):
        for syllable in self._items:
            if syllable.has_stress():
                self.stress = True
        self._index = 0


    def __len__(self) -> int:
        return len(self._items)


    @overload
    def __getitem__(self, key: int) -> Syllable: ...
    @overload
    def __getitem__(self, key: slice) -> list[Syllable]: ...
    def __getitem__(self, key: int | slice) -> Syllable | list[Syllable]:
        return self._items[key]


    def __next__(self) -> Syllable:
        if self._index >= len(self):
            self._index = 0
            raise StopIteration
        index = self._index
        self._index += 1
        return self._items[index]


    def is_empty(self) -> bool:
        if self.prefix:
            return False
        if self._items:
            return False
        return True


    def text(self, delim: str, stress_prefix: str = '') -> str:
        source_text: list[str] = []
        if self.prefix:
            source_text.append(self.prefix)

        for syllable in self._items:
            source_text.append(syllable.text())

        output_text = delim.join(source_text)
        if self.stress:
            output_text = f'{stress_prefix}{output_text}'
        
        return output_text

    
    def has_onset(self) -> bool:
        if self.prefix:
            return True
        if not self._items:
            return False
        return self._items[0].has_onset()


    def has_coda(self) -> bool:
        if not self._items:
            return False
        return self._items[-1].has_coda()


    def add_prefix(self, other: 'PoeticSyllable') -> None:
        target = other._items[-1]
        codalen = len(target.coda)

        if codalen == 1:
            self.prefix = target.coda
            target.coda = ''
            return
        if codalen > 1:
            coda = target.coda
            new_onset = coda[-1]
            new_coda  = coda[:-1]
            self.prefix = new_onset
            target.coda = new_coda
            return
    

    def append(self, syllable: Syllable):
        self._items.append(syllable)
        if syllable.has_stress():
            self.stress = True


    def extend(self, other: 'PoeticSyllable'):
        self._items.extend(other._items)
        for syllable in other._items:
            if syllable.has_stress():
                self.stress = True
