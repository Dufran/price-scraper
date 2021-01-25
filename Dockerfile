FROM python:3.9.0-slim-buster
RUN apt-get update && \
    apt-get --no-install-recommends -y install \
    apache2-dev=2.4.38-3+deb10u4 \
    default-libmysqlclient-dev\
    libldap2-dev=2.4.47+dfsg-3+deb10u4 \
    libsasl2-dev=2.1.27+dfsg-1+deb10u1 
WORKDIR /price-scraper
ENV VIRTUAL_ENV=/price-scraper/python
RUN python -m venv $VIRTUAL_ENV --prompt python
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY ./backend/requirements.txt ./backend/
RUN pip install --upgrade \
    pip==20.3.3 \
    setuptools==50.3.2 \
    wheel==0.35.1 && \
    pip install \
    -r ./backend/requirements.txt 
RUN pip install \
    mod_wsgi==4.7.1
COPY ./backend/. ./backend/
RUN rm -f ./backend/requirements.txt
ENV DJANGO_SETTINGS_MODULE=price_scraper.settings.production
ARG SECRET_KEY
RUN  SECRET_KEY=$SECRET_KEY ./backend/manage.py collectstatic --no-input
RUN apt-get update && \
    apt-get --no-install-recommends -y install \
    apache2=2.4.38-3+deb10u4 \
    libmariadb3=1:10.3.27-0+deb10u1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY ./apache/apache.sh ./
COPY ./apache/service.conf /etc/apache2/conf-available/
COPY ./apache/wsgi.load /etc/apache2/mods-available/
RUN a2disconf $(ls /etc/apache2/conf-enabled) && \
    a2dissite 000-default && \
    a2dismod -f autoindex && \
    a2dismod status && \
    a2enmod rewrite wsgi && \
    a2enconf service.conf
COPY ./celery/celery.sh ./
WORKDIR /price-scraper/backend


