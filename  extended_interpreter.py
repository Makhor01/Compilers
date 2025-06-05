from antlr4 import *
from ExtendedLangLexer import ExtendedLangLexer
from ExtendedLangParser import ExtendedLangParser
from ExtendedLangVisitor import ExtendedLangVisitor

class Value:
    def __init__(self, value, type_):
        self.value = value
        self.type = type_

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Value({self.value}, '{self.type}')"

class ExtendedInterpreter(ExtendedLangVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: ExtendedLangParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitAssignment(self, ctx: ExtendedLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitIfStatement(self, ctx: ExtendedLangParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        if condition.value:
            self.visit(ctx.block(0))
        elif ctx.elseBlock():
            self.visit(ctx.elseBlock())

    def visitElseBlock(self, ctx: ExtendedLangParser.ElseBlockContext):
        self.visit(ctx.block())

    def visitWhileStatement(self, ctx: ExtendedLangParser.WhileStatementContext):
        while self.visit(ctx.expression()).value:
            self.visit(ctx.block())

    def visitPrintStatement(self, ctx: ExtendedLangParser.PrintStatementContext):
        values = [self.visit(expr) for expr in ctx.expression()]
        print(", ".join(str(v) for v in values))

    def visitParenExpr(self, ctx: ExtendedLangParser.ParenExprContext):
        return self.visit(ctx.expression())

    def _check_types(self, left, right, op):
        # Разрешаем операции между int и float (преобразуем к float)
        if left.type == 'int' and right.type == 'int':
            return 'int'
        if (left.type in ('int', 'float') and right.type in ('int', 'float')):
            return 'float'
        if left.type == 'string' and right.type == 'string' and op == '+':
            return 'string'
        raise TypeError(f"Unsupported operand types for {op}: {left.type} and {right.type}")

    def visitMulDivExpr(self, ctx: ExtendedLangParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text

        result_type = self._check_types(left, right, op)

        if op == '*':
            if result_type == 'string':
                raise TypeError("Cannot multiply strings")
            return Value(left.value * right.value, result_type)
        elif op == '/':
            if right.value == 0:
                raise ZeroDivisionError("Division by zero")
            return Value(left.value / right.value, 'float')

    def visitAddSubExpr(self, ctx: ExtendedLangParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text

        if op == '+':
            if left.type == 'string' or right.type == 'string':
                return Value(str(left.value) + str(right.value), 'string')
            result_type = self._check_types(left, right, op)
            return Value(left.value + right.value, result_type)
        elif op == '-':
            result_type = self._check_types(left, right, op)
            return Value(left.value - right.value, result_type)

    def visitCompExpr(self, ctx: ExtendedLangParser.CompExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text

        if left.type != right.type and not (left.type in ('int', 'float') and right.type in ('int', 'float')):
            raise TypeError(f"Cannot compare {left.type} with {right.type}")

        if op == '<':
            return Value(left.value < right.value, 'bool')
        elif op == '>':
            return Value(left.value > right.value, 'bool')
        elif op == '<=':
            return Value(left.value <= right.value, 'bool')
        elif op == '>=':
            return Value(left.value >= right.value, 'bool')

    def visitEqNeqExpr(self, ctx: ExtendedLangParser.EqNeqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text

        if left.type != right.type and not (left.type in ('int', 'float') and right.type in ('int', 'float')):
            return Value(op == '!=', 'bool')

        if op == '==':
            return Value(left.value == right.value, 'bool')
        elif op == '!=':
            return Value(left.value != right.value, 'bool')

    def visitNumber(self, ctx: ExtendedLangParser.NumberContext):
        return Value(int(ctx.NUMBER().getText()), 'int')

    def visitFloat(self, ctx: ExtendedLangParser.FloatContext):
        return Value(float(ctx.FLOAT().getText()), 'float')

    def visitString(self, ctx: ExtendedLangParser.StringContext):
        text = ctx.STRING().getText()
        return Value(text[1:-1], 'string')

    def visitBool(self, ctx: ExtendedLangParser.BoolContext):
        return Value(ctx.BOOL().getText() == 'true', 'bool')

    def visitId(self, ctx: ExtendedLangParser.IdContext):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            raise NameError(f"Variable '{var_name}' is not defined")
        return self.variables[var_name]

def run_extended_program(filename):
    input_stream = FileStream(filename)
    lexer = ExtendedLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExtendedLangParser(stream)
    tree = parser.program()

    interpreter = ExtendedInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        run_extended_program(sys.argv[1])
    else:
        print("Usage: python extended_interpreter.py <filename>")