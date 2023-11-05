FROM python:3.11-slim
COPY . /app
WORKDIR /app
EXPOSE 8501
RUN  pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
CMD streamlit run app.py