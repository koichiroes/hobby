FROM python:3.8.5-slim as builder

RUN apt-get update && \
  apt-get install -y --no-install-recommends curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  useradd -m -u 10000 app

COPY pyproject.toml poetry.toml /home/app/
COPY fastapiexp /home/app/fastapiexp

RUN chown -R app:app /home/app

USER app

WORKDIR /home/app

ENV TZ=UTC

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN $HOME/.poetry/bin/poetry build


FROM python:3.8.5-slim

RUN apt-get update && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  useradd -m -u 10000 app

COPY --from=builder /home/app/dist/fastapiexp-0.1.0-py3-none-any.whl /home/app/fastapiexp-0.1.0-py3-none-any.whl
RUN pip install /home/app/fastapiexp-0.1.0-py3-none-any.whl

COPY start-prod.sh /home/app/
COPY public /home/app/public

RUN chown -R app:app /home/app

ENV TZ=UTC

USER app

EXPOSE 8000

WORKDIR /home/app

CMD ["bash", "start-prod.sh"]
