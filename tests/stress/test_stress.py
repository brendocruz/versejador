from unittest import TestCase
from src.words.splitter import WordSplitter
from src.stress.finder import StressFinder



class TestWordsWithOnset(TestCase):

    def test_empty(self):
        finder = StressFinder()
        splitter = WordSplitter()

        word = splitter.run('')
        index = finder.run(word)
        self.assertEqual(-1, index)



    def test_proparoxytones_accent(self):
        finder = StressFinder()
        splitter = WordSplitter()

        word = splitter.run('matemática')
        index = finder.run(word)
        self.assertEqual(2, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('abóbora')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('átomo')
        index = finder.run(word)
        self.assertEqual(0, index)
        self.assertTrue(word[index].has_stress())




    def test_paroxytones_accent(self):
        finder = StressFinder()
        splitter = WordSplitter()

        word = splitter.run('amável')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('dócil')
        index = finder.run(word)
        self.assertEqual(0, index)
        self.assertTrue(word[index].has_stress())




    def test_oxytones_accent(self):
        finder = StressFinder()
        splitter = WordSplitter()

        word = splitter.run('bebê')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('português')
        index = finder.run(word)
        self.assertEqual(2, index)
        self.assertTrue(word[index].has_stress())


    def test_paroxytones_no_accent(self):
        finder = StressFinder()
        splitter = WordSplitter()

        word = splitter.run('gato')
        index = finder.run(word)
        self.assertEqual(0, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('prolixo')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('talarico')
        index = finder.run(word)
        self.assertEqual(2, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('dissimulado')
        index = finder.run(word)
        self.assertEqual(3, index)
        self.assertTrue(word[index].has_stress())


    def test_oxytones_no_accent(self):
        finder = StressFinder()
        splitter = WordSplitter()

        word = splitter.run('hostil')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('amar')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('talismã')
        index = finder.run(word)
        self.assertEqual(2, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('irmãs')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('gratidão')
        index = finder.run(word)
        self.assertEqual(2, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('anciãos')
        index = finder.run(word)
        self.assertEqual(2, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('jejum')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('incomuns')
        index = finder.run(word)
        self.assertEqual(2, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('tatus')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('abacaxi')
        index = finder.run(word)
        self.assertEqual(3, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('caquis')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('farei')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('podeis')
        index = finder.run(word)
        self.assertEqual(1, index)
        self.assertTrue(word[index].has_stress())




    def test_monosyllable_stressed_accent(self):
        finder = StressFinder()
        splitter = WordSplitter()

        word = splitter.run('só')
        index = finder.run(word)
        self.assertEqual(0, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('pé')
        index = finder.run(word)
        self.assertEqual(0, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('dê')
        index = finder.run(word)
        self.assertEqual(0, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('lá')
        index = finder.run(word)
        self.assertEqual(0, index)
        self.assertTrue(word[index].has_stress())




    def test_monosyllable_unstressed(self):
        finder = StressFinder()
        splitter = WordSplitter()

        word = splitter.run('te')
        index = finder.run(word)
        self.assertEqual(-1, index)
        self.assertFalse(word[index].has_stress())

        word = splitter.run('a')
        index = finder.run(word)
        self.assertEqual(-1, index)
        self.assertFalse(word[index].has_stress())

        word = splitter.run('o')
        index = finder.run(word)
        self.assertEqual(-1, index)
        self.assertFalse(word[index].has_stress())

        word = splitter.run('sem')
        index = finder.run(word)
        self.assertEqual(-1, index)
        self.assertFalse(word[index].has_stress())

        word = splitter.run('com')
        index = finder.run(word)
        self.assertEqual(-1, index)
        self.assertFalse(word[index].has_stress())

        word = splitter.run('-ma')
        index = finder.run(word)
        self.assertEqual(-1, index)
        self.assertFalse(word[index].has_stress())



    def test_monosyllable_stressed_no_accent(self):
        finder = StressFinder()
        splitter = WordSplitter()

        word = splitter.run('ver')
        index = finder.run(word)
        self.assertEqual(0, index)
        self.assertTrue(word[index].has_stress())

        word = splitter.run('mão')
        index = finder.run(word)
        self.assertEqual(0, index)
        self.assertTrue(word[index].has_stress())



    
    def test_word_without_nucleus(self):
        finder = StressFinder()
        splitter = WordSplitter(split_onset_cluster=True)

        # Sem núcleo antes de paroxítona.
        text = 'ritmo'
        word = splitter.run(text)
        index = finder.run(word)
        self.assertEqual(index, 0)
        self.assertTrue(word[index].has_stress())

        # Sem núcleo antes de proparoxítona.
        text = 'núpcias'
        word = splitter.run(text)
        index = finder.run(word)
        self.assertEqual(index, 0)
        self.assertTrue(word[index].has_stress())

        # Sem núcleo depois de oxítona.
        text = 'friccionar'
        word = splitter.run(text)
        index = finder.run(word)
        self.assertEqual(index, 4)
        self.assertTrue(word[index].has_stress())

        # Sem núcleo depois de paroxítona.
        text = 'advogado'
        word = splitter.run(text)
        index = finder.run(word)
        self.assertEqual(index, 3)
        self.assertTrue(word[index].has_stress())

        # Sem núcleo depois de proparoxítona.
        text = 'mnemônico'
        word = splitter.run(text)
        index = finder.run(word)
        self.assertEqual(index, 2)
        self.assertTrue(word[index].has_stress())
