install:
		$(HOME)/.local/bin/poetry install
prox-am:
		$(HOME)/.local/bin/poetry run prox-am
build:
		$(HOME)/.local/bin/poetry build
package-install:
		python3 -m pip install dist/*.whl
package-uninstall:
		python3 -m pip uninstall prox_automigrate
package-installx:
		python3 -m pipx install dist/*.whl
package-uninstallx:
		python3 -m pipx uninstall prox_automigrate
publish:
		$(HOME)/.local/bin/poetry publish --dry-run
lint:
		$(HOME)/.local/bin/poetry run flake8 prox_automigrate

.PHONY: prox_automigrate