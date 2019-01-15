from rply import ParserGenerator
from ast import Number, Sum, Sub, Mul, Div, Print, Prog, Prog_int, Less_equal, Greater_equal, Greater, Less, Not_equal, Equal, If_stm


class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'MUL', 'DIV','SUM', 'SUB', 'LESS_EQUAL', 'GREATER_EQUAL',
             'GREATER', 'LESS', 'NOT_EQUAL', 'EQUAL', 'IF', 'ELSE', 'OPEN_BRACE', 'CLOSE_BRACE'],
             precedence=[
                        ('left', ['LESS_EQUAL', 'GREATER_EQUAL','GREATER', 'LESS', 'NOT_EQUAL', 'EQUAL']),
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

        @self.pg.production('expression : IF OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE program CLOSE_BRACE ELSE OPEN_BRACE program CLOSE_BRACE')
        def if_stm(p):
            return If_stm(self.builder, self.module, p[2], p[5], p[9])                 

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

        @self.pg.production('expression : expression LESS_EQUAL expression')
        @self.pg.production('expression : expression GREATER_EQUAL expression')
        @self.pg.production('expression : expression GREATER expression')
        @self.pg.production('expression : expression LESS expression')       
        @self.pg.production('expression : expression NOT_EQUAL expression')
        @self.pg.production('expression : expression EQUAL expression')
        def compare(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'LESS_EQUAL':
                return Less_equal(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'GREATER_EQUAL':
                return Greater_equal(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'GREATER':
                return Greater(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'LESS':
                return Less(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'NOT_EQUAL':
                return Not_equal(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'EQUAL':
                return Equal(self.builder, self.module, left, right)


        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
