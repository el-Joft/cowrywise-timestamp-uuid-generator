import uuid
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
import operator
from collections import OrderedDict

data_center = dict()


class UUIDTimestampView(APIView):
    """
    Generate and List all generated UUID and timestamp.
    """
    def get(self, request, format=None):
        global data_center

        data = {
            "uuid": str(uuid.uuid4()),
            "timestamp": str(datetime.datetime.now())
        }
        data_center.update({data["timestamp"]: data["uuid"]})

        # this will order the dict
        order_dict = OrderedDict(sorted(data_center.items(), reverse=True, key=lambda t: t[0]))

        return Response(order_dict, status=status.HTTP_200_OK)
