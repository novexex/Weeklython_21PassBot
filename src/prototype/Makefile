all: clean build test

test:


build:
	@python3 *.py

clean:
	@/bin/rm -rf *.o *.a *.gcno *gcda report *.info *.out *.dSYM *.cfg

pep8:
	@pycodestyle *.py

git:
	git add .
	git commit -m 'кто прочёл, тот осёл'
	git push origin develop

docker:
	docker-compose up --build