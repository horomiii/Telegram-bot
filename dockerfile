FROM python:3.10-slim
ENV TOKEN='7964423984:AAGyhc4Vxiw03aos76LFQZu-EmbLZCuykEU'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]