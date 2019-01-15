from llvmlite import ir

class Prog():
    def __init__(self, builder, module, value1, value2):
        self.builder = builder
        self.module = module
        self.value1 = value1
        self.value2 = value2

    def eval(self):
        self.value1.eval()
        # i = ir.Constant(self.value1.eval()) 
        self.value2.eval()    
        return 

class Prog_int():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        self.value.eval()
        return 

class Number():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        i = ir.Constant(ir.IntType(8), int(self.value))
        return i

# class Name():
#     def __init__(self, builder, module, value):
#         self.builder = builder
#         self.module = module
#         self.value = value

#     def eval(self):
#         i = ir.Constant(ir.PointerType(str), int(self.value))
#         # print self.value
#         return i

# class Assign():
#     def __init__(self, builder, module, value):
#         self.builder = builder
#         self.module = module
#         self.value = value

#     def eval(self):
#         return self.value

class BinaryOp():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i


class Sub(BinaryOp):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i

# class Mul(BinaryOp):
#     def eval(self):
#         # i = self.left.eval() * self.right.eval()
#         i = self.builder.mul(self.left.eval(), self.right.eval())
#         return i
class Mul(BinaryOp):
    def eval(self):
        i = self.builder.mul(self.left.eval(), self.right.eval())
        return i

class Div(BinaryOp):
    def eval(self):
        i = self.builder.sdiv(self.left.eval(), self.right.eval())
        return i

class Less_equal(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('<=',self.left.eval(), self.right.eval())
        return i

class Greater_equal(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('>=',self.left.eval(), self.right.eval())
        return i

class Greater(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('>',self.left.eval(), self.right.eval())
        return i

class Less(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('<',self.left.eval(), self.right.eval())
        return i

class Not_equal(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('!=',self.left.eval(), self.right.eval())
        return i

class Equal(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('==',self.left.eval(), self.right.eval())
        return i



class Print():
    def __init__(self, builder, module, printf, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value

    def eval(self):
        value = self.value.eval()

        # Declare argument list
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr" + str(self.value))
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Call Print Function
        self.builder.call(self.printf, [fmt_arg, value])

class If_stm():
    def __init__(self, builder, module, value1, value2, value3):
        self.builder = builder
        self.module = module
        self.value1 = value1
        self.value2 = value2        
        self.value3 = value3 

    def eval(self):
        with self.builder.if_else(self.value1.eval()) as (then, otherwise):
            with then:
                # print '111111111'
                self.value2.eval()
            with otherwise:
                # print '222222222'
                self.value3.eval()
        return