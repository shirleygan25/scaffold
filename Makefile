# Makefile  

# Example Makefile recipe

lint:
	pylint **/*.py

test:  
	pytest -vv 
	
format:
	black *.py
	
clean:
	rm -rf build
	
# Call with `make lint` etc
