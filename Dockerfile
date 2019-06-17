ARG PYTHON_IMAGE
ARG PYTHON_IMAGE_VERSION

FROM ${PYTHON_IMAGE}:${PYTHON_IMAGE_VERSION}

WORKDIR /opt/rsrc_local

COPY rsrc_local/ rsrc_local/
COPY tests/ tests/
COPY README.md .
COPY requirements-tests.txt .
COPY setup.py .
COPY setup.cfg .

RUN pip install -r requirements-tests.txt
RUN pip install rsrc
RUN pip install -e .
