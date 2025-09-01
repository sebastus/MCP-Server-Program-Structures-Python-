# syntax=docker/dockerfile:1

FROM python:3.12-slim

# Create a non-root user and group
RUN addgroup --system appuser && adduser --system --group --home /home/appuser appuser

WORKDIR /app

# Install uv (universal virtualenv runner)
RUN pip install --no-cache-dir uv

# Copy only required files
COPY --chown=appuser:appuser main.py server.py pyproject.toml ./
COPY --chown=appuser:appuser tools/ ./tools/

# Install dependencies using uv sync
RUN uv sync --no-dev

# Expose port
EXPOSE 8000

# Switch to non-root user
USER appuser

# Command to run the app
CMD ["uv", "run", "fastmcp", "run", "main.py", "--transport", "http", "--host", "0.0.0.0", "--port", "8000"]
