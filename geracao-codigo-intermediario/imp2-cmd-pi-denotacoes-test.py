import unittest
import tatsu
from impiler import Impiler

class TestImpToPiIR(unittest.TestCase):
    def setUp(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        self.parser = tatsu.compile(imp_grammar)

    def __test_parse(self, file_name, ast):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        pi_ast = self.parser.parse(source, semantics=Impiler())
        self.assertEqual(str(pi_ast), ast)

    def test_cmd_parse0(self):
        '''
        Escreva a representação em Pi IR do programa Imp em examples/cmd-test0.imp2.
        '''
        pi_ast = ""
        self.__test_parse('examples/cmd-test0.imp2', pi_ast)

    def test_cmd_parse1(self):
        '''
        Escreva a representação em Pi IR do programa Imp em examples/cmd-test1.imp2.
        '''
        pi_ast = ""
        self.__test_parse('examples/cmd-test1.imp2', pi_ast)
        
if __name__ == '__main__':
    unittest.main()
