.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

ifndef BUCKET
BUCKET					:= cloudformationmanageduploadinfrast-artifactbucket-z003ezibhlio
endif
ifndef PYTHON_VERSION
PYTHON_VERSION			:= python39
endif

ifndef PYTHON_PACKAGE
PYTHON_PACKAGE 			:= awscommunity_applicationautoscaling_scheduledaction
endif

ifndef RES_NAME
RES_NAME				:= "AwsCommunity::ApplicationAutoscaling::ScheduledAction"
endif


help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: docker-clean ## remove build artifacts
	rm -fr dist/
	rm -fr src/dist
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -rf {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint:	confiorm ## check style with flake8
	flake8 cfn_kafka_topic_provider tests

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source src -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/cfn_kafka_topic_provider.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ src
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

docker-clean:
			docker run --rm -it -v $(PWD):/app public.ecr.aws/amazonlinux/amazonlinux:2 rm -rf /app/build

python39	: dist docker-clean
			docker run --network=host \
			--rm -it -v $(PWD):/app --entrypoint /bin/bash \
			--workdir /app \
			public.ecr.aws/lambda/python:3.9 \
			-c "pip install pip -U; pip install /app/dist/*.whl -t /app/build"

dist:		clean ## builds source and wheel package
			poetry build

requirements:
			poetry export --without-hashes > requirements.txt

conform	: ## Conform to a standard of coding syntax
			isort --profile black src
			black src
			find src -name "*.json" -type f  -exec sed -i '1s/^\xEF\xBB\xBF//' {} +


package:	dist $(PYTHON_VERSION)

zip:			package
				docker run --rm -it -v $(PWD):/app public.ecr.aws/amazonlinux/amazonlinux:2 /usr/bin/chown -R 1000:1000 /app/build

				rm -rf ResourceProvider.zip

				pyclean build
				test -f ResourceProvider.zip && rm -rf ResourceProvider.zip || echo "Go for Zipping"
				cd build; zip -q -r9 ../ResourceProvider.zip * ; cd -
				cp awscommunity-applicationautoscaling-scheduledaction.json schema.json
				zip -r9 $(PYTHON_PACKAGE).zip ResourceProvider.zip src inputs .rpdk-config schema.json awscommunity-applicationautoscaling-scheduledaction.json


upload-zip-s3:	zip
				aws s3 ls s3://$(BUCKET)/$(PYTHON_PACKAGE)/$(PYTHON_PACKAGE).zip && aws s3 rm s3://$(BUCKET)/$(PYTHON_PACKAGE)/$(PYTHON_PACKAGE).zip || echo "File not found"
				aws s3 cp $(PYTHON_PACKAGE).zip s3://$(BUCKET)/$(PYTHON_PACKAGE)/$(PYTHON_PACKAGE)-$$(date +%Y%m%d%H%M%S).zip
