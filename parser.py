from rply import ParserGenerator
from ast import Number, Sum, Sub, Mul, Div, Print, Name, Prog, Prog_int


class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'MUL', 'DIV','SUM', 'SUB'],
             precedence=[
                        ('left', ['PLUS', 'MINUS']),
                        ('left', ['MUL', 'DIV'])
                                                    ]
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):

        @self.pg.production('program : expression SEMI_COLON program')
        def program(p):
            return Prog(self.builder, self.module, p[0], p[2]) 

        @self.pg.production('program : expression SEMI_COLON')
        def program_int(p):
            return Prog_int(self.builder, self.module, p[0])        

        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN ')
        def printf(p):
            return Print(self.builder, self.module, self.printf, p[2])
	@self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')

        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)
	    elif operator.gettokentype() == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)



        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
