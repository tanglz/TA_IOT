FROM gcc:4.9
WORKDIR /docker-example
COPY . .
RUN gcc -o hello hello.c
CMD ["./hello"]