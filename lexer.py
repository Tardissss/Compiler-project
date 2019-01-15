from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Var
        self.lexer.add('VAR', r'var')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')

        self.lexer.add('LESS_EQUAL', r'<=')
        self.lexer.add('GREATER_EQUAL', r'>=')
        self.lexer.add('GREATER', r'>')
        self.lexer.add('LESS', r'<')
        self.lexer.add('NOT_EQUAL', r'!=')
        self.lexer.add('EQUAL', r'=')        

        # Assign
        self.lexer.add('ASSIGN', r'\:=')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Name
        self.lexer.add('NAME', r'([_A-Za-z])*')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
