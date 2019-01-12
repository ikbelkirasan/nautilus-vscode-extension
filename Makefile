# Author: Ricardo Rodrigues

DEST=~/.local/share/nautilus-python/extensions/

SOURCES = \
		VSCodeExtension.py

DEST_SOURCES=$(join $(DEST), $(notdir $(SOURCES))) 
DEST_SOURCES_COMPILED=$(join $(DEST), $(notdir $(SOURCES:.py=.pyc))) 

all: copy close-nautilus

copy: $(SOURCES)
	mkdir -p $(DEST)
	cp -f -t $(DEST) $(SOURCES)

close-nautilus:
	@nautilus -q || true

clean:
	@echo Deleting $(DEST_SOURCES)
	rm -f $(DEST_SOURCES) $(DEST_SOURCES_COMPILED)