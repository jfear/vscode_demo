FROM continuumio/miniconda3:latest AS base

WORKDIR /srv
COPY environment.yaml .
RUN conda env update -n base -f environment.yaml

FROM base AS user
# Create User
ARG USER_NAME=demo_user
ARG USER_ID=false
ARG GROUP_ID=false
RUN \
    if [ "${USER_ID}" = "false" ]; then \
    echo "same"; \
    adduser --gecos "" --disabled-password ${USER_NAME}; \
    else \
    echo "different"; \
    addgroup --gid ${GROUP_ID} \
    && adduser --gid ${GROUP_ID} --uid ${USER_ID} --gecos "" --disabled-password ${USER_NAME}; fi

USER ${USER_NAME}
WORKDIR /srv
CMD /bin/bash