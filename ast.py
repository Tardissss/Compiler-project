# Comapre class
class Equality:
    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

# Statement class
class Statement(Equality):
    pass

# Arithmetic expression class
class Aexp(Equality):
    pass

# Bool expression class
class Bexp(Equality):
    pass

# Basic Assignment statement class
class AssignStatement(Statement):
    def __init__(self, name, aexp):
        self.name = name
        self.aexp = aexp

    def __repr__(self):
        return 'AssignStatement(%s, %s)' % (self.name, self.aexp)

    def eval(self, env, c_env):
        value = self.aexp.eval(env, c_env)
        env[self.name] = value

# Compound statement class
class CompoundStatement(Statement):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return 'CompoundStatement(%s, %s)' % (self.first, self.second)

    def eval(self, env, c_env):
        self.first.eval(env, c_env)
        self.second.eval(env, c_env)

# If statement class
class IfStatement(Statement):
    def __init__(self, condition, true_stmt, false_stmt):
        self.condition = condition
        self.true_stmt = true_stmt
        self.false_stmt = false_stmt

    def __repr__(self):
        return 'IfStatement(%s, %s, %s)' % (self.condition, self.true_stmt, self.false_stmt)

    def eval(self, env, c_env):
        condition_value = self.condition.eval(env, c_env)
        if condition_value:
            self.true_stmt.eval(env, c_env)
        else:
            if self.false_stmt:
                self.false_stmt.eval(env, c_env)

# While statement class
class WhileStatement(Statement):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return 'WhileStatement(%s, %s)' % (self.condition, self.body)

    def eval(self, env, c_env):
        condition_value = self.condition.eval(env, c_env)
        # compare = condition_value
        counter = 0
        while condition_value:
            pre = c_env
            self.body.eval(env, c_env)
            condition_value = self.condition.eval(env, c_env)
            curr = c_env
            # print pre, curr
            if curr - pre == 0:
                counter  = counter + 1
            if counter > 1000:
                exit("Error! It seems there is an infinite loop.")

# Print statement class
class PrintStatement(Statement):
    def __init__(self, aexp):
        self.aexp = aexp

    def __repr__(self):
        return 'PrintStatement(%s)' % (self.aexp)

    def eval(self, env, c_env):
        value = self.aexp.eval(env, c_env)
        print value

# Readin statement class
class ReadStatement(Statement):
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def __repr__(self):
        return 'ReadStatement(%s)' % (self.name)

    def eval(self, env, c_env):
        value = input(self.name1.replace('\"','') + '\n' + self.name2 + ':=')
        env[self.name2] = value

# Append statement class
class AppendStatement(Statement):
    def __init__(self, name, aexp):
        self.name = name
        self.aexp = aexp

    def __repr__(self):
        return 'AppendStatement(%s, %s)' % (self.name, self.exp)

    def eval(self, env, c_env):
        value = self.aexp.eval(env, c_env);
        env[self.name].append(value)

# Index assignment statement class: y := x[1]
class IndexStatement_1(Statement):
    def __init__(self, name1, name2, aexp):
        self.name1 = name1
        self.name2 = name2
        self.aexp = aexp

    def __repr__(self):
        return 'IndexStatement_1(%s=%s[%s])' % (self.name1, self.name2, self.aexp)

    def eval(self, env, c_env):

        index = self.aexp.eval(env, c_env)
        array = env[self.name2]    
        value = array[index[0]]
        env[self.name1] = value

# Index assignment statement class: y[1] := x
class IndexStatement_2(Statement):
    def __init__(self, name, aexp1, aexp2):
        self.name = name
        self.aexp1 = aexp1
        self.aexp2 = aexp2

    def __repr__(self):
        return 'IndexStatement_2(%s[%s]=%s)' % (self.name, self.aexp1, self.aexp2)

    def eval(self, env, c_env):
        index = self.aexp1.eval(env, c_env)
        # array = env[self.name1]
        value = self.aexp2.eval(env, c_env) 
        env[self.name][index[0]] = value  

# Index assignment statement class: y := x[1]
class IndexStatement_3(Statement):
    def __init__(self, name, aexp1, aexp2):
        self.name = name
        self.aexp1 = aexp1
        self.aexp2 = aexp2

    def __repr__(self):
        return 'IndexStatement_3(%s[%s]=%s)' % (self.name, self.aexp1, self.aexp2)

    def eval(self, env, c_env):
        index = self.aexp1.eval(env, c_env)
        # array = env[self.name1]
        value = self.aexp2.eval(env, c_env)
        env[self.name][index[0]] = value  

# Index assignment statement class: y := x[a]
class IndexStatement_4(Statement):
    def __init__(self, name1, name2, aexp):
        self.name1 = name1
        self.name2 = name2
        self.aexp = aexp

    def __repr__(self):
        return 'IndexStatement_4(%s=%s[%s])' % (self.name1, self.name2, self.aexp)

    def eval(self, env, c_env):
        # array = env[self.name1]
        # print env[self.name2]
        # print env[self.name3]
        value = env[self.name2][self.aexp.eval(env, c_env)]
        # print value
        env[self.name1] = value 

# Index assignment statement class: x[a] := 1
class IndexStatement_5(Statement):
    def __init__(self, name, aexp1, aexp2):
        self.name = name
        self.aexp1 = aexp1
        self.aexp2 = aexp2

    def __repr__(self):
        return 'IndexStatement_5(%s[%s]=%s)' % (self.name, self.aexp1, self.aexp2)

    def eval(self, env, c_env):
        # array = env[self.name1]
        # print env[self.name1]
        # print env[self.name2]
        value = self.aexp2.eval(env, c_env)
        env[self.name][self.aexp1.eval(env, c_env)] = value 

# Index assignment statement class: list[1] := list[2];
class IndexStatement_6(Statement):
    def __init__(self, name1, aexp1, name2, aexp2):
        self.name1 = name1
        self.name2 = name2
        self.aexp1 = aexp1
        self.aexp2 = aexp2

    def __repr__(self):
        return 'IndexStatement_6(%s[%s]=%s[%s])' % (self.name1, self.aexp1, self.name2, self.aexp2)

    def eval(self, env, c_env):
        # array = env[self.name1]
        # print env[self.name1]
        # print env[self.name2]
        value = env[self.name2][self.aexp2.eval(env, c_env)[0]]
        env[self.name1][self.aexp1.eval(env, c_env)[0]] = value

# Index assignment statement class: list[2] := list[a];
class IndexStatement_7(Statement):
    def __init__(self, name1, aexp1, name2, aexp2):
        self.name1 = name1
        self.aexp1 = aexp1
        self.name2 = name2
        self.aexp2 = aexp2

    def __repr__(self):
        return 'IndexStatement_7(%s[%s]=%s[%s])' % (self.name1, self.aexp1, self.name2, self.aexp2)

    def eval(self, env, c_env):
        # array = env[self.name1]
        # print env[self.name1]
        # print env[self.name2]
        value = env[self.name2][self.aexp2.eval(env, c_env)]
        env[self.name1][self.aexp1.eval(env, c_env)[0]] = value

# Index assignment statement class: list[a] := list[1];
class IndexStatement_8(Statement):
    def __init__(self, name1, aexp1, name2, aexp2):
        self.name1 = name1
        self.aexp1 = aexp1
        self.name2 = name2
        self.aexp2 = aexp2

    def __repr__(self):
        return 'IndexStatement_8(%s[%s]=%s[%s])' % (self.name1, self.aexp1, self.name2, self.aexp2)

    def eval(self, env, c_env):
        # array = env[self.name1]
        # print env[self.name1]
        # print env[self.name2]
        value = env[self.name2][self.aexp2.eval(env, c_env)[0]]
        env[self.name1][self.aexp1.eval(env, c_env)] = value

# Index assignment statement class: list[a] := list[a];
class IndexStatement_9(Statement):
    def __init__(self, name1, exp1, name2, exp2):
        self.name1 = name1
        self.name2 = name2
        self.exp1 = exp1
        self.exp2 = exp2

    def __repr__(self):
        return 'IndexStatement_9(%s[%s]=%s[%s])' % (self.name1, self.exp1, self.name2, self.exp2)

    def eval(self, env, c_env):
        # array = env[self.name1]
        # print env[self.name1]
        # print env[self.name2]
        value = env[self.name2][self.exp2.eval(env, c_env)]
        env[self.name1][self.exp1.eval(env, c_env)] = value

# Length statement class
class LengthStatement(Statement):
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def __repr__(self):
        return 'LengthStatement(%s=%s.l)' % (self.name1, self.name2)

    def eval(self, env, c_env):
        array = env[self.name2]
        env[self.name1] = len(array) 

# Int arithmatic class
class IntAexp(Aexp):
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return 'IntAexp(%d)' % self.i

    def eval(self, env, c_env):
        return self.i

# Array arithmatic class
class ArrayAexp(Aexp):
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return 'ArrayAexp'

    def eval(self, env, c_env):
        return self.i

# Str arithmatic class
class StrAexp(Aexp):
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return 'StrAexp'

    def eval(self, env, c_env):
        return self.i

# Variable arithmatic class
class VarAexp(Aexp):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'VarAexp(%s)' % self.name

    def eval(self, env, c_env):
        if self.name in env:
            return env[self.name]
        else:
            return 0

# Bool comparation class
class BinopAexp(Aexp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return 'BinopAexp(%s, %s, %s)' % (self.op, self.left, self.right)

    def eval(self, env, c_env):
        left_value = self.left.eval(env, c_env)
        right_value = self.right.eval(env, c_env)
        if type(left_value) == str:
            right_value = str(right_value)
        if type(right_value) == str:
            left_value = str(left_value)

        if self.op == '+':
            value = left_value + right_value
        elif self.op == '-':
            value = left_value - right_value
        elif self.op == '*':
            value = left_value * right_value
        elif self.op == '/':
            value = left_value / right_value
        else:
            raise RuntimeError('unknown operator: ' + self.op)
        return value

# Bool comparation class
class RelopBexp(Bexp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return 'RelopBexp(%s, %s, %s)' % (self.op, self.left, self.right)

    def eval(self, env, c_env):
        left_value = self.left.eval(env, c_env)
        right_value = self.right.eval(env, c_env)
        if type(left_value) == list and type(right_value) == list:
            if self.op == '<':
                raise RuntimeError('Can\'t do ' + self.op + ' between arrays')
            elif self.op == '<=':
                raise RuntimeError('Can\'t do ' + self.op + ' between arrays')
            elif self.op == '>':
                raise RuntimeError('Can\'t do ' + self.op + ' between arrays')
            elif self.op == '>=':
                raise RuntimeError('Can\'t do ' + self.op + ' between arrays')
            elif self.op == '=':
                value = left_value == right_value
            elif self.op == '!=':
                value = left_value != right_value
            else:
                raise RuntimeError('unknown operator: ' + self.op)
            return value            

        if self.op == '<':
            value = left_value < right_value
        elif self.op == '<=':
            value = left_value <= right_value
            c_env = right_value - left_value 
        elif self.op == '>':
            value = left_value > right_value
        elif self.op == '>=':
            value = left_value >= right_value
        elif self.op == '=':
            value = left_value == right_value
        elif self.op == '!=':
            value = left_value != right_value
        else:
            raise RuntimeError('unknown operator: ' + self.op)
        return value

# Bool comparation class for array and index
class RelopBexp2(Bexp):
    def __init__(self, name1, aexp1, op, name2, aexp2):
        self.op = op
        self.name1 = name1
        self.name2 = name2
        self.aexp1 = aexp1
        self.aexp2 = aexp2       

    def __repr__(self):
        return 'RelopBexp2(%s[%s] %s %s[%s])' % (self.name1, self.aexp1, self.op, self.name2, self.aexp2)

    def eval(self, env, c_env):
        if type(self.aexp1.eval(env, c_env)) == int:
            index1 = self.aexp1.eval(env, c_env)
        else:
            index1 = self.aexp1.eval(env, c_env)[0]

        if type(self.aexp2.eval(env, c_env)) == int:
            index2 = self.aexp2.eval(env, c_env)
        else:
            index2 = self.aexp2.eval(env, c_env)[0]

        left_value = env[self.name1][index1]
        right_value = env[self.name2][index2]
        if self.op == '<':
            value = left_value < right_value
        elif self.op == '<=':
            value = left_value <= right_value
        elif self.op == '>':
            value = left_value > right_value
        elif self.op == '>=':
            value = left_value >= right_value
        elif self.op == '=':
            value = left_value == right_value
        elif self.op == '!=':
            value = left_value != right_value
        else:
            raise RuntimeError('unknown operator: ' + self.op)
        return value


# And class
class AndBexp(Bexp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return 'AndBexp(%s, %s)' % (self.left, self.right)

    def eval(self, env, c_env):
        left_value = self.left.eval(env, c_env)
        right_value = self.right.eval(env, c_env)
        return left_value and right_value

# Or class
class OrBexp(Bexp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return 'OrBexp(%s, %s)' % (self.left, self.right)

    def eval(self, env, c_env):
        left_value = self.left.eval(env, c_env)
        right_value = self.right.eval(env, c_env)
        return left_value or right_value

# Not class
class NotBexp(Bexp):
    def __init__(self, exp):
        self.exp = exp

    def __repr__(self):
        return 'NotBexp(%s)' % self.exp

    def eval(self, env, c_env):
        value = self.exp.eval(env, c_env)
        return not value
