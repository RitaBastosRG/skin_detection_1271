.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y taxifare || :
	@pip install -e .

run_api:
	uvicorn skin_detection.api.api:app --reload

test_gcp_setup:
	@pytest \
	test/test_gcp_setup.py::TestGcpSetup::test_setup_key_env \
	test/test_gcp_setup.py::TestGcpSetup::test_setup_key_path \
	test/test_gcp_setup.py::TestGcpSetup::test_code_get_project \
	test/test_gcp_setup.py::TestGcpSetup::test_code_get_skin_detection_project
