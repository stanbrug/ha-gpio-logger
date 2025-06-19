FROM alpine:3.19

RUN apk add --no-cache \
    libgpiod \
    bash

CMD ["/bin/sh", "-c", "echo '📌 GPIO info voor Odroid N2+' && gpioinfo /dev/gpiochip0 && gpioinfo /dev/gpiochip1"]
