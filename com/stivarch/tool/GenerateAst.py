#!/usr/bin/env python
import sys

class GenerateAst:
    def __init__(self, args):
        self.args = args

    def defineAst(self, outputDir, baseName, types):
        path = outputDir + "/" + baseName + ".java"
        print(path)

    def main(self):
        if(len(self.args) == 1):
            print("Usage GenerateAst <output directory>")
            exit(64)

        outputDir = self.args[1]

        self.defineAst(outputDir, "Expr", (
                "Binary : Expr left, Token opeartor, Expr right",
	            "Grouping : Expr expression",
	            "Literal : Object value",
	            "Unary : Token operator, Expr right"))

generateAst = GenerateAst(sys.argv)
generateAst.main()