from unittest import TestCase
from src.words.splitter import WordSplitter



class TestWordsWithHiatus(TestCase):

    def test_end_with_accented_i(self):
        splitter = WordSplitter()

        text = 'paraíso'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'p', 'a', ''], word[0].parts())
        self.assertListEqual(['', 'r', 'a', ''], word[1].parts())
        self.assertListEqual(['', '',  'í', ''], word[2].parts())
        self.assertListEqual(['', 's', 'o', ''], word[3].parts())

        text = 'cafeína'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'c', 'a',  ''], word[0].parts())
        self.assertListEqual(['', 'f', 'e',  ''], word[1].parts())
        self.assertListEqual(['', '',  'í',  ''], word[2].parts())
        self.assertListEqual(['', 'n', 'a',  ''], word[3].parts())

        text = 'egoísmo'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'e',  ''], word[0].parts())
        self.assertListEqual(['', 'g', 'o',  ''], word[1].parts())
        self.assertListEqual(['', '',  'í', 's'], word[2].parts())
        self.assertListEqual(['', 'm', 'o',  ''], word[3].parts())

        text = 'juízes'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'j', 'u',  ''], word[0].parts())
        self.assertListEqual(['', '',  'í',  ''], word[1].parts())
        self.assertListEqual(['', 'z', 'e', 's'], word[2].parts())




    def test_end_with_accented_u(self):
        splitter = WordSplitter()

        text = 'alaúde'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'a', ''], word[0].parts())
        self.assertListEqual(['', 'l', 'a', ''], word[1].parts())
        self.assertListEqual(['', '',  'ú', ''], word[2].parts())
        self.assertListEqual(['', 'd', 'e', ''], word[3].parts())

        text = 'ciúme'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'c', 'i', ''], word[0].parts())
        self.assertListEqual(['', '',  'ú', ''], word[1].parts())
        self.assertListEqual(['', 'm', 'e', ''], word[2].parts())




    def test_before_consonant_on_word_end(self):
        splitter = WordSplitter()

        text = 'adail'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',  'a',  ''], word[0].parts())
        self.assertListEqual(['', 'd', 'a',  ''], word[1].parts())
        self.assertListEqual(['', '',  'i', 'l'], word[2].parts())

        text = 'ruim'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'r',  'u',  ''], word[0].parts())
        self.assertListEqual(['', '',   'i', 'm'], word[1].parts())

        text = 'juiz'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'j',  'u',  ''], word[0].parts())
        self.assertListEqual(['', '',   'i', 'z'], word[1].parts())

        text = 'influir'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'i', 'n'], word[0].parts())
        self.assertListEqual(['', 'fl', 'u',  ''], word[1].parts())
        self.assertListEqual(['', '',   'i', 'r'], word[2].parts())




    def test_before_cluster(self):
        splitter = WordSplitter()

        text = 'rainha'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'r',  'a', ''], word[0].parts())
        self.assertListEqual(['', '',   'i', ''], word[1].parts())
        self.assertListEqual(['', 'nh', 'a', ''], word[2].parts())

        text = 'coimbra'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'c',  'o',  ''], word[0].parts())
        self.assertListEqual(['', '',   'i', 'm'], word[1].parts())
        self.assertListEqual(['', 'br', 'a',  ''], word[2].parts())

        text = 'ainda'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',  'a',  ''], word[0].parts())
        self.assertListEqual(['', '',  'i', 'n'], word[1].parts())
        self.assertListEqual(['', 'd', 'a',  ''], word[2].parts())

        text = 'triunfo'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'tr', 'i',  ''], word[0].parts())
        self.assertListEqual(['', '',   'u', 'n'], word[1].parts())
        self.assertListEqual(['', 'f',  'o',  ''], word[2].parts())

        text = 'influirmos'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',   'i', 'n'], word[0].parts())
        self.assertListEqual(['', 'fl', 'u',  ''], word[1].parts())
        self.assertListEqual(['', '',   'i', 'r'], word[2].parts())
        self.assertListEqual(['', 'm',  'o', 's'], word[3].parts())



    def test_hiatus_always(self):
        splitter = WordSplitter()

        text = 'realizar'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'r', 'e',  ''], word[0].parts())
        self.assertListEqual(['', '',  'a',  ''], word[1].parts())
        self.assertListEqual(['', 'l', 'i',  ''], word[2].parts())
        self.assertListEqual(['', 'z', 'a', 'r'], word[3].parts())

        text = 'vídeo'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'v', 'í', ''], word[0].parts())
        self.assertListEqual(['', 'd', 'e', ''], word[1].parts())
        self.assertListEqual(['', '',  'o', ''], word[2].parts())

        text = 'calúnia'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'c', 'a', ''], word[0].parts())
        self.assertListEqual(['', 'l', 'ú', ''], word[1].parts())
        self.assertListEqual(['', 'n', 'i', ''], word[2].parts())
        self.assertListEqual(['', '',  'a', ''], word[3].parts())

        text = 'espécie'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'e', 's'], word[0].parts())
        self.assertListEqual(['', 'p', 'é',  ''], word[1].parts())
        self.assertListEqual(['', 'c', 'i',  ''], word[2].parts())
        self.assertListEqual(['', '',  'e',  ''], word[3].parts())

        text = 'ocioso'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'o', ''], word[0].parts())
        self.assertListEqual(['', 'c', 'i', ''], word[1].parts())
        self.assertListEqual(['', '',  'o', ''], word[2].parts())
        self.assertListEqual(['', 's', 'o', ''], word[3].parts())

        text = 'mágoa'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'm', 'á', ''], word[0].parts())
        self.assertListEqual(['', 'g', 'o', ''], word[1].parts())
        self.assertListEqual(['', '',  'a', ''], word[2].parts())

        text = 'mútua'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'm', 'ú', ''], word[0].parts())
        self.assertListEqual(['', 't', 'u', ''], word[1].parts())
        self.assertListEqual(['', '',  'a', ''], word[2].parts())

        text = 'cruel'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'cr', 'u',  ''], word[0].parts())
        self.assertListEqual(['', '',   'e', 'l'], word[1].parts())

        text = 'vácuo'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'v', 'á', ''], word[0].parts())
        self.assertListEqual(['', 'c', 'u', ''], word[1].parts())
        self.assertListEqual(['', '',  'o', ''], word[2].parts())


    def test_same_vowel_twice(self):
        splitter = WordSplitter()

        text = 'caatinga'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'c', 'a',  ''], word[0].parts())
        self.assertListEqual(['', '',  'a',  ''], word[1].parts())
        self.assertListEqual(['', 't', 'i', 'n'], word[2].parts())
        self.assertListEqual(['', 'g', 'a',  ''], word[3].parts())
