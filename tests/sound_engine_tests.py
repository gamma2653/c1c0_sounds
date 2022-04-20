import sys
import unittest
sys.path.insert(0, "..")

from c1c0_sounds.sound_engine import _interpret_chirp_types
from c1c0_sounds.utils import Trie, TrieNode

class SoundEngineTests(unittest.TestCase):
    def test_interpret_chirp_types(self):
        chirp_types = [
            ('9S_1L_1S0.wav', ('9S', '1L', '1S', '0')),
            ('1L_1S0.wav', ('1L', '1S', '0')),
            ('1L_1S1.wav', ('1L', '1S', '1')),
            ('1L_2S0.wav', ('1L', '2S', '0')),
            ('1L0.wav', ('1L', '0')),
        ]
        for chirp_name, expected in chirp_types:
            result = _interpret_chirp_types(chirp_name)
            self.assertEqual(result, expected)
    
    def test_trie(self):
        trie_tests = [
            ('', 0),
            ('a', 1),
            ('...-.-.---', 2),
            ('...-.-.---.-', 3),
            ('...-.-.---.', 4),
            ('...-.-', 5),
            ('.....-.-.', 6),
        ]
        trie = Trie()
        for trie_test in trie_tests:
            trie.insert(*trie_test)
        for trie_test in trie_tests:
            print(trie.traverse(trie_test[0]))

            
if __name__ == "__main__":
    unittest.main()
