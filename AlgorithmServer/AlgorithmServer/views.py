from django.http import JsonResponse
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail