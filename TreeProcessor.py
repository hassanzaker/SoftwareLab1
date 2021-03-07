from lark import Transformer

class Calculator(Transformer):

    def constant_int(self, args):
        val = int(args[0].value, 0)
        return val

    def constant_double(self, args):
        val = float(args[0].value)
        return val

    def constant(self, args):
        return args[0]

    def cexp(self, args):
        return args[0]

    def bexp(self, args):
        return args[0]

    def aexp(self, args):
        return args[0]

    def add(self, args):
        return args[0] + args[1]

    def sub(self, args):
        return args[0] - args[1]

    def mul(self, args):
        return args[0] * args[1]

    def div(self, args):
        return args[0] / args[1]

    def mod(self, args):
        return args[0] % args[1]

    def par_exp_par(self, args):
        return args[0]