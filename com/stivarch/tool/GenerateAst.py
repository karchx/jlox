#!/usr/bin/env python
import sys

class GenerateAst:
    def __init__(self, args):
        self.args = args

    def defineAst(self, outputDir, baseName, types):
        path = outputDir + "/" + baseName + ".java"
        writer = open(path, "w")
        writer.write("package com.stivarch.lox;")
        writer.write("\n")
        writer.write("\nimport java.util.List;")
        writer.write("\n")
        writer.write("\nabstract class " + baseName +" {")
        writer.write("\n")

        self.defineVisitor(writer, baseName, types)

        # The AST classes.
        for t in types:
            className = t.split(":")[0].strip()
            fields = t.split(":")[1].strip()
            self.defineType(writer, baseName, className, fields)
        
        writer.close()
        

    def defineVisitor(self, writer, baseName, types):
        writer.write("\n  interface Visitor<R> {")

        for t in types:
            typeName = t.split(":")[0].strip()
            writer.write("\n    R visit" + typeName + baseName + "(" + typeName + " " + baseName.lower() + ");")

        writer.write("\n  }")
        writer.write("\n")
           

    def defineType(self, writer, baseName, className, fieldList):
        writer.write("\nstatic class " + className + " extends " + baseName + " {")
        # constructor
        writer.write("\n    " + className + "(" + fieldList + ") {")
        
        # Store parameters in fields.
        fields = fieldList.split(", ")
        for field in fields:
            name = field.split(" ")[1]
            writer.write("\n      this." + name + " = " + name + ";")
            
        writer.write("\n")
        writer.write("    }")

        # Visitor pattern.
        writer.write("\n")
        writer.write("\n    @Override")
        writer.write("\n    <R> R accept(Visitor<R> visitor) {")
        writer.write("\n      return visitor.visit" + className + baseName + "(this);")
        writer.write("\n    }")

        # Fields.
        writer.write("\n")
        for field in fields:
            writer.write("\n    final " + field + ";")
            
        writer.write("\n  }")
        writer.write("\n")

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
