from lark import Lark

grammer = """
    exp: exp "%" aexp -> mod
        | aexp -> aexp
    aexp: aexp "+" bexp -> add
        | aexp "-" bexp -> sub
        | bexp -> bexp
    bexp: bexp "*" cexp -> mul
        | bexp "/" cexp -> div
        | bexp "**" cexp -> pow
        | cexp -> cexp
    cexp: "(" exp ")" -> par_exp_par
        | "|" exp "|" -> abs_exp
        | "[" exp "]" -> floor_exp
        | "-" exp -> neg_exp
        | "sqrt(" exp ")" -> sqrt_exp
        | "sin(" exp ")" -> sin
        | "cos(" exp ")" -> cos
        | "tan(" exp ")" -> tan
        | "cot(" exp ")" -> cot
        | "rand" -> rand
        | "sign" exp -> sign
        | "max(" (exp ",")+ exp ")" -> max
        | "min(" (exp ",")+ exp ")" -> min
        | "log(" exp "," exp ")" -> log
        | constant -> constant
    
    constant : INT -> constant_int
            | DOUBLE -> constant_double
            | "pi" -> pi_constant
            | "e" -> e_constant
    DOUBLE.2 : /(\\d)+\\.(\\d)*/
    INT: /[0-9]+/   
    
    %import common.WS -> WHITESPACE
    %ignore WHITESPACE
"""