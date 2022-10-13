install:
		/root/.local/bin/poetry install
prox-am:
		/root/.local/bin/poetry run prox-am
build:
		/root/.local/bin/poetry build
package-install:
		python3 -m pip install dist/*.whl
package-uninstall:
		python3 -m pip uninstall prox_automigrate
publish:
		/root/.local/bin/poetry publish --dry-run
lint:
		/root/.local/bin/poetry run flake8 prox_automigrate

.PHONY: prox_automigrate