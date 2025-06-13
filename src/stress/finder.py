from src.words.classes import Word
from src.stress.monosyllables import MONOSYLLABLES
from src.stress.structs import *



class StressFinder():
    def __init__(self):
        pass


    def run(self, word: Word) -> int:
        num_syllables = len(word)

        if num_syllables == 0:
            return -1

        count = 0
        # Checando por acentos que indiquem a sílaba tônica da palavra.
        for index in range(num_syllables - 1, -1, -1):
            # Sílabas "sem núcleo" são ignoradas, porque eles não inteferen
            # na tonicidade de uma palavra.
            if not word[index].has_nucleus():
                continue

            # Checando a primeira letra do núcleo por acento. Mesmo nos casos
            # de ditongo, o acento que indica a tonicidade vai estar na 
            # primeira vogal do núcleo.
            if word[index].nucleus[0] in STRESSABLE_VOWELS:
                word[index].stress = True
                return index 
            count += 1

            # Checando se já foram checadas as três últimas sílabas. Apenas
            # as três últimas sílabas podem ter acento, porque apenas elas
            # podem ser tônicas.
            if count == 3:
                break

        wordstr = word.text()
        if wordstr[0] == '-':
            wordstr = wordstr[1:]

        # Checando por monossílabas átonas.
        if wordstr in MONOSYLLABLES:
            return -1;

        # Checando por oxítonas. Essa checagem só é feita, porque a terminação
        # "ão" que torna as palavras oxítonas se confudem com a terminação "o"
        # que torna as palavras paroxítonas.
        if wordstr.endswith(PAROXYTONE_ENDS):
            word[num_syllables - 1].stress = True
            return num_syllables - 1

        # Checando por paroxítonas.
        if wordstr.endswith(OXYTONE_ENDS):
            if word[num_syllables - 2].has_nucleus():
                word[num_syllables - 2].stress = True
                return num_syllables - 2
            word[num_syllables - 3].stress = True
            return num_syllables - 3

        # Todas as palavras que não passarem nos testes acima são consideras
        # paroxítonas. Os testes acima devem pegar 100% das palavras que não
        # são paroxítonas e que seguem os padrões de acentuação e grafia da
        # língua portuguesa. Além disso, paroxítonas é o padrão da língua, se
        # por acaso houver alguma palavra não segue o padrão, é bem provável
        # que ela seja paroxítonas.
        word[num_syllables - 1].stress = True
        return num_syllables - 1
