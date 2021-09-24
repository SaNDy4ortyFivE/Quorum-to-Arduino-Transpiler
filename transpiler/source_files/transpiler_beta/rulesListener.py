# Generated from rules.g4 by ANTLR 4.8
from antlr4 import *
from transpiler_beta import handleNode

if __name__ is not None and "." in __name__:
    from .rulesParser import rulesParser
else:
    from rulesParser import rulesParser

# This class defines a complete listener for a parse tree produced by rulesParser.
class rulesListener(ParseTreeListener):

    # Enter a parse tree produced by rulesParser#stmt.
    def enterStmt(self, ctx:rulesParser.StmtContext):
        pass

    # Exit a parse tree produced by rulesParser#stmt.
    def exitStmt(self, ctx:rulesParser.StmtContext):
        handleNode.printTree()
        pass


    # Enter a parse tree produced by rulesParser#line.
    def enterLine(self, ctx:rulesParser.LineContext):
        if not ctx.END() is None:
            handleNode.addNodeEnd()
        pass

    # Exit a parse tree produced by rulesParser#line.
    def exitLine(self, ctx:rulesParser.LineContext):
        pass


    # Enter a parse tree produced by rulesParser#v_init.
    def enterV_init(self, ctx:rulesParser.V_initContext):
        pass

    # Exit a parse tree produced by rulesParser#v_init.
    def exitV_init(self, ctx:rulesParser.V_initContext):
        pass


    # Enter a parse tree produced by rulesParser#decl.
    def enterDecl(self, ctx:rulesParser.DeclContext):
        var = ctx.VARIABLE().getText()
        i = ctx.d_type().INTEGER()
        n = ctx.d_type().NUMBER()
        d_type = i.getText() if not i is None else n.getText()
        handleNode.addDecl(d_type, var)
        pass

    # Exit a parse tree produced by rulesParser#decl.
    def exitDecl(self, ctx:rulesParser.DeclContext):
        pass


    # Enter a parse tree produced by rulesParser#assign.
    def enterAssign(self, ctx:rulesParser.AssignContext):
        var = ctx.VARIABLE().getText()
        value = ctx.NUMB().getText()
        handleNode.addAssign(var, value)
        pass

    # Exit a parse tree produced by rulesParser#assign.
    def exitAssign(self, ctx:rulesParser.AssignContext):
        pass


    # Enter a parse tree produced by rulesParser#both.
    def enterBoth(self, ctx:rulesParser.BothContext):
        i = ctx.d_type().INTEGER()
        n = ctx.d_type().NUMBER()
        d_type = i.getText() if not i is None else n.getText()
        var = ctx.VARIABLE().getText()
        val = ctx.NUMB().getText()
        handleNode.addBoth(d_type,var,val)
        pass

    # Exit a parse tree produced by rulesParser#both.
    def exitBoth(self, ctx:rulesParser.BothContext):
        pass


    # Enter a parse tree produced by rulesParser#d_type.
    def enterD_type(self, ctx:rulesParser.D_typeContext):
        pass

    # Exit a parse tree produced by rulesParser#d_type.
    def exitD_type(self, ctx:rulesParser.D_typeContext):
        pass


    # Enter a parse tree produced by rulesParser#conditional.
    def enterConditional(self, ctx:rulesParser.ConditionalContext):
        pass

    # Exit a parse tree produced by rulesParser#conditional.
    def exitConditional(self, ctx:rulesParser.ConditionalContext):
        if not ctx.ELSE() is None:
            handleNode.addNodeElse()
        pass


    # Enter a parse tree produced by rulesParser#r_if.
    def enterR_if(self, ctx:rulesParser.R_ifContext):
        val1,val2=0,0
        rel = ctx.relation().GREATER()
        if rel is None:
            rel = ctx.relation().LESS()
        if rel is None:
            rel = ctx.relation().EQUAL()
        if len(ctx.VARIABLE())==2:
            val1 = ctx.VARIABLE(0)
            val2 = ctx.VARIABLE(1)
        elif len(ctx.NUMB())==2:
            val1 = ctx.NUMB(0)
            val2 = ctx.NUMB(1)
        else:
            varb = ctx.VARIABLE(0).getSymbol()
            numb = ctx.NUMB(0).getSymbol()
            ##check indices
            if varb.tokenIndex < numb.tokenIndex:
                val1 = ctx.VARIABLE(0)
                val2 = ctx.NUMB(0)
            else:
                val1 = ctx.NUMB(0)
                val2 = ctx.VARIABLE(0)
        handleNode.addIf(val1.getText(),val2.getText(),rel.getText())
        pass

    # Exit a parse tree produced by rulesParser#r_if.
    def exitR_if(self, ctx:rulesParser.R_ifContext):
        pass


    # Enter a parse tree produced by rulesParser#r_elif.
    def enterR_elif(self, ctx:rulesParser.R_elifContext):
        pass

    # Exit a parse tree produced by rulesParser#r_elif.
    def exitR_elif(self, ctx:rulesParser.R_elifContext):
        pass


    # Enter a parse tree produced by rulesParser#relation.
    def enterRelation(self, ctx:rulesParser.RelationContext):
        pass

    # Exit a parse tree produced by rulesParser#relation.
    def exitRelation(self, ctx:rulesParser.RelationContext):
        pass


    # Enter a parse tree produced by rulesParser#output.
    def enterOutput(self, ctx:rulesParser.OutputContext):
        handleNode.addNodeOutput(ctx.VARIABLE()[-1].getText())
        pass

    # Exit a parse tree produced by rulesParser#output.
    def exitOutput(self, ctx:rulesParser.OutputContext):
        pass

    # Enter a parse tree produced by rulesParser#other.
    def enterOther(self, ctx:rulesParser.OtherContext):
        pass

    # Exit a parse tree produced by rulesParser#other.
    def exitOther(self, ctx:rulesParser.OtherContext):
        pass


    # Enter a parse tree produced by rulesParser#use.
    def enterUse(self, ctx:rulesParser.UseContext):
        pass

    # Exit a parse tree produced by rulesParser#use.
    def exitUse(self, ctx:rulesParser.UseContext):
        pass


    # Enter a parse tree produced by rulesParser#inst.
    def enterInst(self, ctx:rulesParser.InstContext):
        pass

    # Exit a parse tree produced by rulesParser#inst.
    def exitInst(self, ctx:rulesParser.InstContext):
        pass


    # Enter a parse tree produced by rulesParser#lib.
    def enterLib(self, ctx:rulesParser.LibContext):
        pass

    # Exit a parse tree produced by rulesParser#lib.
    def exitLib(self, ctx:rulesParser.LibContext):
        pass


    # Enter a parse tree produced by rulesParser#class_.
    def enterClass_(self, ctx:rulesParser.Class_Context):
        pass

    # Exit a parse tree produced by rulesParser#class_.
    def exitClass_(self, ctx:rulesParser.Class_Context):
        pass


    # Enter a parse tree produced by rulesParser#action.
    def enterAction(self, ctx:rulesParser.ActionContext):
        pass

    # Exit a parse tree produced by rulesParser#action.
    def exitAction(self, ctx:rulesParser.ActionContext):
        pass


    # Enter a parse tree produced by rulesParser#funcall.
    def enterFuncall(self, ctx:rulesParser.FuncallContext):
        ins = ctx.VARIABLE().getText()
        fctx = ctx.funs()
        if not fctx.led_related() is None:
            if not fctx.led_related().LED_ON() is None:
                #print("LED {} is turned on...".format(ins))
                handleNode.turnLedOn(ins)
            elif not fctx.led_related().LED_OFF() is None:
                #print("LED {} is turned off...".format(ins))
                handleNode.turnLedOff(ins)
            else:
                #print("{} is set on pin:{}".format(ins, ctx.funs().LED_PIN().getText()))
                p = int(fctx.led_related().LED_PIN().getText()[4:-1])
                handleNode.addLED(ins, p)
        pass

    # Exit a parse tree produced by rulesParser#funcall.
    def exitFuncall(self, ctx:rulesParser.FuncallContext):
        pass


    # Enter a parse tree produced by rulesParser#funs.
    def enterFuns(self, ctx:rulesParser.FunsContext):
        pass

    # Exit a parse tree produced by rulesParser#funs.
    def exitFuns(self, ctx:rulesParser.FunsContext):
        pass


    # Enter a parse tree produced by rulesParser#led_related.
    def enterLed_related(self, ctx:rulesParser.Led_relatedContext):
        pass

    # Exit a parse tree produced by rulesParser#led_related.
    def exitLed_related(self, ctx:rulesParser.Led_relatedContext):
        pass



del rulesParser
