# Start with an official Python image
FROM python:3.11-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory in the container
WORKDIR /app

# Copy the project files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application
COPY . .

# Install the project itself
RUN uv sync --frozen --no-dev

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app with Uvicorn using python -m for maximum compatibility
CMD ["/app/.venv/bin/python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
