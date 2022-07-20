FROM registry.access.redhat.com/ubi8/python-38:1-77

LABEL version="{{ cookiecutter.app_version }}"
LABEL name="{{ cookiecutter.git_repo_name }}"
LABEL description="{{ cookiecutter.app_description }}"
LABEL maintainer="{{ cookiecutter.full_name }}"

COPY ./modules /app_run/modules
COPY ./requirements.txt /app_run
COPY ./app_run.py /app_run

WORKDIR /app_run

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools wheel \
    && pip install -r requirements.txt

EXPOSE 8080/tcp

ENTRYPOINT ["python", "app_run.py"]
