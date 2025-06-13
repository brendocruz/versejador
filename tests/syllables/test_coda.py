from unittest import TestCase
from src.words.splitter import WordSplitter



class TestWordsWithCoda(TestCase):

    def test_basic(self):
        splitter = WordSplitter()

        text = 'fazer'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'f', 'a',  ''], word[0].parts())
        self.assertListEqual(['', 'z', 'e', 'r'], word[1].parts())

        text = 'certo'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'c', 'e', 'r'], word[0].parts())
        self.assertListEqual(['', 't', 'o',  ''], word[1].parts())

        text = 'sal'
        word = splitter.run(text)
        self.assertEqual(1, len(word))
        self.assertListEqual(['', 's', 'a', 'l'], word[0].parts())

        text = 'ah'
        word = splitter.run(text)
        self.assertEqual(1, len(word))
        self.assertListEqual(['', '', 'a', 'h'], word[0].parts())




    def test_digraph_sometimes(self):
        splitter = WordSplitter()

        text = 'excarcerar'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'e', 'x'], word[0].parts())
        self.assertListEqual(['', 'c', 'a', 'r'], word[1].parts())
        self.assertListEqual(['', 'c', 'e',  ''], word[2].parts())
        self.assertListEqual(['', 'r', 'a', 'r'], word[3].parts())

        text = 'excluir'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'e', 'x'], word[0].parts())
        self.assertListEqual(['', 'cl', 'u',  ''], word[1].parts())
        self.assertListEqual(['', '',   'i', 'r'], word[2].parts())

        text = 'pescar'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'p', 'e', 's'], word[0].parts())
        self.assertListEqual(['', 'c', 'a', 'r'], word[1].parts())

        text = 'consigo'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'c', 'o', 'n'], word[0].parts())
        self.assertListEqual(['', 's', 'i',  ''], word[1].parts())
        self.assertListEqual(['', 'g', 'o',  ''], word[2].parts())




    def test_cluster_middle(self):
        splitter = WordSplitter()

        text = 'transporte'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'tr', 'a', 'ns'], word[0].parts())
        self.assertListEqual(['', 'p',  'o',  'r'], word[1].parts())
        self.assertListEqual(['', 't',  'e',   ''], word[2].parts())




    def test_cluster_end(self):
        splitter = WordSplitter()

        text = 'bíceps'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'b', 'í',   ''], word[0].parts())
        self.assertListEqual(['', 'c', 'e', 'ps'], word[1].parts())

        text = 'hífens'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'h', 'í',   ''], word[0].parts())
        self.assertListEqual(['', 'f', 'e', 'ns'], word[1].parts())
