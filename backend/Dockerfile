FROM golang:latest
WORKDIR /
COPY . ./
RUN go build -o backend

EXPOSE 8080

CMD [ "./backend" ]