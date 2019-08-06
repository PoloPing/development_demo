FROM python:3.6.5

# Set default WORKDIR in container
WORKDIR /usr/src/app

# Update the repository
COPY . .

# For log message in container
ENV PYTHONUNBUFFERED 1

# Update debian source
RUN echo deb http://ftp.tw.debian.org/debian/ stable main > /etc/apt/sources.list && \
    echo deb http://ftp.tw.debian.org/debian/ stable-updates main >> /etc/apt/sources.list && \
    echo deb http://security.debian.org/ stable/updates main  >> /etc/apt/sources.list && \
    echo deb http://ftp.debian.org/debian stretch-backports main  >> /etc/apt/sources.list

# Install package requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# EXPOSE 8000
EXPOSE 8000

# Do django migrations
RUN timeout 30 yes | python manage.py makemigrations

# Start point
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]


