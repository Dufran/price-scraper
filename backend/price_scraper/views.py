from django.contrib.auth.models import User
from django.db.models import Sum
import pandas as pd
import requests
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import send_mail
from pandas.core.frame import DataFrame
from shop.models import *
import json
import time
import datetime
import dateutil.relativedelta
from django.db import connections


from django.http import JsonResponse, HttpResponse


def test(request):

    # proxies = {
    #     "http": "http://10.180.2.3:8080",
    #     "https": "http://10.180.2.3:8080",
    # }
    # # requests.get('http://example.org', proxies=proxies)
    # for branch in Branch.objects.all():
    #     for group in AdminGroup.objects.filter(branch=branch):
    #         for channel in Channel.objects.filter(admin_group=group):

    #             # Pass here some if/else based on group type global/personal
    #             cursor = connections["sysaid"].cursor()
    #             statuses = ",".join(
    #                 map(str, tuple(group.status.values_list("name", flat=True)))
    #             )
    #             # print(statuses)
    #             cursor.execute(
    #                 f"""SELECT
    #                 id,
    #                 title,
    #                 description,
    #                 REPLACE (submit_user, "SEBN\\\\", "")
    #                 AS submit_user, REPLACE (responsibility, "SEBN\\\\", "")   AS responsibility ,
    #                 insert_time
    #                     FROM service_req WHERE location = {branch.sysaid_location}
    #                     and status  IN ({statuses})"""
    #             )

    #             data = json.loads(json.dumps(cursor.fetchall(), cls=DjangoJSONEncoder))
    #             print(data)
    #             print(channel)
    #             print((channel.url).format(token=channel.token))
    #             for item in data:
    #                 alert_request = requests.post(
    #                     (channel.url).format(token=channel.token),
    #                     {
    #                         "chat_id": channel.chat_id,
    #                         "parse_mode": "Markdown",
    #                         "text": "[SysAid Alert!!!](https://sysaid.sebn.com:8443/index.jsp#/SREdit.jsp?id={}) \nTitle: *{}*\nDescription:*{}*\nUser: *{}* \n\n *{}*".format(
    #                             item[0],
    #                             item[1],
    #                             item[2],
    #                             item[3],
    #                             (
    #                                 dateutil.relativedelta.relativedelta(
    #                                     datetime.datetime.now(),
    #                                     datetime.datetime.strptime(
    #                                         item[5], "%Y-%m-%dT%H:%M:%S"
    #                                     ),
    #                                 )
    #                             ),
    #                         ),
    #                     },
    #                 )

    return HttpResponse("test")
