FROM golang:latest
WORKDIR /
COPY . ./
RUN go build -o frontend

EXPOSE 8080

CMD [ "./frontend" ]
