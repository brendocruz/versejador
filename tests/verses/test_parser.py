from unittest import TestCase
from src.verses.scanner import VerseScanner
from src.verses.parser import ParseError, VerseParser
from src.verses.nodes import *



class TestParser(TestCase):


    def test_empty(self):
        input   = ''
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()
        self.assertEqual(len(verse.children), 0)


    def test_single_word(self):
        input   = 'vermelho'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()
        self.assertEqual(len(verse.children), 1)

        string = verse.children[0]
        self.assertIsInstance(string, NodeWord)


    def test_multiple_words(self):
        input   = 'vermelho verde azul'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()
        self.assertEqual(len(verse.children), 3)

        string_1 = verse.children[0]
        self.assertEqual(string_1, NodeWord('vermelho'))
        string_2 = verse.children[1]
        self.assertEqual(string_2, NodeWord('verde'))
        string_3 = verse.children[2]
        self.assertEqual(string_3, NodeWord('azul'))


    def test_hyphenated_word(self):
        input   = 'água-viva'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        self.assertEqual(len(verse.children), 2)
        self.assertEqual(verse.children[0], NodeWord('água'))
        self.assertEqual(verse.children[1], NodeWord('-viva'))


    def test_stressed_word(self):
        input   = '> amarelo'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        all_stress = verse.children[0]
        self.assertIsInstance(all_stress, NodeStressedWord)
        string = all_stress.children[0]
        self.assertEqual(string, NodeWord('amarelo'))


    def test_unstressed_word(self):
        input   = '< verde'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        all_unstress = verse.children[0]
        self.assertIsInstance(all_unstress, NodeUnstressedWord)
        string = all_unstress.children[0]
        self.assertEqual(string, NodeWord('verde'))


    def test_tied_subwords(self):
        input   = 'sa ^ udade'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        auto_word = verse.children[0]
        self.assertIsInstance(auto_word, NodeTiedSubwords)
        self.assertEqual(len(auto_word.children), 2)

        string_1 = auto_word.children[0]
        self.assertEqual(string_1, NodeWord('sa'))
        string_2 = auto_word.children[1]
        self.assertEqual(string_2, NodeWord('udade'))


    def test_untied_subwords(self):
        input   = 'sa ~ úde'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        auto_word = verse.children[0]
        self.assertIsInstance(auto_word, NodeUntiedSubwords)
        self.assertEqual(len(auto_word.children), 2)

        string_1 = auto_word.children[0]
        self.assertEqual(string_1, NodeWord('sa'))
        string_2 = auto_word.children[1]
        self.assertEqual(string_2, NodeWord('úde'))


    def test_tied_subwords_and_untied_subwords(self):
        input   = 'sa ^ uda ~ de'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        child_A = verse.children[0]
        self.assertIsInstance(child_A, NodeUntiedSubwords)
        self.assertEqual(len(child_A.children), 2)

        child_A_1 = child_A.children[0]
        self.assertIsInstance(child_A_1, NodeTiedSubwords)
        self.assertEqual(len(child_A_1.children), 2)
        self.assertEqual(child_A_1.children[0], NodeWord('sa'))
        self.assertEqual(child_A_1.children[1], NodeWord('uda'))

        child_A_2 = child_A.children[1]
        self.assertEqual(child_A_2, NodeWord('de'))


    def test_fragments(self):
        input   = '| a | ma | re | lo |'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse   = parser.parse()

        child_A = verse.children[0]
        self.assertIsInstance(child_A, NodeFragments)
        self.assertEqual(len(child_A.children), 4)

        child_A_1 = child_A.children[0]
        self.assertIsInstance(child_A_1, NodeFragment)
        self.assertEqual(len(child_A_1.children), 1)
        self.assertEqual(child_A_1.children[0], NodeWord('a'))

        child_A_2 = child_A.children[1]
        self.assertIsInstance(child_A_2, NodeFragment)
        self.assertEqual(len(child_A_2.children), 1)
        self.assertEqual(child_A_2.children[0], NodeWord('ma'))

        child_A_3 = child_A.children[2]
        self.assertIsInstance(child_A_3, NodeFragment)
        self.assertEqual(len(child_A_3.children), 1)
        self.assertEqual(child_A_3.children[0], NodeWord('re'))

        child_A_4 = child_A.children[3]
        self.assertIsInstance(child_A_4, NodeFragment)
        self.assertEqual(len(child_A_4.children), 1)
        self.assertEqual(child_A_4.children[0], NodeWord('lo'))


    def test_stressed_fragment(self):
        input   = '| a | ma | +re | lo_e | +a | zul |'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse   = parser.parse()

        self.assertEqual(len(verse.children), 1)

        child_A = verse.children[0]
        self.assertIsInstance(child_A, NodeFragments)
        self.assertEqual(len(child_A.children), 6)

        child_A_1 = child_A.children[0]
        self.assertIsInstance(child_A_1, NodeFragment)
        self.assertEqual(len(child_A_1.children), 1)
        self.assertEqual(child_A_1.children[0], NodeWord('a'))

        child_A_2 = child_A.children[1]
        self.assertIsInstance(child_A_2, NodeFragment)
        self.assertEqual(len(child_A_2.children), 1)
        self.assertEqual(child_A_2.children[0], NodeWord('ma'))

        child_A_3 = child_A.children[2]
        self.assertIsInstance(child_A_3, NodeStressedFragment)
        self.assertEqual(len(child_A_3.children), 1)
        child_A_3_1 = child_A_3.children[0]
        self.assertIsInstance(child_A_3_1, NodeFragment)
        self.assertEqual(len(child_A_3_1.children), 1)
        self.assertEqual(child_A_3_1.children[0], NodeWord('re'))

        child_A_4 = child_A.children[3]
        self.assertIsInstance(child_A_4, NodeJoinedFragments)
        self.assertEqual(len(child_A_4.children), 2)
        self.assertEqual(child_A_4.children[0], NodeWord('lo'))
        self.assertEqual(child_A_4.children[1], NodeWord('e'))

        child_A_5 = child_A.children[4]
        self.assertIsInstance(child_A_5, NodeStressedFragment)
        self.assertEqual(len(child_A_5.children), 1)
        child_A_5_1 = child_A_5.children[0]
        self.assertIsInstance(child_A_5_1, NodeFragment)
        self.assertEqual(len(child_A_5_1.children), 1)
        self.assertEqual(child_A_5_1.children[0], NodeWord('a'))

        child_A_6 = child_A.children[5]
        self.assertIsInstance(child_A_6, NodeFragment)
        self.assertEqual(len(child_A_6.children), 1)
        self.assertEqual(child_A_6.children[0], NodeWord('zul'))


    def test_joined_fragments(self):
        input   = '| ca | sa_a_a | zul|'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse   = parser.parse()

        self.assertEqual(len(verse.children), 1)

        child_A = verse.children[0]
        self.assertIsInstance(child_A, NodeFragments)
        self.assertEqual(len(child_A.children), 3)

        child_A_1 = child_A.children[0]
        self.assertIsInstance(child_A_1, NodeFragment)
        self.assertEqual(len(child_A_1.children), 1)
        self.assertEqual(child_A_1.children[0], NodeWord('ca'))

        child_A_2 = child_A.children[1]
        self.assertIsInstance(child_A_2, NodeJoinedFragments)
        self.assertEqual(len(child_A_2.children), 3)
        self.assertEqual(child_A_2.children[0], NodeWord('sa'))
        self.assertEqual(child_A_2.children[1], NodeWord('a'))
        self.assertEqual(child_A_2.children[2], NodeWord('a'))

        child_A_3 = child_A.children[2]
        self.assertIsInstance(child_A_3, NodeFragment)
        self.assertEqual(len(child_A_3.children), 1)
        self.assertEqual(child_A_3.children[0], NodeWord('zul'))


    def test_joined_stressed_fragments(self):
        input   = '|pa|le|+tó_a|+zul|'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse   = parser.parse()

        self.assertEqual(len(verse.children), 1)

        child_A = verse.children[0]
        self.assertIsInstance(child_A, NodeFragments)
        self.assertEqual(len(child_A.children), 4)

        child_A_1 = child_A.children[0]
        self.assertIsInstance(child_A_1, NodeFragment)
        self.assertEqual(len(child_A_1.children), 1)
        self.assertEqual(child_A_1.children[0], NodeWord('pa'))

        child_A_2 = child_A.children[1]
        self.assertIsInstance(child_A_2, NodeFragment)
        self.assertEqual(len(child_A_2.children), 1)
        self.assertEqual(child_A_2.children[0], NodeWord('le'))

        child_A_3 = child_A.children[2]
        self.assertIsInstance(child_A_3, NodeStressedFragment)
        self.assertEqual(len(child_A_3.children), 1)

        child_A_3_1 = child_A_3.children[0]
        self.assertIsInstance(child_A_3_1, NodeJoinedFragments)
        self.assertEqual(len(child_A_3_1.children), 2)
        self.assertEqual(child_A_3_1.children[0], NodeWord('tó'))
        self.assertEqual(child_A_3_1.children[1], NodeWord('a'))

        child_A_4 = child_A.children[3]
        self.assertIsInstance(child_A_4, NodeStressedFragment)
        self.assertEqual(len(child_A_4.children), 1)

        child_A_4_1 = child_A_4.children[0]
        self.assertIsInstance(child_A_4_1, NodeFragment)
        self.assertEqual(child_A_4_1.children[0], NodeWord('zul'))


    def test_hyphenated_fragment(self):
        text   = '|trem|-ba|la|'
        scanner = VerseScanner(text)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        self.assertEqual(len(verse.children), 1)
        

    def test_uncounted_fragment(self):
        input   = '|ma|te|má|--tica|'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse   = parser.parse()

        child_A = verse.children[0]
        self.assertIsInstance(child_A, NodeFragments)
        self.assertEqual(len(child_A.children), 4)

        child_A_1 = child_A.children[0]
        self.assertIsInstance(child_A_1, NodeFragment)
        self.assertEqual(len(child_A_1.children), 1)
        self.assertEqual(child_A_1.children[0], NodeWord('ma'))

        child_A_2 = child_A.children[1]
        self.assertIsInstance(child_A_2, NodeFragment)
        self.assertEqual(len(child_A_2.children), 1)
        self.assertEqual(child_A_2.children[0], NodeWord('te'))

        child_A_3 = child_A.children[2]
        self.assertIsInstance(child_A_3, NodeFragment)
        self.assertEqual(len(child_A_3.children), 1)
        self.assertEqual(child_A_3.children[0], NodeWord('má'))

        child_A_4 = child_A.children[3]
        self.assertIsInstance(child_A_4, NodeUncountedFragment)
        self.assertEqual(len(child_A_4.children), 1)
        self.assertEqual(child_A_4.children[0], NodeWord('tica'))


    def test_tied_words(self):
        input   = 'amarelo * azul'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        fragment_word = verse.children[0]
        self.assertIsInstance(fragment_word, NodeTiedWords)
        self.assertEqual(len(fragment_word.children), 2)

        string_1 = fragment_word.children[0]
        self.assertEqual(string_1, NodeWord('amarelo'))
        string_2 = fragment_word.children[1]
        self.assertEqual(string_2, NodeWord('azul'))


    def test_untied_words(self):
        input   = 'amarelo / azul'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        fragment_word = verse.children[0]
        self.assertIsInstance(fragment_word, NodeUntiedWords)
        self.assertEqual(len(fragment_word.children), 2)

        string_1 = fragment_word.children[0]
        self.assertEqual(string_1, NodeWord('amarelo'))
        string_2 = fragment_word.children[1]
        self.assertEqual(string_2, NodeWord('azul'))


    def test_manual_word(self):
        input   = '[ ver | me | lho ]'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse = parser.parse()

        manual_word = verse.children[0]
        self.assertIsInstance(manual_word, NodeManualWord)
        self.assertEqual(len(manual_word.children), 3)

        string_1 = manual_word.children[0]
        self.assertEqual(string_1, NodeWord('ver'))
        string_2 = manual_word.children[1]
        self.assertEqual(string_2, NodeWord('me'))
        string_3 = manual_word.children[2]
        self.assertEqual(string_3, NodeWord('lho'))


    def test_manual_word_malformed_1(self):
        input   = '[ ver | me lho ]'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)

        with self.assertRaises(ParseError):
            parser.parse()


    def test_manual_word_malformed_2(self):
        input   = '[ [ ver me lho ]'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)

        with self.assertRaises(ParseError):
            parser.parse()


    def test_malformed_full_word(self):
        input   = '] ver | me | lho ]'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)

        with self.assertRaises(ParseError):
            parser.parse()


    def test_malformed_stressed_word(self):
        input   = 'azul >'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)

        with self.assertRaises(ParseError):
            parser.parse_stressed_word_or_unstressed_word()


    def test_malformed_fragments(self):
        input   = '| | ver | me | lho |'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)

        with self.assertRaises(ParseError):
            parser.parse()


    def test_verse(self):
        input   = '|a|ma|re|lo| e [a|zul] são <minhas sa~udades'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse   = parser.parse()

        self.assertEqual(len(verse.children), 6)

        child_A = verse.children[0]
        self.assertIsInstance(child_A, NodeFragments)
        self.assertEqual(len(child_A.children), 4)

        child_A_1 = child_A.children[0]
        self.assertIsInstance(child_A_1, NodeFragment)
        self.assertEqual(len(child_A_1.children), 1)
        self.assertEqual(child_A_1.children[0], NodeWord('a'))

        child_A_2 = child_A.children[1]
        self.assertIsInstance(child_A_2, NodeFragment)
        self.assertEqual(len(child_A_2.children), 1)
        self.assertEqual(child_A_2.children[0], NodeWord('ma'))

        child_A_3 = child_A.children[2]
        self.assertIsInstance(child_A_3, NodeFragment)
        self.assertEqual(len(child_A_3.children), 1)
        self.assertEqual(child_A_3.children[0], NodeWord('re'))

        child_A_4 = child_A.children[3]
        self.assertIsInstance(child_A_4, NodeFragment)
        self.assertEqual(len(child_A_4.children), 1)
        self.assertEqual(child_A_4.children[0], NodeWord('lo'))

        child_B = verse.children[1]
        self.assertEqual(child_B, NodeWord('e'))

        child_C = verse.children[2]
        self.assertIsInstance(child_C, NodeManualWord)
        self.assertEqual(len(child_C.children), 2)
        self.assertEqual(child_C.children[0], NodeWord('a'))
        self.assertEqual(child_C.children[1], NodeWord('zul'))

        child_D = verse.children[3]
        self.assertEqual(child_D, NodeWord('são'))

        child_E = verse.children[4]
        self.assertIsInstance(child_E, NodeUnstressedWord)
        self.assertEqual(child_E.children[0], NodeWord('minhas'))

        child_F = verse.children[5]
        self.assertIsInstance(child_F, NodeUntiedSubwords)
        self.assertEqual(len(child_F.children), 2)
        self.assertEqual(child_F.children[0], NodeWord('sa'))
        self.assertEqual(child_F.children[1], NodeWord('udades'))


    def test_fragment_with_tied_words_and_untied_words_with_manual_word(self):
        input   = '|la|ran|ja| * e / [a|zul]'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse   = parser.parse()

        self.assertEqual(len(verse.children), 1)

        child_A = verse.children[0]
        self.assertIsInstance(child_A, NodeUntiedWords)
        self.assertEqual(len(child_A.children), 2)
        
        child_A_1 = child_A.children[0]
        self.assertIsInstance(child_A_1, NodeTiedWords)
        self.assertEqual(len(child_A_1.children), 2)

        child_A_1_1 = child_A_1.children[0]
        self.assertIsInstance(child_A_1_1, NodeFragments)
        self.assertEqual(len(child_A_1_1.children), 3)
        child_A_1_1_1 = child_A_1_1.children[0]
        self.assertIsInstance(child_A_1_1_1, NodeFragment)
        self.assertEqual(child_A_1_1_1.children[0], NodeWord('la'))
        child_A_1_1_2 = child_A_1_1.children[1]
        self.assertIsInstance(child_A_1_1_2, NodeFragment)
        self.assertEqual(child_A_1_1_2.children[0], NodeWord('ran'))
        child_A_1_1_3 = child_A_1_1.children[2]
        self.assertIsInstance(child_A_1_1_3, NodeFragment)
        self.assertEqual(child_A_1_1_3.children[0], NodeWord('ja'))

        child_A_1_2 = child_A_1.children[1]
        self.assertEqual(child_A_1_2, NodeWord('e'))

        child_A_2 = child_A.children[1]
        self.assertIsInstance(child_A_2, NodeManualWord)
        self.assertEqual(len(child_A_2.children), 2)
        self.assertEqual(child_A_2.children[0], NodeWord('a'))
        self.assertEqual(child_A_2.children[1], NodeWord('zul'))


    def test_prefix_coda(self):
        input   = '|+mai|s_um|+di|--a|'
        scanner = VerseScanner(input)
        parser  = VerseParser(scanner)
        verse   = parser.parse()

        self.assertEqual(len(verse.children), 1)

        child_A = verse.children[0]
        self.assertIsInstance(child_A, NodeFragments)
        self.assertEqual(len(child_A.children), 4)

        child_A_1 = child_A.children[0]
        self.assertIsInstance(child_A_1, NodeStressedFragment)
        self.assertEqual(len(child_A_1.children), 1)

        child_A_1_1 = child_A_1.children[0]
        self.assertIsInstance(child_A_1_1, NodeFragment)
        self.assertEqual(len(child_A_1_1.children), 1)
        self.assertEqual(child_A_1_1.children[0], NodeWord('mai'))

        child_A_2 = child_A.children[1]
        self.assertIsInstance(child_A_2, NodeJoinedFragments)
        self.assertEqual(len(child_A_2.children), 2)
        self.assertEqual(child_A_2.children[0], NodeWord('s'))
        self.assertEqual(child_A_2.children[1], NodeWord('um'))

        child_A_3 = child_A.children[2]
        self.assertIsInstance(child_A_3, NodeStressedFragment)
        self.assertEqual(len(child_A_3.children), 1)

        child_A_3_1 = child_A_3.children[0]
        self.assertIsInstance(child_A_3_1, NodeFragment)
        self.assertEqual(len(child_A_3_1.children), 1)
        self.assertEqual(child_A_3_1.children[0], NodeWord('di'))

        child_A_4 = child_A.children[3]
        self.assertIsInstance(child_A_4, NodeUncountedFragment)
        self.assertEqual(len(child_A_4.children), 1)
        self.assertEqual(child_A_4.children[0], NodeWord('a'))
