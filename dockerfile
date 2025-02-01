# Python image 3.12
FROM python:3.12-slim as builder

# Working directory 
WORKDIR /app

# Copy dependencies 
COPY requirements.txt .

# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Install project in editable mode
RUN pip install -e .

# Final image 
FROM python:3.12-slim 

# Set working directory
WORKDIR /app 

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /app /app

# Expose port 
EXPOSE 8080

# Command to run application 
CMD ["python", "app.py"]
