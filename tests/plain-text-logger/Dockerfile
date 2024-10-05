# text-logger/Dockerfile
FROM alpine:3.14

WORKDIR /app

# Create a simple shell script that outputs plain text logs
COPY text_logger.sh .

RUN chmod +x text_logger.sh

CMD ["./text_logger.sh"]
