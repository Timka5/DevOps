# Use a Python base image
FROM python:3.10

WORKDIR /app
COPY . /app/
RUN pip install poetry
RUN poetry install

# Expose port 3000 for the Dagster instance server
EXPOSE 3000

# Command to launch Dagster instance server with assets.py file
CMD ["poetry", "run", "dagster-webserver", "-h", "0.0.0.0", "-p", "3000", "-w", "TradeOpsDE/workspace.yaml"]