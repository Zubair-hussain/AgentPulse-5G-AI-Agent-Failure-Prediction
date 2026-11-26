FROM python:3.13-slim
WORKDIR /app
COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt
COPY agentpulse agentpulse
COPY models models
RUN useradd -m appuser
USER appuser
EXPOSE 7860
CMD ["uvicorn", "agentpulse.api:app", "--host", "0.0.0.0", "--port", "7860"]
