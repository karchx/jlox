.PHONY: __all

__all: compile

compile:
	javac -sourcepath . com/stivarch/lox/*.java


run:
	java com.stivarch.lox.Lox

tool/%:
	 python com/stivarch/tool/GenerateAst.py $*

clean:
	rm -rf com/stivarch/lox/*.class
