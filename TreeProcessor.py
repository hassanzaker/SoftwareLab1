from lark import Transformer
import math
import random
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

    def abs_exp(self, args):
        if args[0] >= 0:
            return args[0]
        else:
            return -1 * args[0]

    def sqrt_exp(self, args):
        if args[0] >= 0:
            return math.sqrt(args[0])
        else:
            raise Exception("negative value for sqrt")

    def pow(self, args):
        return args[0] ** args[1]

    def neg_exp(self, args):
        return -args[0]

    def sin(self, args):
        return math.sin(args[0] / 180 * math.pi)

    def cos(self, args):
        return math.cos(args[0] / 180 * math.pi)

    def tan(self, args):
        return math.tan(args[0] / 180 * math.pi)

    def cot(self, args):
        return 1 / math.tan(args[0] / 180 * math.pi)

    def log(self, args):
        if args[0] <= 0:
            raise Exception('unexpected value for log')
        if args[1] <= 0 or args[1] == 1:
            raise Exception('unexpected value for log')
        return math.log(args[0], args[1])

    def rand(self, args):
        return random.random()