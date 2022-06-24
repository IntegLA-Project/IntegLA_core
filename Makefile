all:
	python3 main.py

# need `pip install yapf`
format:
	yapf -i `find -name "*.py"`

clean:
	rm -rf obj/
