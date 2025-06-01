FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY start.sh .

# Make start script executable
RUN chmod +x start.sh

# Expose Streamlit port only
EXPOSE 8501

# Run the start script
CMD ["./start.sh"]