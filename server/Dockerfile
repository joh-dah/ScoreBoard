FROM python:3.9.7
EXPOSE 5000
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
