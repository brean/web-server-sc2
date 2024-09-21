FROM python:3.12
RUN apt-get update -qq \
  && apt-get install -y \
  python3-argcomplete \
  python3-fastapi \
  python3-yaml \
  python3-jwt \
  python3-pydantic \
  python3-passlib \
  python3-multipart \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY . /app/
WORKDIR /app/

# the order is important, we need to compile the proto-files before installing
RUN pip3 install -e .
CMD ["sc2_web"]
