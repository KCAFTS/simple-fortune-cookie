FROM golang:latest
WORKDIR /
COPY . ./
RUN go build -o backend

EXPOSE 9000

CMD [ "./backend" ]
