FROM python:3.8
EXPOSE 8501
WORKDIR /apps
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD cd apps
CMD streamlit run apps/streamlit_app.py