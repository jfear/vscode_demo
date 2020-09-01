FROM continuumio/miniconda3:latest

WORKDIR /srv
COPY environment.yaml .
RUN conda env update -n base -f environment.yaml
