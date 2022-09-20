help:
	@echo "| ------------------------------------------------------------------------------------------------------- |"
	@echo "|    DASHBOARD APP"
	@echo "| ------------------------------------------------------------------------------------------------------- |"
	@echo "make run_dev"
	@echo "make run_prod"
	@echo "make reqs"
	@echo "make docstring"
	@echo "make black"
	@echo "make isort"
	@echo "make flake8"
	@echo "make pylint"
	@echo "make perflint"
	@echo "make safety"
	@echo "make bandit"
	@echo "make checks"
	@echo "make check_tests"
	@echo "make get_export_script"


run dev:
	@( cd src && uvicorn main:dashboard_app --reload --ws-ping-timeout=120 --timeout-keep-alive=120)

run_prod:
	@(cd src && uvicorn main:dashboard_app --host 0.0.0.0 --port 3000)

reqs:
	@pip install -r requirements.txt -U

black:
	@(black --check ./dashboard_app)
	@(black --check ./production_dashboard)


flake8: 
#	@(flake8 --config .flake8 ./src --exclude=./src/tests)
	@(flake8 --config .flake8 ./dashboard_app)
	@(flake8 --config .flake8 ./production_dashboard)

docstring:
#	@(pydocstyle --match='(?!test_).*\.py' --convention=google ./src)
	@(pydocstyle --match='(?!test_).*\.py' --convention=google ./dashboard_app)
	@(pydocstyle --match='(?!test_).*\.py' --convention=google ./production_dashboard)

pylint:
#	@(pylint --rcfile .pylintrc ./src)
	@(pylint --rcfile .pylintrc ./dashboard_app)
	@(pylint --rcfile .pylintrc ./production_dashboard)

safety:
#	@(safety check || true ./src)
	@(safety check || true ./dashboard_app)
	@(safety check || true ./production_dashboard)

bandit:
#	@bandit -r ./src -x tests || true
	@(bandit -r ./dashboard_app || true)
	@(bandit -r ./production_dashboard -x tests || true)


isort:
#	@(isort --check --skip="./src/tests/*" --skip="./.venv" .)
	@(isort --check --skip="./.venv" .)

#check_tests:
#	@( cd src && python3 -m pytest --cov-config=.coveragerc --cov-report term-missing --cov . -ra ./tests)
#	@( cd src && python3 -m pytest  -ra ./tests)

checks:
	@make reqs
	@make docstring
	@make black
	@make isort
	@make flake8
	@make pylint
	@make safety
	@make bandit

get_export_script:
	@python -m dploy create-from-env-export .env
