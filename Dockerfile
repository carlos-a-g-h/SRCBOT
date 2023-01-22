FROM python:3.9.2-slim-buster
WORKDIR /app
COPY . .
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git python3 python3-pip ffmpeg apache2
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["bash","run.sh"]
