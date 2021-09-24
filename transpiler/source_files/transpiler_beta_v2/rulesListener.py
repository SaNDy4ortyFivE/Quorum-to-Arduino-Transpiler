# Generated from rules.g4 by ANTLR 4.8
from antlr4 import *
from transpiler_beta_v2 import handleNode

if __name__ is not None and "." in __name__:
    from .rulesParser import rulesParser
else:
    from rulesParser import rulesParser

# This class defines a complete listener for a parse tree produced by rulesParser.
class rulesListener(ParseTreeListener):

    # Enter a parse tree produced by rulesParser#stmt.
    def enterStmt(self, ctx:rulesParser.StmtContext):
        handleNode.initTree()
        pass

    # Exit a parse tree produced by rulesParser#stmt.
    def exitStmt(self, ctx:rulesParser.StmtContext):
        ##handleNode.printTree()
        handleNode.startTranspiling()
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
        lib_name = None
        funs_name = None
        var = ctx.VARIABLE(0).getText()
        value = None
        if not ctx.NUMB() is None:
            value = ctx.NUMB().getText()
        elif not ctx.FLOAT() is None:
            value = ctx.FLOAT().getText()
        else:
            lib_name = ctx.VARIABLE(1).getText()
            if not ctx.ret_val().ret_high_low() is None:
                if not ctx.ret_val().ret_high_low().IRED_READ() is None:
                    funs_name =  ctx.ret_val().ret_high_low().IRED_READ().getText()
                    ##print("tring to read value of IR {}...".format(lib_name))
                elif not ctx.ret_val().ret_high_low().BTN_STATE() is None:
                    funs_name =  ctx.ret_val().ret_high_low().BTN_STATE().getText()
                    ##print("tring to read state of button {}...".format(lib_name))
            elif not ctx.ret_val().ret_integer() is None:
                if not ctx.ret_val().ret_integer().USONIC_DIST() is None:
                    funs_name =  ctx.ret_val().ret_integer().USONIC_DIST().getText()
                    ##print("tring to read distance from USONIC {}...".format(lib_name))
            elif not ctx.ret_val().ret_number() is None:
                if not ctx.ret_val().ret_number().LMTEMP_READ() is None:
                    funs_name =  ctx.ret_val().ret_number().LMTEMP_READ().getText()
                    ##print("tring to read temperature from LMTEMP {}...".format(lib_name))
        ##print("var={}, value={}, lib={}, funs={}".format(var, value, lib_name, funs_name))
        handleNode.addAssign(var, value, lib_name, funs_name)
        pass

    # Exit a parse tree produced by rulesParser#assign.
    def exitAssign(self, ctx:rulesParser.AssignContext):
        pass


    # Enter a parse tree produced by rulesParser#both.
    def enterBoth(self, ctx:rulesParser.BothContext):
        pass

    # Exit a parse tree produced by rulesParser#both.
    def exitBoth(self, ctx:rulesParser.BothContext):
        var = ctx.VARIABLE(0).getText()
        i = ctx.d_type().INTEGER()
        n = ctx.d_type().NUMBER()
        value = None
        funs_name = None
        lib_name = None
        d_type = i.getText() if not i is None else n.getText()
        if not ctx.NUMB() is None:
            value = ctx.NUMB().getText()
        elif not ctx.FLOAT() is None:
            value = ctx.NUMB().getText()
        else:
            lib_name = ctx.VARIABLE(1).getText()
            if not ctx.ret_val().ret_high_low() is None:
                if not ctx.ret_val().ret_high_low().IRED_READ() is None:
                    funs_name =  ctx.ret_val().ret_high_low().IRED_READ().getText()
                    ##print("tring to read value of IR {}...".format(lib_name))
                else:
                    funs_name =  ctx.ret_val().ret_high_low().BTN_STATE().getText()
                    ##print("tring to read state of button {}...".format(lib_name))
            elif not ctx.ret_val().ret_integer() is None:
                if not ctx.ret_val().ret_integer().USONIC_DIST() is None:
                    funs_name =  ctx.ret_val().ret_integer().USONIC_DIST().getText()
                    ##print("tring to read distance from USONIC {}...".format(lib_name))
            elif not ctx.ret_val().ret_number() is None:
                if not ctx.ret_val().ret_number().LMTEMP_READ() is None:
                    funs_name =  ctx.ret_val().ret_number().LMTEMP_READ().getText()
                    ##print("tring to read temperature from LMTEMP {}...".format(lib_name))
        ##print("dtype={}, var={}, value={}, lib={}, funs={}".format(d_type, var, value, lib_name, funs_name))
        handleNode.addBoth(d_type,var,value,lib_name,funs_name)
        pass


    # Enter a parse tree produced by rulesParser#d_type.
    def enterD_type(self, ctx:rulesParser.D_typeContext):
        pass

    # Exit a parse tree produced by rulesParser#d_type.
    def exitD_type(self, ctx:rulesParser.D_typeContext):
        pass


    # Enter a parse tree produced by rulesParser#conditional.
    def enterConditional(self, ctx:rulesParser.ConditionalContext):
        if not ctx.ELSE() is None:
            handleNode.addNodeElse()
        pass

    # Exit a parse tree produced by rulesParser#conditional.
    def exitConditional(self, ctx:rulesParser.ConditionalContext):
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
        shortctx = None
        ##check which function it is
        if not ctx.funs().led_related() is None:
            shortctx = ctx.funs().led_related()
            if not shortctx.LED_ON() is None:
                ##print("Turning LED {} on...".format(ins))
                handleNode.turnLedOn(ins)
            elif not shortctx.LED_OFF() is None:
                ##print("Turning LED {} off...".format(ins))
                handleNode.turnLedOff(ins)
            elif not shortctx.LED_PIN() is None:
                p = int(shortctx.LED_PIN().getText()[7:-1])
                ##print("LED connected at pin {}".format(p))
                handleNode.addLED(ins, p)
        elif not ctx.funs().ired_related() is None:
            shortctx = ctx.funs().ired_related()
            if not shortctx.IRED_READ() is None:
                ##print("tring to read to {} IR...".format(ins))
                handleNode.readIRED(ins)
            else:
                p = int(shortctx.IRED_PIN().getText()[6:-1])
                ##print("IR {} connected at pin {}".format(ins, p))
                handleNode.addIRED(ins, p)
        elif not ctx.funs().usonic_related() is None:
            shortctx = ctx.funs().usonic_related()
            if not shortctx.TRIG_PIN() is None:
                tp = int(shortctx.TRIG_PIN().getText()[8:-1])
                ##print("USON {} has trig pin at {}".format(ins, tp))
                handleNode.addUsonTrig(ins, tp)
            elif not shortctx.ECHO_PIN() is None:
                ep = int(shortctx.ECHO_PIN().getText()[8:-1])
                ##print("USON {} has echo pin at {}".format(ins, ep))
                handleNode.addUsonEcho(ins, ep)
            else:
                ##print("Reading distance from US {}".format(ins))
                handleNode.readUsonDist(ins)
        elif not ctx.funs().btn_related() is None:
            shortctx = ctx.funs().btn_related()
            if not shortctx.BTN_PIN() is None:
                p = int(shortctx.BTN_PIN().getText()[7:-1])
                ##print("Button {} connected at {}".format(ins, p))
                handleNode.addButton(ins, p)
            else:
                ##print("Reading state of button {}".format(ins))
                handleNode.readBtnState(ins)
        else:
            shortctx = ctx.funs().lmtemp_related()
            if not shortctx.LMTEMP_PIN() is None:
                p = int(shortctx.LMTEMP_PIN().getText()[8:-1])
                ##print("LMTEMP {} connected at {}".format(ins, p))
                handleNode.addLMTEMP(ins, p)
            else:
                ##print("Reading Temperature from button {}".format(ins))
                handleNode.readLMTemp()
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


    # Enter a parse tree produced by rulesParser#ired_related.
    def enterIred_related(self, ctx:rulesParser.Ired_relatedContext):
        pass

    # Exit a parse tree produced by rulesParser#ired_related.
    def exitIred_related(self, ctx:rulesParser.Ired_relatedContext):
        pass


    # Enter a parse tree produced by rulesParser#usonic_related.
    def enterUsonic_related(self, ctx:rulesParser.Usonic_relatedContext):
        pass

    # Exit a parse tree produced by rulesParser#usonic_related.
    def exitUsonic_related(self, ctx:rulesParser.Usonic_relatedContext):
        pass


    # Enter a parse tree produced by rulesParser#btn_related.
    def enterBtn_related(self, ctx:rulesParser.Btn_relatedContext):
        pass

    # Exit a parse tree produced by rulesParser#btn_related.
    def exitBtn_related(self, ctx:rulesParser.Btn_relatedContext):
        pass


    # Enter a parse tree produced by rulesParser#lmtemp_related.
    def enterLmtemp_related(self, ctx:rulesParser.Lmtemp_relatedContext):
        pass

    # Exit a parse tree produced by rulesParser#lmtemp_related.
    def exitLmtemp_related(self, ctx:rulesParser.Lmtemp_relatedContext):
        pass


    # Enter a parse tree produced by rulesParser#ret_val.
    def enterRet_val(self, ctx:rulesParser.Ret_valContext):
        pass

    # Exit a parse tree produced by rulesParser#ret_val.
    def exitRet_val(self, ctx:rulesParser.Ret_valContext):
        pass


    # Enter a parse tree produced by rulesParser#ret_high_low.
    def enterRet_high_low(self, ctx:rulesParser.Ret_high_lowContext):
        pass

    # Exit a parse tree produced by rulesParser#ret_high_low.
    def exitRet_high_low(self, ctx:rulesParser.Ret_high_lowContext):
        pass


    # Enter a parse tree produced by rulesParser#ret_integer.
    def enterRet_integer(self, ctx:rulesParser.Ret_integerContext):
        pass

    # Exit a parse tree produced by rulesParser#ret_integer.
    def exitRet_integer(self, ctx:rulesParser.Ret_integerContext):
        pass


    # Enter a parse tree produced by rulesParser#ret_number.
    def enterRet_number(self, ctx:rulesParser.Ret_numberContext):
        pass

    # Exit a parse tree produced by rulesParser#ret_number.
    def exitRet_number(self, ctx:rulesParser.Ret_numberContext):
        pass



del rulesParser
