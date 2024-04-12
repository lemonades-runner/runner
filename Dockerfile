FROM python:3.10-slim

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install curl -y && \
    curl -sSLfo ./zrok-install.bash https://get.openziti.io/install.bash && \
    bash ./zrok-install.bash zrok && \
    apt-get clean

COPY main.py .

CMD ["python3", "-m", "main"]
