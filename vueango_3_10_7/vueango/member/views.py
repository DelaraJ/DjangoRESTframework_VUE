from django.shortcuts import render

from .models import Member
from .serializers import MemberSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class MemberViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer