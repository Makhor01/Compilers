# Generated from SimpleLang.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#program.
    def enterProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#program.
    def exitProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#statement.
    def enterStatement(self, ctx:SimpleLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#statement.
    def exitStatement(self, ctx:SimpleLangParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#assignment.
    def enterAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#assignment.
    def exitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ifStatement.
    def enterIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ifStatement.
    def exitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#whileStatement.
    def enterWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#whileStatement.
    def exitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#block.
    def enterBlock(self, ctx:SimpleLangParser.BlockContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#block.
    def exitBlock(self, ctx:SimpleLangParser.BlockContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#printStatement.
    def enterPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#printStatement.
    def exitPrintStatement(self, ctx:SimpleLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#number.
    def enterNumber(self, ctx:SimpleLangParser.NumberContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#number.
    def exitNumber(self, ctx:SimpleLangParser.NumberContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#addSubExpr.
    def enterAddSubExpr(self, ctx:SimpleLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#addSubExpr.
    def exitAddSubExpr(self, ctx:SimpleLangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#compExpr.
    def enterCompExpr(self, ctx:SimpleLangParser.CompExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#compExpr.
    def exitCompExpr(self, ctx:SimpleLangParser.CompExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#id.
    def enterId(self, ctx:SimpleLangParser.IdContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#id.
    def exitId(self, ctx:SimpleLangParser.IdContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:SimpleLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:SimpleLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#parenExpr.
    def enterParenExpr(self, ctx:SimpleLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#parenExpr.
    def exitParenExpr(self, ctx:SimpleLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#eqNeqExpr.
    def enterEqNeqExpr(self, ctx:SimpleLangParser.EqNeqExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#eqNeqExpr.
    def exitEqNeqExpr(self, ctx:SimpleLangParser.EqNeqExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#op.
    def enterOp(self, ctx:SimpleLangParser.OpContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#op.
    def exitOp(self, ctx:SimpleLangParser.OpContext):
        pass



del SimpleLangParser