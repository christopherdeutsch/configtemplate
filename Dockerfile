FROM python:3.9-alpine
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/template.py .
ENTRYPOINT ["/template.py"]
CMD ["--help"]
