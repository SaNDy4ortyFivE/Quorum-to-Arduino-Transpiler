from antlr4 import *
from transpiler_beta.rulesLexer import rulesLexer
from transpiler_beta.rulesListener import rulesListener
from transpiler_beta.rulesParser import rulesParser
import transpiler_beta.handleNode
import sys
import asyncio



async def startTranspiling(filename):
    inp = FileStream(filename)
    lexer = rulesLexer(inp)
    stream = CommonTokenStream(lexer)
    tokens = CommonTokenStream(lexer)
    parser = rulesParser(stream)
    tree = parser.stmt()
    printer = rulesListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    return transpiler_beta.handleNode.getLines()
    # Print tokens as text (EOF is stripped from the end)
