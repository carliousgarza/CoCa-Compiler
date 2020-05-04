# Generated from patito.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .patitoParser import patitoParser
else:
    from patitoParser import patitoParser

from Compiler.compiler import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.quadruple import *
compiler = Compiler()


# This class defines a complete listener for a parse tree produced by patitoParser.
class patitoListener(ParseTreeListener):

    # Enter a parse tree produced by patitoParser#program.
    def enterProgram(self, ctx:patitoParser.ProgramContext):
        pass

    # Exit a parse tree produced by patitoParser#program.
    def exitProgram(self, ctx:patitoParser.ProgramContext):
        pass


    # Enter a parse tree produced by patitoParser#declarevars.
    def enterDeclarevars(self, ctx:patitoParser.DeclarevarsContext):
        pass

    # Exit a parse tree produced by patitoParser#declarevars.
    def exitDeclarevars(self, ctx:patitoParser.DeclarevarsContext):
        pass


    # Enter a parse tree produced by patitoParser#variables.
    def enterVariables(self, ctx:patitoParser.VariablesContext):
        pass

    # Exit a parse tree produced by patitoParser#variables.
    def exitVariables(self, ctx:patitoParser.VariablesContext):
        pass


    # Enter a parse tree produced by patitoParser#vartypes.
    def enterVartypes(self, ctx:patitoParser.VartypesContext):
        pass

    # Exit a parse tree produced by patitoParser#vartypes.
    def exitVartypes(self, ctx:patitoParser.VartypesContext):
        pass


    # Enter a parse tree produced by patitoParser#constant.
    def enterConstant(self, ctx:patitoParser.ConstantContext):
        pass

    # Exit a parse tree produced by patitoParser#constant.
    def exitConstant(self, ctx:patitoParser.ConstantContext):
        pass


    # Enter a parse tree produced by patitoParser#arrayconstant.
    def enterArrayconstant(self, ctx:patitoParser.ArrayconstantContext):
        pass

    # Exit a parse tree produced by patitoParser#arrayconstant.
    def exitArrayconstant(self, ctx:patitoParser.ArrayconstantContext):
        pass


    # Enter a parse tree produced by patitoParser#functions.
    def enterFunctions(self, ctx:patitoParser.FunctionsContext):
        pass

    # Exit a parse tree produced by patitoParser#functions.
    def exitFunctions(self, ctx:patitoParser.FunctionsContext):
        pass


    # Enter a parse tree produced by patitoParser#function.
    def enterFunction(self, ctx:patitoParser.FunctionContext):
        pass

    # Exit a parse tree produced by patitoParser#function.
    def exitFunction(self, ctx:patitoParser.FunctionContext):
        pass


    # Enter a parse tree produced by patitoParser#functiontype.
    def enterFunctiontype(self, ctx:patitoParser.FunctiontypeContext):
        pass

    # Exit a parse tree produced by patitoParser#functiontype.
    def exitFunctiontype(self, ctx:patitoParser.FunctiontypeContext):
        pass


    # Enter a parse tree produced by patitoParser#parameters.
    def enterParameters(self, ctx:patitoParser.ParametersContext):
        pass

    # Exit a parse tree produced by patitoParser#parameters.
    def exitParameters(self, ctx:patitoParser.ParametersContext):
        pass


    # Enter a parse tree produced by patitoParser#mexp.
    def enterMexp(self, ctx:patitoParser.MexpContext):
        pass

    # Exit a parse tree produced by patitoParser#mexp.
    def exitMexp(self, ctx:patitoParser.MexpContext):
        pass


    # Enter a parse tree produced by patitoParser#sexp.
    def enterSexp(self, ctx:patitoParser.SexpContext):
        pass

    # Exit a parse tree produced by patitoParser#sexp.
    def exitSexp(self, ctx:patitoParser.SexpContext):
        pass


    # Enter a parse tree produced by patitoParser#exp.
    def enterExp(self, ctx:patitoParser.ExpContext):
        pass

    # Exit a parse tree produced by patitoParser#exp.
    def exitExp(self, ctx:patitoParser.ExpContext):
        pass


    # Enter a parse tree produced by patitoParser#term.
    def enterTerm(self, ctx:patitoParser.TermContext):
        pass

    # Exit a parse tree produced by patitoParser#term.
    def exitTerm(self, ctx:patitoParser.TermContext):
        pass


    # Enter a parse tree produced by patitoParser#factor.
    def enterFactor(self, ctx:patitoParser.FactorContext):
        pass

    # Exit a parse tree produced by patitoParser#factor.
    def exitFactor(self, ctx:patitoParser.FactorContext):
        pass


    # Enter a parse tree produced by patitoParser#statute.
    def enterStatute(self, ctx:patitoParser.StatuteContext):
        pass

    # Exit a parse tree produced by patitoParser#statute.
    def exitStatute(self, ctx:patitoParser.StatuteContext):
        pass


    # Enter a parse tree produced by patitoParser#assignation.
    def enterAssignation(self, ctx:patitoParser.AssignationContext):
        pass

    # Exit a parse tree produced by patitoParser#assignation.
    def exitAssignation(self, ctx:patitoParser.AssignationContext):
        pass


    # Enter a parse tree produced by patitoParser#voidcall.
    def enterVoidcall(self, ctx:patitoParser.VoidcallContext):
        pass

    # Exit a parse tree produced by patitoParser#voidcall.
    def exitVoidcall(self, ctx:patitoParser.VoidcallContext):
        pass


    # Enter a parse tree produced by patitoParser#returncall.
    def enterReturncall(self, ctx:patitoParser.ReturncallContext):
        pass

    # Exit a parse tree produced by patitoParser#returncall.
    def exitReturncall(self, ctx:patitoParser.ReturncallContext):
        pass


    # Enter a parse tree produced by patitoParser#indexvariable.
    def enterIndexvariable(self, ctx:patitoParser.IndexvariableContext):
        pass

    # Exit a parse tree produced by patitoParser#indexvariable.
    def exitIndexvariable(self, ctx:patitoParser.IndexvariableContext):
        pass


    # Enter a parse tree produced by patitoParser#read.
    def enterRead(self, ctx:patitoParser.ReadContext):
        pass

    # Exit a parse tree produced by patitoParser#read.
    def exitRead(self, ctx:patitoParser.ReadContext):
        pass


    # Enter a parse tree produced by patitoParser#write.
    def enterWrite(self, ctx:patitoParser.WriteContext):
        pass

    # Exit a parse tree produced by patitoParser#write.
    def exitWrite(self, ctx:patitoParser.WriteContext):
        pass


    # Enter a parse tree produced by patitoParser#conditional.
    def enterConditional(self, ctx:patitoParser.ConditionalContext):
        pass

    # Exit a parse tree produced by patitoParser#conditional.
    def exitConditional(self, ctx:patitoParser.ConditionalContext):
        pass


    # Enter a parse tree produced by patitoParser#whileloop.
    def enterWhileloop(self, ctx:patitoParser.WhileloopContext):
        pass

    # Exit a parse tree produced by patitoParser#whileloop.
    def exitWhileloop(self, ctx:patitoParser.WhileloopContext):
        pass


    # Enter a parse tree produced by patitoParser#fromloop.
    def enterFromloop(self, ctx:patitoParser.FromloopContext):
        pass

    # Exit a parse tree produced by patitoParser#fromloop.
    def exitFromloop(self, ctx:patitoParser.FromloopContext):
        pass


    # Enter a parse tree produced by patitoParser#mainfunc.
    def enterMainfunc(self, ctx:patitoParser.MainfuncContext):
        pass

    # Exit a parse tree produced by patitoParser#mainfunc.
    def exitMainfunc(self, ctx:patitoParser.MainfuncContext):
        pass



del patitoParser