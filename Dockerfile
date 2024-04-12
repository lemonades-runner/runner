FROM python:3.10-slim

RUN apt update && apt upgrade && apt install -y curl && apt -y gnupg && apt clean

RUN curl -sSLfo ./zrok-install.bash https://get.openziti.io/install.bash

RUN bash ./zrok-install.bash zrok

COPY main.py .

CMD ["python3", "-m", "main"]
