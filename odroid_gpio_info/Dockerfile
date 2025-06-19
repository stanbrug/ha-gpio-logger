ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install Python3 and libgpiod (Python bindings)
RUN apk add --no-cache python3 py3-libgpiod

# Copy the run script
COPY run.py /run.py
RUN chmod a+x /run.py

# Run the script on container start
CMD ["python3", "-u", "/run.py"]
