from unittest import TestCase

from src.words.splitter import WordSplitter



class TestBasicWords(TestCase):

    def test_consonant_start_no_accent(self):
        splitter = WordSplitter()

        text = 'figura'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'f', 'i', ''], word[0].parts())
        self.assertListEqual(['', 'g', 'u', ''], word[1].parts())
        self.assertListEqual(['', 'r', 'a', ''], word[2].parts())

        text = 'banana'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'b', 'a', ''], word[0].parts())
        self.assertListEqual(['', 'n', 'a', ''], word[1].parts())
        self.assertListEqual(['', 'n', 'a', ''], word[2].parts())

        text = 'rude'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'r', 'u', ''], word[0].parts())
        self.assertListEqual(['', 'd', 'e', ''], word[1].parts())

        text = 'vi'
        word = splitter.run(text)
        self.assertEqual(1, len(word))
        self.assertListEqual(['', 'v', 'i', ''], word[0].parts())
    



    def test_vowel_start_no_accent(self):
        splitter = WordSplitter()

        text = 'abacaxi'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'a', ''], word[0].parts())
        self.assertListEqual(['', 'b', 'a', ''], word[1].parts())
        self.assertListEqual(['', 'c', 'a', ''], word[2].parts())
        self.assertListEqual(['', 'x', 'i', ''], word[3].parts())

        text = 'agora'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',  'a', ''], word[0].parts())
        self.assertListEqual(['', 'g', 'o', ''], word[1].parts())
        self.assertListEqual(['', 'r', 'a', ''], word[2].parts())

        text = 'ele'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', '',  'e', ''], word[0].parts())
        self.assertListEqual(['', 'l', 'e', ''], word[1].parts())

        text = 'a'
        word = splitter.run(text)
        self.assertEqual(1, len(word))
        self.assertListEqual(['', '', 'a', ''], word[0].parts())




    def test_consonant_start_and_accent(self):
        splitter = WordSplitter()

        text = 'básico'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'b', 'á', ''], word[0].parts())
        self.assertListEqual(['', 's', 'i', ''], word[1].parts())
        self.assertListEqual(['', 'c', 'o', ''], word[2].parts())

        text = 'maçã'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'm', 'a', ''], word[0].parts())
        self.assertListEqual(['', 'ç', 'ã', ''], word[1].parts())

        text = 'vê'
        word = splitter.run(text)
        self.assertEqual(1, len(word))
        self.assertListEqual(['', 'v', 'ê', ''], word[0].parts())



    def test_vowel_start_and_accent(self):
        splitter = WordSplitter()

        text = 'átomo'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',  'á', ''], word[0].parts())
        self.assertListEqual(['', 't', 'o', ''], word[1].parts())
        self.assertListEqual(['', 'm', 'o', ''], word[2].parts())

        text = 'alô'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', '',  'a', ''], word[0].parts())
        self.assertListEqual(['', 'l', 'ô', ''], word[1].parts())

        text = 'é'
        word = splitter.run(text)
        self.assertEqual(1, len(word))
        self.assertListEqual(['', '', 'é', ''], word[0].parts())



    def test_word_with_hyphen(self):
        splitter = WordSplitter()

        text = 'água-viva'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['',  '',   'á', ''], word[0].parts())
        self.assertListEqual(['',  'gu', 'a', ''], word[1].parts())
        self.assertListEqual(['-', 'v',  'i', ''], word[2].parts())
        self.assertListEqual(['',  'v',  'a', ''], word[3].parts())

        text = 'águas-vivas'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['',  '',   'á',  ''], word[0].parts())
        self.assertListEqual(['',  'gu', 'a', 's'], word[1].parts())
        self.assertListEqual(['-', 'v',  'i',  ''], word[2].parts())
        self.assertListEqual(['',  'v',  'a', 's'], word[3].parts())

        text = 'trens-bala'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['',  'tr', 'e', 'ns'], word[0].parts())
        self.assertListEqual(['-', 'b',  'a',   ''], word[1].parts())
        self.assertListEqual(['',  'l',  'a',   ''], word[2].parts())
