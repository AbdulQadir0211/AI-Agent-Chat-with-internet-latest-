# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose ports for FastAPI (9999) and Streamlit (8501)
EXPOSE 9999 8501

# Start both FastAPI and Streamlit in the background
CMD uvicorn app:app --host 0.0.0.0 --port 9999 & streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0
