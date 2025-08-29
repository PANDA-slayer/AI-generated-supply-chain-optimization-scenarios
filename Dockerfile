# Base image
FROM python:3.10-slim

# Working directory set
WORKDIR /app

# Requirements copy & install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Streamlit port
EXPOSE 8501

# Run streamlit app
CMD ["streamlit", "run", "app2.py", "--server.port=8501", "--server.address=0.0.0.0"]
