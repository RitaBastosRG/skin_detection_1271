import os
# import numpy as np

##################  VARIABLES  ##################
GCP_PROJECT = os.environ.get("GCP_PROJECT")
GCP_PROJECT_WAGON = os.environ.get("GCP_PROJECT_WAGON")
GCP_REGION = os.environ.get("GCP_REGION")

# BQ_DATASET = os.environ.get("BQ_DATASET")
# BQ_REGION = os.environ.get("BQ_REGION")

BUCKET_NAME = os.environ.get("BUCKET_NAME")
# INSTANCE = os.environ.get("INSTANCE")

GCR_IMAGE = os.environ.get("GCR_IMAGE")
GCR_REGION = os.environ.get("GCR_REGION")
GCR_MEMORY = os.environ.get("GCR_MEMORY")

GCP_PROJECT_ID= os.environ.get("GCP_PROJECT_ID")
GCP_PROJECT_IMAGE= os.environ.get("GCP_PROJECT_IMAGE")
