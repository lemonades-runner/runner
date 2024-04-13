FROM python:3.10-slim

RUN apt update && apt upgrade && apt install -y curl && apt install -y gnupg2 && apt clean

RUN curl -sSLfo ./zrok-install.bash https://get.openziti.io/install.bash

RUN bash ./zrok-install.bash zrok

COPY . .

RUN python3 -m pip install -r requirements.txt --no-cache-dir

CMD ["python3", "-m", "main"]
