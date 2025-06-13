from unittest import TestCase
from src.syllables.classes import Syllable
from src.words.classes import Word



class TestWordClass(TestCase):

    def test_length_when_empty(self):
        word = Word()
        self.assertEqual(0, len(word.text()))



    def test_length_when_not_empty(self):
        syllables  = []
        syllable_1 = Syllable(onset='b', nucleus='a')
        syllable_2 = Syllable(onset='n', nucleus='a')
        syllable_3 = Syllable(onset='n', nucleus='a')
        syllables.extend([syllable_1, syllable_2, syllable_3])

        word = Word(syllables)
        self.assertEqual(6, len(word.text()))



    def test_str_when_empty(self):
        word = Word()
        self.assertEqual('', word.text())



    def test_str_when_not_empty(self):
        syllables  = []
        syllable_1 = Syllable(onset='b', nucleus='a')
        syllable_2 = Syllable(onset='n', nucleus='a')
        syllable_3 = Syllable(onset='n', nucleus='a')
        syllables.extend([syllable_1, syllable_2, syllable_3])

        word = Word(syllables)
        self.assertEqual('banana', word.text())


    def test_find(self):
        syllable_1 = Syllable(onset='s', nucleus='a')
        syllable_2 = Syllable(onset='',  nucleus='ú')
        syllable_3 = Syllable(onset='d', nucleus='e')
        syllables  = [syllable_1, syllable_2, syllable_3]
        word       = Word(syllables)

        indices = word.find('aú')
        self.assertTupleEqual(indices, (0, 1))


        syllable_1 = Syllable(onset='v', nucleus='í')
        syllable_2 = Syllable(onset='d', nucleus='e')
        syllable_3 = Syllable(onset='',  nucleus='o')
        syllables  = [syllable_1, syllable_2, syllable_3]
        word       = Word(syllables)

        indices = word.find('eo')
        self.assertTupleEqual(indices, (1, 2))

    def test_stess(self):
        syllable_1 = Syllable(onset='l', nucleus='a', coda='')
        syllable_2 = Syllable(onset='r', nucleus='a', coda='n', stress=True)
        syllable_3 = Syllable(onset='j', nucleus='a', coda='')
        syllables  = [syllable_1, syllable_2, syllable_3]
        word       = Word(syllables)
        self.assertEqual(word.stressed(), 1)


        syllable_1 = Syllable(onset='d', nucleus='e')
        syllables  = [syllable_1]
        word       = Word(syllables)
        self.assertEqual(word.stressed(), -1)




    def test_span_text(self):
        syllable_1 = Syllable(onset='l', nucleus='a', coda='')
        syllable_2 = Syllable(onset='r', nucleus='a', coda='n')
        syllable_3 = Syllable(onset='j', nucleus='a', coda='')
        syllables  = [syllable_1, syllable_2, syllable_3]
        word       = Word(syllables)

        self.assertTupleEqual(word.span_text(0), ( 0,  2))
        self.assertTupleEqual(word.span_text(1), ( 2,  5))
        self.assertTupleEqual(word.span_text(2), ( 5,  7))
        self.assertTupleEqual(word.span_text(3), (-1, -1))



    def test_span_syllable(self):
        syllable_1 = Syllable(onset='l', nucleus='a', coda='')
        syllable_2 = Syllable(onset='r', nucleus='a', coda='n')
        syllable_3 = Syllable(onset='j', nucleus='a', coda='')
        syllables  = [syllable_1, syllable_2, syllable_3]
        word       = Word(syllables)

        self.assertTupleEqual(word.span_syllable(4, 5), (1, 2))
        self.assertTupleEqual(word.span_syllable(10, 15), ())
        self.assertTupleEqual(word.span_syllable(5,  3), ())
        self.assertTupleEqual(word.span_syllable(2, 2), (1, ))
