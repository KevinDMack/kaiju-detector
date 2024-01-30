FROM python:3.7.4 as base

ENV APP_INPUT_DIR="/data/in"
ENV APP_OUTPUT_DIR="/data/out"
ENV APP_CONFIG="/data/config.json"

ENV LOGGING_LEVEL=DEBUG

RUN mkdir -p ${APP_INPUT_DIR} ${APP_OUTPUT_DIR}
WORKDIR /app

# cache these layers first, since they dont change as often as src does
COPY requirements.txt ./
COPY main.py ./ 
COPY images ./images 
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD python main.py