from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor


class Interpreter(SimpleLangVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitAssignment(self, ctx: SimpleLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitIfStatement(self, ctx: SimpleLangParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        if condition:
            self.visit(ctx.block(0))
        elif ctx.elseBlock():
            self.visit(ctx.elseBlock())

    def visitElseBlock(self, ctx: SimpleLangParser.BlockContext):
        self.visit(ctx.block())

    def visitWhileStatement(self, ctx: SimpleLangParser.WhileStatementContext):
        while self.visit(ctx.expression()):
            self.visit(ctx.block())

    def visitPrintStatement(self, ctx: SimpleLangParser.PrintStatementContext):
        value = self.visit(ctx.expression())
        print(value)

    def visitParenExpr(self, ctx: SimpleLangParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitMulDivExpr(self, ctx: SimpleLangParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.operator.text
        if op == '*':
            return left * right
        elif op == '/':
            return left // right

    def visitAddSubExpr(self, ctx: SimpleLangParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.operator.text
        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    def visitCompExpr(self, ctx: SimpleLangParser.CompExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.operator.text
        if op == '<':
            return 1 if left < right else 0
        elif op == '>':
            return 1 if left > right else 0
        elif op == '<=':
            return 1 if left <= right else 0
        elif op == '>=':
            return 1 if left >= right else 0

    def visitEqNeqExpr(self, ctx: SimpleLangParser.EqNeqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.operator.text
        if op == '==':
            return 1 if left == right else 0
        elif op == '!=':
            return 1 if left != right else 0

    def visitNumber(self, ctx: SimpleLangParser.NumberContext):
        return int(ctx.NUMBER().getText())

    def visitId(self, ctx: SimpleLangParser.IdContext):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            raise NameError(f"Variable '{var_name}' is not defined")
        return self.variables[var_name]


def run_program(filename):
    input_stream = FileStream(filename, encoding='utf-8')
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)
    tree = parser.program()

    interpreter = Interpreter()
    interpreter.visit(tree)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        run_program(sys.argv[1])
    else:
        print("Usage: python interpreter.py <filename>")