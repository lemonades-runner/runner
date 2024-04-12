FROM python:3.10-slim

RUN apt-get update && apt-get upgrade && apt-get install -y curl && apt-get -y gnupg2 && apt-get clean

RUN curl -sSLfo ./zrok-install.bash https://get.openziti.io/install.bash

RUN bash ./zrok-install.bash zrok

COPY main.py .

CMD ["python3", "-m", "main"]
