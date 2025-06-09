from dataclasses import dataclass, field

### LIST OF NODES
# - NodePhrase
# - NodeVerse
# > WORDS
#  - NodeWord
#  - NodeManualWord
#  - NodeTiedWords
#  - NodeUntiedWords
#  - NodeTiedSubwords
#  - NodeUntiedSubwords
#  - NodeStressedWord
#  - NodeUnstressedWord
# > FRAGMENTS
#  - NodeFragment
#  - NodeFragments
#  - NodeStressedFragment
#  - NodeJoinedFragments
#  - NodeUncountedFragment

@dataclass
class NodePhrase:
    children: tuple['NodePhrase', ...] = field(default_factory=tuple)

    def __init__(self, *args: 'NodePhrase') -> None:
        self.children = args


@dataclass(init=False)
class NodeVerse(NodePhrase):
    pass


@dataclass
class NodeWord(NodePhrase):
    value: str = field(default_factory=str)

    def __init__(self, value: str, *args: NodePhrase) -> None:
        self.value = value
        super().__init__(*args)


@dataclass(init=False)
class NodeManualWord(NodePhrase):
    pass


@dataclass(init=False)
class NodeFragments(NodePhrase):
    pass


@dataclass(init=False)
class NodeFragment(NodePhrase):
    pass


@dataclass(init=False)
class NodeStressedFragment(NodePhrase):
    pass


@dataclass(init=False)
class NodeJoinedFragments(NodePhrase):
    pass


@dataclass(init=False)
class NodeUncountedFragment(NodePhrase):
    pass


@dataclass(init=False)
class NodeTiedWords(NodePhrase):
    pass


@dataclass(init=False)
class NodeUntiedWords(NodePhrase):
    pass


@dataclass(init=False)
class NodeTiedSubwords(NodePhrase):
    pass


@dataclass(init=False)
class NodeUntiedSubwords(NodePhrase):
    pass


@dataclass(init=False)
class NodeStressedWord(NodePhrase):
    pass


@dataclass(init=False)
class NodeUnstressedWord(NodePhrase):
    pass
