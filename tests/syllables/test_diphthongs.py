from unittest import TestCase
from src.words.splitter import WordSplitter



class TestWordsWithDiphthongs(TestCase):

    def test_dipthong_always(self):
        splitter = WordSplitter()

        text = 'coração'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'c', 'o',  ''], word[0].parts())
        self.assertListEqual(['', 'r', 'a',  ''], word[1].parts())
        self.assertListEqual(['', 'ç', 'ão', ''], word[2].parts())

        text = 'ações'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', '',  'a',   ''], word[0].parts())
        self.assertListEqual(['', 'ç', 'õe', 's'], word[1].parts())

        text = 'cãibra'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'c',  'ãi', ''], word[0].parts())
        self.assertListEqual(['', 'br', 'a',  ''], word[1].parts())

        text = 'câimbra'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'c',  'âi', 'm'], word[0].parts())
        self.assertListEqual(['', 'br', 'a',   ''], word[1].parts())

        text = 'mãe'
        word = splitter.run(text)
        self.assertEqual(1, len(word))
        self.assertListEqual(['', 'm', 'ãe', ''], word[0].parts())

        text = 'náilon'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'n', 'ái',  ''], word[0].parts())
        self.assertListEqual(['', 'l', 'o',  'n'], word[1].parts())

        text = 'áureo'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',  'áu', ''], word[0].parts())
        self.assertListEqual(['', 'r', 'e',  ''], word[1].parts())
        self.assertListEqual(['', '',  'o',  ''], word[2].parts())

        text = 'hotéis'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'h', 'o',   ''], word[0].parts())
        self.assertListEqual(['', 't', 'éi', 's'], word[1].parts())

        text = 'contêiner'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'c', 'o',  'n'], word[0].parts())
        self.assertListEqual(['', 't', 'êi',  ''], word[1].parts())
        self.assertListEqual(['', 'n', 'e',  'r'], word[2].parts())

        text = 'chapéu'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'ch', 'a',  ''], word[0].parts())
        self.assertListEqual(['', 'p',  'éu', ''], word[1].parts())

        text = 'nêutron'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'n',  'êu',  ''], word[0].parts())
        self.assertListEqual(['', 'tr', 'o',  'n'], word[1].parts())

        text = 'herói'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'h', 'e',  ''], word[0].parts())
        self.assertListEqual(['', 'r', 'ói', ''], word[1].parts())



    def test_dipthong_always(self):
        splitter = WordSplitter()

        text = 'ao'
        word = splitter.run(text)
        self.assertEqual(1, len(word))
        self.assertListEqual(['', '', 'ao',  ''], word[0].parts())
