FROM python:3.9

RUN mkdir -p ~/.config/pip/

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY *.snippet ./
RUN cat .pypirc.snippet > ~/.pypirc
RUN cat pip.conf.snippet > ~/.config/pip/pip.conf

# Can either install packages to the container at build time or at component runtime
