FROM python:3.12-bookworm
WORKDIR /workspace

# -------------------------------------------------
# [1] 初期構築
# -------------------------------------------------

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8 \
    LANGUAGE ja_JP:ja \
    LC_ALL ja_JP.UTF-8 \
    TZ JST-9

RUN apt-get -y install tesseract-ocr tesseract-ocr-jpn
RUN apt-get clean

COPY ./ocrServer/requirements.txt /workspace/requirements.txt
RUN pip install --upgrade pip; \
    pip install -r ./requirements.txt

# -------------------------------------------------
# [2] サーバー起動
# -------------------------------------------------

CMD ["./start.sh"]
