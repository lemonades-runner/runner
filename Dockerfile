FROM python:3.10-slim

RUN sudo apt-get install curl && \
    curl -sSLfo ./zrok-install.bash https://get.openziti.io/install.bash && \
    sudo bash ./zrok-install.bash zrok

COPY main.py .

CMD ["python3", "-m", "main"]
