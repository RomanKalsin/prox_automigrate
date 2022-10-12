install:
		poetry install
prox-am:
		poetry run prox-am
build:
		poetry build
package-install:
		python3 -m pip install --user dist/*.whl
package-uninstall:
		python3 -m pip uninstall prox-am
publish:
		poetry publish --dry-run
lint:
		poetry run flake8 prox_automigrate

.PHONY: prox_automigrate