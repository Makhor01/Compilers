# Generated from SimpleLang.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#program.
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignment.
    def visitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ifStatement.
    def visitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#whileStatement.
    def visitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#block.
    def visitBlock(self, ctx:SimpleLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#printStatement.
    def visitPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#number.
    def visitNumber(self, ctx:SimpleLangParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#addSubExpr.
    def visitAddSubExpr(self, ctx:SimpleLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#compExpr.
    def visitCompExpr(self, ctx:SimpleLangParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#id.
    def visitId(self, ctx:SimpleLangParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:SimpleLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#parenExpr.
    def visitParenExpr(self, ctx:SimpleLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#eqNeqExpr.
    def visitEqNeqExpr(self, ctx:SimpleLangParser.EqNeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#op.
    def visitOp(self, ctx:SimpleLangParser.OpContext):
        return self.visitChildren(ctx)



del SimpleLangParser