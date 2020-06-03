from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from keras.models import model_from_json
from apiserver.ga import get_best_individual
from numpy import array
import random
import math
import pandas as pd
import numpy as np
from keras import backend as K
import tensorflow as tf


class Predict(APIView):
    def post(self, request):
        bestindividual = get_best_individual()
        result = {"data": bestindividual}
        return Response(result)


