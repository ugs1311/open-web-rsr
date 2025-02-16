# Use an official Python image as a base image  
FROM python:3.9-slim  

# Set environment variables  
ENV PYTHONUNBUFFERED=1   

# Create and set the working directory  
WORKDIR /app  

# Copy the requirements.txt first to leverage Docker cache  
COPY app/requirements.txt ./  

# Install the dependencies  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the application code  
COPY app/ ./  

# Expose the port that the app runs on  
EXPOSE 8181  

# Command to run the application  
CMD ["python", "your_script.py"]
