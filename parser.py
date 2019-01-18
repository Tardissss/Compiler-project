from lexer import *
from combinators import *
from ast import *

# Basic parsers
def keyword(kw):
    return Reserved(kw, RESERVED)

# change str to array
def str2array(input):
    array1 = input.replace('[','').replace(']','').split(',')
    array2 = []
    for i in array1:
        array2.append(int(i))
    return array2

# def str2index(input):
#     array = env[input.split('[')[0]]
#     index = input.split('[').split(']')[0]
    
#     print array, index
#     return array[index]

# Basic types
num = Tag(INT) ^ (lambda i: int(i))
array = Tag(ARRAY) ^ str2array
# index = Tag(INDEX) ^ str2index
id = Tag(ID)
string = Tag(STRING) ^ (lambda i: str(i).replace("\"",""))

# Top level parser
def foo_parse(tokens):
    ast = parser()(tokens, 0)
    return ast

def parser():
    return Phrase(stmt_list())    

# Statements
def stmt_list():
    separator = keyword(';') ^ (lambda x: lambda l, r: CompoundStatement(l, r))
    return Exp(stmt(), separator)

# Different statements
def stmt():
    return index_stmt_8()  | \
           index_stmt_9()  | \
           index_stmt_4()  | \
           index_stmt_5()  | \
           index_stmt_6()  | \
           index_stmt_7()  | \
           length_stmt()   | \
           index_stmt_1()  | \
           index_stmt_2()  | \
           assign_stmt() | \
           bool_stmt() | \
           if_stmt()     | \
           while_stmt()  | \
           append_stmt() | \
           read_stmt()   | \
           print_stmt()

# Basic assign stmts for simple id variable
def assign_stmt():
    def process(parsed):
        ((name, _), exp) = parsed
        return AssignStatement(name, exp)
    return id + keyword(':=') + aexp() ^ process

# Basic bool stmts
def bool_stmt():
    def process(parsed):
        ((name, _), exp) = parsed
        return AssignStatement(name, exp)
    return id + keyword(':=') + bexp() ^ process

# If stmts
def if_stmt():
    def process(parsed):
        (((((_, condition), _), true_stmt), false_parsed), _) = parsed
        if false_parsed:
            (_, false_stmt) = false_parsed
        else:
            false_stmt = None
        return IfStatement(condition, true_stmt, false_stmt)
    return keyword('if') + bexp() + \
           keyword('then') + Lazy(stmt_list) + \
           Opt(keyword('else') + Lazy(stmt_list)) + \
           keyword('end') ^ process

# While stmts
def while_stmt():
    def process(parsed):
        ((((_, condition), _), body), _) = parsed
        return WhileStatement(condition, body)
    return keyword('while') + bexp() + \
           keyword('do') + Lazy(stmt_list) + \
           keyword('end') ^ process

# Print stmts
def print_stmt():
    def process(parsed):
        (_, exp) = parsed
        return PrintStatement(exp)
    return keyword('print') + aexp() ^ process

# Readin stmts
def read_stmt():
    def process(parsed):
        ((_, name1), name2) = parsed
        return ReadStatement(name1, name2)
    return keyword('readin') + string + id ^ process

# Apeend stmts
def append_stmt():
    def process(parsed):
        ((_, name), exp) = parsed
        return AppendStatement(name, exp)
    return keyword('append') + id + aexp() ^ process


# The following definations are different index assignments.
# In ordder to be simple to understand, we write a simple example for each stmt 

# y := x[1]
def index_stmt_1():
    def process(parsed):
        (((name1, _), name2), exp) = parsed
        return IndexStatement_1(name1, name2, exp)
    return id + keyword(':=') + id + aexp() ^ process

# y := x[a]
def index_stmt_4():
    def process(parsed):
        (((((name1, _), name2), _), exp),_) = parsed
        return IndexStatement_4(name1, name2, exp)
    return id + keyword(':=') + id + keyword('[') + aexp() + keyword(']') ^ process

# x[a] := 1
def index_stmt_5():
    def process(parsed):
        (((((name, _), exp1), _), _), exp2) = parsed
        return IndexStatement_5(name, exp1, exp2)
    return id + keyword('[') + aexp() + keyword(']') + keyword(':=') + aexp() ^ process

# list[1] := list[2];
def index_stmt_6():
    def process(parsed):
        ((((name1, exp1), _), name2), exp2) = parsed
        return IndexStatement_6(name1, exp1, name2, exp2)
    return id + aexp() + keyword(':=') + id + aexp() ^ process

# list[2] := list[a];
def index_stmt_7():
    def process(parsed):
        ((((((name1, exp1), _), name2),_), exp2), _) = parsed
        return IndexStatement_7(name1, exp, name2, exp2)
    return id + aexp() + keyword(':=') + id + keyword('[') + aexp() + keyword(']') ^ process

# list[a] := list[1];
def index_stmt_8():
    def process(parsed):
        ((((((name1, _), exp1), _),_), name2), exp2) = parsed
        return IndexStatement_8(name1, exp1, name2, exp2)
    return id + keyword('[') + aexp() + keyword(']') + keyword(':=') + id + aexp() ^ process

# list[a] := list[a];
def index_stmt_9():
    def process(parsed):
        ((((((((name1, _), exp1), _),_), name2), _), exp2), _) = parsed
        return IndexStatement_9(name1, exp1, name2, exp2)
    return id + keyword('[') + aexp() + keyword(']') + keyword(':=') + id + keyword('[') + aexp() + keyword(']') ^ process

# y[1] := x
def index_stmt_2():
    def process(parsed):
        (((name, exp1), _), exp2) = parsed
        return IndexStatement_2(name, exp1, exp2)
    return id + aexp() + keyword(':=') + aexp() ^ process

# y[1] := 1
# def index_stmt_3():
#     def process(parsed):
#         (((name, exp1), _), exp2) = parsed
#         return IndexStatement_3(name, exp1, exp2)
#     return id + aexp() + keyword(':=') + aexp() ^ process

# length attr for array
def length_stmt():
    def process(parsed):
        (((name1, _), name2),_) = parsed
        return LengthStatement(name1, name2)
    return id + keyword(':=') + id + keyword('.l') ^ process

# Boolean expressions
def bexp():
    return precedence(bexp_term(),
                      bexp_precedence_levels,
                      process_logic)

def bexp_term():
    return bexp_not()   | \
           bexp_relop2() | \
           bexp_relop3() | \
           bexp_relop4() | \
           bexp_relop5() | \
           bexp_relop1() | \
           bexp_group()

def bexp_not():
    return keyword('not') + Lazy(bexp_term) ^ (lambda parsed: NotBexp(parsed[1]))

# Basci bool stmt
def bexp_relop1():
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return aexp() + any_operator_in_list(relops) + aexp() ^ process_relop

# The following definations are different bool comparetions.
# In ordder to be simple to understand, we write a simple example for each stmt 

# list[a] < list[b]
def bexp_relop2():
    def process_relop2(parsed):
        ((((((((name1, _), exp1), _), op), name2), _), exp2), _) = parsed
        return RelopBexp2(name1, exp1, op, name2, exp2)
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return id + keyword('[') + aexp() + keyword(']') + any_operator_in_list(relops) + id + keyword('[') + aexp() + keyword(']') ^ process_relop2

# list[a] < list[1]
def bexp_relop3():
    def process_relop2(parsed):
        ((((((name1, _), exp1), _), op), name2), exp2) = parsed
        return RelopBexp2(name1, exp1, op, name2, exp2)
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return id + keyword('[') + aexp() + keyword(']') + any_operator_in_list(relops) + id + aexp() ^ process_relop2

# list[1] < list[b]
def bexp_relop4():
    def process_relop2(parsed):
        ((((((name1, exp1), op), name2), _), exp2), _) = parsed
        return RelopBexp2(name1, exp1, op, name2, exp2)
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return id + aexp() + any_operator_in_list(relops) + id + keyword('[') + aexp() + keyword(']') ^ process_relop2

# list[1] < list[b]
def bexp_relop5():
    def process_relop2(parsed):
        ((((name1, exp1), op), name2), exp2) = parsed
        return RelopBexp2(name1, exp1, op, name2, exp2)
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return id + aexp() + any_operator_in_list(relops) + id + aexp() ^ process_relop2


def bexp_group():
    return keyword('(') + Lazy(bexp) + keyword(')') ^ process_group

# Arithmetic expressions
def aexp():
    return precedence(aexp_term(),
                      aexp_precedence_levels,
                      process_binop)

def aexp_term():
    return aexp_value() | aexp_group()

def aexp_group():
    return keyword('(') + Lazy(aexp) + keyword(')') ^ process_group

# Get the value of each arithmatic expressiohn           
def aexp_value():
    return (num ^ (lambda i: IntAexp(i))) | \
           (array ^ (lambda i: ArrayAexp(i))) | \
           (string ^ (lambda i: StrAexp(i))) | \
           (id  ^ (lambda v: VarAexp(v)))

# An IMP-specific combinator for binary operator expressions (aexp and bexp)
def precedence(value_parser, precedence_levels, combine):
    def op_parser(precedence_level):
        return any_operator_in_list(precedence_level) ^ combine
    parser = value_parser * op_parser(precedence_levels[0])
    for precedence_level in precedence_levels[1:]:
        parser = parser * op_parser(precedence_level)
    return parser

# Miscellaneous functions for binary and relational operators
def process_binop(op):
    return lambda l, r: BinopAexp(op, l, r)

def process_relop(parsed):
    ((left, op), right) = parsed
    return RelopBexp(op, left, right)

def process_logic(op):
    if op == 'and':
        return lambda l, r: AndBexp(l, r)
    elif op == 'or':
        return lambda l, r: OrBexp(l, r)
    else:
        raise RuntimeError('unknown logic operator: ' + op)

def process_group(parsed):
    ((_, p), _) = parsed
    return p

def any_operator_in_list(ops):
    op_parsers = [keyword(op) for op in ops]
    parser = reduce(lambda l, r: l | r, op_parsers)
    return parser

# Operator keywords and precedence levels
aexp_precedence_levels = [
    ['*', '/'],
    ['+', '-'],
]

bexp_precedence_levels = [
    ['and'],
    ['or'],
]
