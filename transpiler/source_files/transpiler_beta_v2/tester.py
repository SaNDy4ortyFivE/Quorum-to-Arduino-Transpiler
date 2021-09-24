from antlr4 import *
from transpiler_beta_v2.rulesLexer import rulesLexer
from transpiler_beta_v2.rulesListener import rulesListener
from transpiler_beta_v2.rulesParser import rulesParser
import transpiler_beta_v2.handleNode
import sys
import asyncio
import time


async def startTranspiling(filename):
    start_time = time.perf_counter()
    inp = FileStream(filename)
    lexer = rulesLexer(inp)
    stream = CommonTokenStream(lexer)
    tokens = CommonTokenStream(lexer)
    parser = rulesParser(stream)
    tree = parser.stmt()
    printer = rulesListener()
    walker = ParseTreeWalker()
    transpilation_start = time.perf_counter()
    walker.walk(printer, tree)
    finish_time = time.perf_counter()
    ##result analysis
    print("Setup time:{0:.5f}".format(transpilation_start-start_time))
    print("Transpilation time:{0:.5f}".format(finish_time-transpilation_start))
    print("Total time:{0:.5f}".format(finish_time-start_time))
    return transpiler_beta_v2.handleNode.getLines()
    # Print tokens as text (EOF is stripped from the end)
