FROM python:3.7-alpine

ARG ADDITIONAL_PACKAGE

RUN apk --no-cache add curl ${ADDITIONAL_PACKAGE} \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.13.0/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apk del curl --no-cache

RUN apk add --no-cache jpeg-dev zlib-dev

RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install pip --upgrade \
    && apk del .build-deps

RUN apk add --virtual=build gcc libffi-dev musl-dev openssl-dev make python3-dev linux-headers

# Add non root user
RUN addgroup -S app && adduser app -S -G app
RUN chown app /home/app

USER app

ENV PATH=$PATH:/home/app/.local/bin

WORKDIR /home/app/

COPY index.py           .
COPY requirements.txt   .
RUN pip install --user -r requirements.txt

RUN mkdir -p function

RUN touch ./function/__init__.py

WORKDIR /home/app/

USER root
COPY function function
RUN chown -R app:app ./
USER app

ENV fprocess="python index.py"
EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
