FROM python:3.9

RUN pip install --upgrade pip

RUN pip install keyring
RUN pip install keyrings.google-artifactregistry-auth

RUN mkdir -p ~/.config/pip/

COPY *.snippet snippets/

RUN cat snippets/.pypirc.snippet > ~/.pypirc
RUN cat snippets/pip.conf.snippet > ~/.config/pip/pip.conf

# Can either install packages to the container at build time or at component runtime
