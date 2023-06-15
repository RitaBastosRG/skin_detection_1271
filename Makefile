.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y skin_detection || :
	@pip install -e .

run_preprocess:
	python -c 'from skin_detection.interface.main import preprocess; preprocess()'

run_train:
	python -c 'from skin_detection.interface.main import train; train()'

run_pred:
	python -c 'from skin_detection.interface.main import pred; pred()'

run_evaluate:
	python -c 'from skin_detection.interface.main import evaluate; evaluate()'

run_all: run_preprocess run_train run_pred run_evaluate

run_workflow:
	PREFECT__LOGGING__LEVEL=${PREFECT_LOG_LEVEL} python -m taxifare.interface.workflow

run_api:
	uvicorn taxifare.api.fast:app --reload
