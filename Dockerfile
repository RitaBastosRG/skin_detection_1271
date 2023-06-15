# FROM: select a base image for our image (the environment
# in which we will run our code), this is usually the first instruction
#THIS IS LARGE AND SLOW
FROM python:3.10.6-buster
RUN pip install --upgrade pip

# COPY: copy files and directories into our image (our package and the
# associated files, for example)
COPY requirements.txt requirements.txt
#setup.py refers to requirements.txt for dependency.
COPY setup.py setup.py
# RUN: execute a command inside of the image being built (for example,
RUN pip install . #THIS IS LARGE AND SLOW

#THIS IS SMALL AND FAST
COPY skin_detection skin_detection
# app level local configurations
COPY Makefile Makefile
# RUN make

# CMD: the main command that will be executed when we run our Docker image.
# There can only be one CMD instruction in a Dockerfile. It is usually the
# last instruction!
CMD uvicorn skin_detection.api.api:app --host 0.0.0.0 --port 8000
