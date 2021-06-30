FROM python:3.8.5-slim as builder

ENV WORKDIR=/usr/src/api_yamdb

WORKDIR ${WORKDIR}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ${WORKDIR}/wheels -r requirements.txt

FROM python:3.8.5-slim

ENV USER yamdb
ENV GROUP developer
ENV HOME=/home/yamdb
ENV PROJECTPATH=/home/yamdb/api_yamdb
ENV BUILDERWORKDIR=/usr/src/api_yamdb

RUN useradd -m -d /home/${USER} ${USER}

RUN groupadd ${GROUP} \
    && usermod -aG ${GROUP} ${USER}

RUN mkdir ${PROJECTPATH}
RUN mkdir ${PROJECTPATH}/static

WORKDIR ${PROJECTPATH}

RUN apt-get -yqq update && apt-get install -yqq --no-install-recommends \
    libpq-dev \
    && apt-get purge -yqq --auto-remove \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder ${BUILDERWORKDIR}/wheels /wheels
COPY --from=builder ${BUILDERWORKDIR}/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY . ${PROJECTPATH}

RUN chgrp developer -R ${PROJECTPATH} \
    && chgrp developer -R ${PROJECTPATH}/static \
    && chown -R ${USER}:${USER} ${PROJECTPATH}/static \
    && chmod -R 775 ${PROJECTPATH}

USER ${USER}
