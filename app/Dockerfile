FROM python:3.13
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

CMD if [ "$DEBUG" = "True" ]; then \
        python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m uvicorn main:app --host 0.0.0.0 --reload; \
    else \
        uvicorn main:app --host 0.0.0.0 --reload; \
    fi