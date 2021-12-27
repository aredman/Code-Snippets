all: LunarLander.cpp SpaceCraft.cpp
	g++ SpaceCraft.h
	g++ LunarLander.cpp -o LunarLander
clean:
	rm LunarLander *.gch
run: LunarLander
	./LunarLander

SpaceCraft: SpaceCraft.cpp SpaceCraft.h
	g++ SpaceCraft.cpp

doc: doc.md
	pandoc doc.md --pdf-engine=pdflatex -o doc.pdf
