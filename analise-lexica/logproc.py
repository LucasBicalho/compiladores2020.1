# ------------------------------------------------------------
# Processing a log file
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'TIMESTAMP',
    'PROC',
    'MESSAGE'
] 

def t_TIMESTAMP(t):
    # Regular expression for TIMESTAMP
    r'\d{2}:\d{2}:\d{2}\.\d{6}\s-\d{4}'
    return t

def t_PROC(t):
    # Regular expression for PROC
    r'\t.*\t'
    t.value = t.value[1:len(t.value) - 1]
    return t

def t_MESSAGE(t):
    # Regular expression for MESSAGE
    r'.+\n(((\D)|(\d+\s)).*\n\n?)*'
    t.value = t.value[:len(t.value) - 1]
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


class LogProcLexer:
    data = None
    lexer = None
    def __init__(self):
        fh = open("log", 'r')
        self.data = fh.read()
        fh.close()
        self.lexer = lex.lex()
        self.lexer.input(self.data)

    def collect_messages(self):
        kernel_messages = []
        while True:
            token = self.lexer.token()

            if not token:
              break
            
            if token.type == 'PROC' and token.value == 'kernel':
              message = self.lexer.token()
              kernel_messages.append(message)

        return kernel_messages
        
def print_array(array):
    for token in array:
        if len(token.value) >= 40:
            token.value = token.value[:20] + '  (...)  ' + token.value[-10:]
        print(token)

if __name__ == '__main__':
    print(LogProcLexer().collect_messages())
    
