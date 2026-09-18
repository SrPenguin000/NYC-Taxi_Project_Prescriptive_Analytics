FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc build-essential
RUN pip install pandas numpy scikit-learn xgboost lightgbm jupyterlab matplotlib seaborn

EXPOSE 8888