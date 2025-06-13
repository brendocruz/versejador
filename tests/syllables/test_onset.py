from unittest import TestCase
from src.words.splitter import WordSplitter



class TestWordsWithOnset(TestCase):

    def test_cluster_with_rl(self):
        splitter = WordSplitter()

        text = 'abraço'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'a', ''], word[0].parts())
        self.assertListEqual(['', 'br', 'a', ''], word[1].parts())
        self.assertListEqual(['', 'ç',  'o', ''], word[2].parts())

        text = 'prato'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'pr', 'a', ''], word[0].parts())
        self.assertListEqual(['', 't',  'o', ''], word[1].parts())

        text = 'tecla'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 't',  'e', ''], word[0].parts())
        self.assertListEqual(['', 'cl', 'a', ''], word[1].parts())




    def test_dipragh(self):
        splitter = WordSplitter()

        text = 'tchéquia'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'tch', 'é', ''], word[0].parts())
        self.assertListEqual(['', 'qu',  'i', ''], word[1].parts())
        self.assertListEqual(['', '',    'a', ''], word[2].parts())

        text = 'velho'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'v',  'e', ''], word[0].parts())
        self.assertListEqual(['', 'lh', 'o', ''], word[1].parts())

        text = 'chato'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'ch', 'a', ''], word[0].parts())
        self.assertListEqual(['', 't',  'o', ''], word[1].parts())

        text = 'carro'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'c',  'a', ''], word[0].parts())
        self.assertListEqual(['', 'rr', 'o', ''], word[1].parts())

        text = 'assado'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'a', ''], word[0].parts())
        self.assertListEqual(['', 'ss', 'a', ''], word[1].parts())
        self.assertListEqual(['', 'd',  'o', ''], word[2].parts())

        text = 'nhonho'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'nh', 'o', ''], word[0].parts())
        self.assertListEqual(['', 'nh', 'o', ''], word[1].parts())

        text = 'guerra'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'gu', 'e', ''], word[0].parts())
        self.assertListEqual(['', 'rr', 'a', ''], word[1].parts())

        text = 'leque'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'l',  'e', ''], word[0].parts())
        self.assertListEqual(['', 'qu', 'e', ''], word[1].parts())

        text = 'exceto'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'e', ''], word[0].parts())
        self.assertListEqual(['', 'xc', 'e', ''], word[1].parts())
        self.assertListEqual(['', 't',  'o', ''], word[2].parts())

        text = 'descendente'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'd',  'e',  ''], word[0].parts())
        self.assertListEqual(['', 'sc', 'e', 'n'], word[1].parts())
        self.assertListEqual(['', 'd',  'e', 'n'], word[2].parts())
        self.assertListEqual(['', 't',  'e',  ''], word[3].parts())

        text = 'exsurgir'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'e',  ''], word[0].parts())
        self.assertListEqual(['', 'xs', 'u', 'r'], word[1].parts())
        self.assertListEqual(['', 'g',  'i', 'r'], word[2].parts())

        text = 'nasço'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'n',  'a', ''], word[0].parts())
        self.assertListEqual(['', 'sç', 'o', ''], word[1].parts())




    def test_cluster_separable_off(self):
        splitter = WordSplitter()

        text = 'friccionar'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'fr', 'i',  ''], word[0].parts())
        self.assertListEqual(['', 'cc', 'i',  ''], word[1].parts())
        self.assertListEqual(['', '',   'o',  ''], word[2].parts())
        self.assertListEqual(['', 'n',  'a', 'r'], word[3].parts())

        text = 'convicção'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'c',  'o',  'n'], word[0].parts())
        self.assertListEqual(['', 'v',  'i',   ''], word[1].parts())
        self.assertListEqual(['', 'cç', 'ão',  ''], word[2].parts())

        text = 'compacto'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'c',  'o', 'm'], word[0].parts())
        self.assertListEqual(['', 'p',  'a',  ''], word[1].parts())
        self.assertListEqual(['', 'ct', 'o',  ''], word[2].parts())

        text = 'núpcias'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'n',  'ú',  ''], word[0].parts())
        self.assertListEqual(['', 'pc', 'i',  ''], word[1].parts())
        self.assertListEqual(['', '',   'a', 's'], word[2].parts())

        text = 'erupção'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'e',  ''], word[0].parts())
        self.assertListEqual(['', 'r',  'u',  ''], word[1].parts())
        self.assertListEqual(['', 'pç', 'ão', ''], word[2].parts())

        text = 'eucalipto'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',   'eu', ''], word[0].parts())
        self.assertListEqual(['', 'c',  'a',  ''], word[1].parts())
        self.assertListEqual(['', 'l',  'i',  ''], word[2].parts())
        self.assertListEqual(['', 'pt', 'o',  ''], word[3].parts())

        text = 'observar'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'o',  ''], word[0].parts())
        self.assertListEqual(['', 'bs', 'e', 'r'], word[1].parts())
        self.assertListEqual(['', 'v',  'a', 'r'], word[2].parts())

        text = 'admitir'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'a',  ''], word[0].parts())
        self.assertListEqual(['', 'dm', 'i',  ''], word[1].parts())
        self.assertListEqual(['', 't',  'i', 'r'], word[2].parts())

        text = 'advogado'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',   'a', ''], word[0].parts())
        self.assertListEqual(['', 'dv', 'o', ''], word[1].parts())
        self.assertListEqual(['', 'g',  'a', ''], word[2].parts())
        self.assertListEqual(['', 'd',  'o', ''], word[3].parts())

        text = 'ritmo'
        word = splitter.run(text)
        self.assertEqual(2, len(word))
        self.assertListEqual(['', 'r',  'i', ''], word[0].parts())
        self.assertListEqual(['', 'tm', 'o', ''], word[1].parts())

        text = 'ignorar'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'i',  ''], word[0].parts())
        self.assertListEqual(['', 'gn', 'o',  ''], word[1].parts())
        self.assertListEqual(['', 'r',  'a', 'r'], word[2].parts())

        text = 'óbvio'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', '',   'ó', ''], word[0].parts())
        self.assertListEqual(['', 'bv', 'i', ''], word[1].parts())
        self.assertListEqual(['', '',   'o', ''], word[2].parts())

        text = 'psiquiatra'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'ps', 'i', ''], word[0].parts())
        self.assertListEqual(['', 'qu', 'i', ''], word[1].parts())
        self.assertListEqual(['', '',   'a', ''], word[2].parts())
        self.assertListEqual(['', 'tr', 'a', ''], word[3].parts())

        text = 'submarino'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 's',  'u', ''], word[0].parts())
        self.assertListEqual(['', 'bm', 'a', ''], word[1].parts())
        self.assertListEqual(['', 'r',  'i', ''], word[2].parts())
        self.assertListEqual(['', 'n',  'o', ''], word[3].parts())

        text = 'tecnologia'
        word = splitter.run(text)
        self.assertEqual(5, len(word))
        self.assertListEqual(['', 't',  'e', ''], word[0].parts())
        self.assertListEqual(['', 'cn', 'o', ''], word[1].parts())
        self.assertListEqual(['', 'l',  'o', ''], word[2].parts())
        self.assertListEqual(['', 'g',  'i', ''], word[3].parts())
        self.assertListEqual(['', '',   'a', ''], word[4].parts())

        text = 'mnemônico'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'mn', 'e', ''], word[0].parts())
        self.assertListEqual(['', 'm',  'ô', ''], word[1].parts())
        self.assertListEqual(['', 'n',  'i', ''], word[2].parts())
        self.assertListEqual(['', 'c',  'o', ''], word[3].parts())




    def test_cluster_separable_on(self):
        splitter = WordSplitter(split_onset_cluster=True)

        text = 'friccionar'
        word = splitter.run(text)
        self.assertEqual(5, len(word))
        self.assertListEqual(['', 'fr', 'i',  ''], word[0].parts())
        self.assertListEqual(['', 'c',  '',   ''], word[1].parts())
        self.assertListEqual(['', 'c',  'i',  ''], word[2].parts())
        self.assertListEqual(['', '',   'o',  ''], word[3].parts())
        self.assertListEqual(['', 'n',  'a', 'r'], word[4].parts())

        text = 'convicção'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'c',  'o',  'n'], word[0].parts())
        self.assertListEqual(['', 'v',  'i',   ''], word[1].parts())
        self.assertListEqual(['', 'c',  '',    ''], word[2].parts())
        self.assertListEqual(['', 'ç',  'ão',  ''], word[3].parts())

        text = 'compacto'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'c', 'o', 'm'], word[0].parts())
        self.assertListEqual(['', 'p', 'a',  ''], word[1].parts())
        self.assertListEqual(['', 'c', '',   ''], word[2].parts())
        self.assertListEqual(['', 't', 'o',  ''], word[3].parts())

        text = 'núpcias'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', 'n', 'ú',  ''], word[0].parts())
        self.assertListEqual(['', 'p', '',   ''], word[1].parts())
        self.assertListEqual(['', 'c', 'i',  ''], word[2].parts())
        self.assertListEqual(['', '',  'a', 's'], word[3].parts())

        text = 'erupção'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'e',  ''], word[0].parts())
        self.assertListEqual(['', 'r', 'u',  ''], word[1].parts())
        self.assertListEqual(['', 'p', '',   ''], word[2].parts())
        self.assertListEqual(['', 'ç', 'ão', ''], word[3].parts())

        text = 'eucalipto'
        word = splitter.run(text)
        self.assertEqual(5, len(word))
        self.assertListEqual(['', '',  'eu', ''], word[0].parts())
        self.assertListEqual(['', 'c', 'a',  ''], word[1].parts())
        self.assertListEqual(['', 'l', 'i',  ''], word[2].parts())
        self.assertListEqual(['', 'p', '',   ''], word[3].parts())
        self.assertListEqual(['', 't', 'o',  ''], word[4].parts())

        text = 'observar'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'o',  ''], word[0].parts())
        self.assertListEqual(['', 'b', '',   ''], word[1].parts())
        self.assertListEqual(['', 's', 'e', 'r'], word[2].parts())
        self.assertListEqual(['', 'v', 'a', 'r'], word[3].parts())

        text = 'admitir'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'a',  ''], word[0].parts())
        self.assertListEqual(['', 'd', '',   ''], word[1].parts())
        self.assertListEqual(['', 'm', 'i',  ''], word[2].parts())
        self.assertListEqual(['', 't', 'i', 'r'], word[3].parts())

        text = 'advogado'
        word = splitter.run(text)
        self.assertEqual(5, len(word))
        self.assertListEqual(['', '',  'a', ''], word[0].parts())
        self.assertListEqual(['', 'd', '',  ''], word[1].parts())
        self.assertListEqual(['', 'v', 'o', ''], word[2].parts())
        self.assertListEqual(['', 'g', 'a', ''], word[3].parts())
        self.assertListEqual(['', 'd', 'o', ''], word[4].parts())

        text = 'ritmo'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'r', 'i', ''], word[0].parts())
        self.assertListEqual(['', 't', '',  ''], word[1].parts())
        self.assertListEqual(['', 'm', 'o', ''], word[2].parts())

        text = 'ignorar'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'i',  ''], word[0].parts())
        self.assertListEqual(['', 'g', '',   ''], word[1].parts())
        self.assertListEqual(['', 'n', 'o',  ''], word[2].parts())
        self.assertListEqual(['', 'r', 'a', 'r'], word[3].parts())

        text = 'óbvio'
        word = splitter.run(text)
        self.assertEqual(4, len(word))
        self.assertListEqual(['', '',  'ó', ''], word[0].parts())
        self.assertListEqual(['', 'b', '',  ''], word[1].parts())
        self.assertListEqual(['', 'v', 'i', ''], word[2].parts())
        self.assertListEqual(['', '',  'o', ''], word[3].parts())

        text = 'psiquiatra'
        word = splitter.run(text)
        self.assertEqual(5, len(word))
        self.assertListEqual(['', 'p',  '',  ''], word[0].parts())
        self.assertListEqual(['', 's',  'i', ''], word[1].parts())
        self.assertListEqual(['', 'qu', 'i', ''], word[2].parts())
        self.assertListEqual(['', '',   'a', ''], word[3].parts())
        self.assertListEqual(['', 'tr', 'a', ''], word[4].parts())

        text = 'submarino'
        word = splitter.run(text)
        self.assertEqual(5, len(word))
        self.assertListEqual(['', 's', 'u', ''], word[0].parts())
        self.assertListEqual(['', 'b', '',  ''], word[1].parts())
        self.assertListEqual(['', 'm', 'a', ''], word[2].parts())
        self.assertListEqual(['', 'r', 'i', ''], word[3].parts())
        self.assertListEqual(['', 'n', 'o', ''], word[4].parts())

        text = 'tecnologia'
        word = splitter.run(text)
        self.assertEqual(6, len(word))
        self.assertListEqual(['', 't', 'e', ''], word[0].parts())
        self.assertListEqual(['', 'c', '',  ''], word[1].parts())
        self.assertListEqual(['', 'n', 'o', ''], word[2].parts())
        self.assertListEqual(['', 'l', 'o', ''], word[3].parts())
        self.assertListEqual(['', 'g', 'i', ''], word[4].parts())
        self.assertListEqual(['', '',  'a', ''], word[5].parts())

        text = 'mnemônico'
        word = splitter.run(text)
        self.assertEqual(5, len(word))
        self.assertListEqual(['', 'm', '',  ''], word[0].parts())
        self.assertListEqual(['', 'n', 'e', ''], word[1].parts())
        self.assertListEqual(['', 'm', 'ô', ''], word[2].parts())
        self.assertListEqual(['', 'n', 'i', ''], word[3].parts())
        self.assertListEqual(['', 'c', 'o', ''], word[4].parts())



    def test_only_onset(self):
        splitter = WordSplitter()

        text = 's'
        word = splitter.run(text)
        self.assertEqual(1, len(word))
        self.assertListEqual(['', 's',   '',  ''], word[0].parts())



    def test_special_symbol(self):
        splitter = WordSplitter()

        text = 'minh\'alma'
        word = splitter.run(text)
        self.assertEqual(3, len(word))
        self.assertListEqual(['', 'm',   'i',  ''], word[0].parts())
        self.assertListEqual(['', "nh'", 'a', 'l'], word[1].parts())
        self.assertListEqual(['', 'm',   'a',  ''], word[2].parts())
