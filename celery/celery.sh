#!/usr/bin/env bash

exec celery \
    --app price_scraper.celery worker  -B 