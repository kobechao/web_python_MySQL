# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

from datetime import datetime


@csrf_exempt
def index( request ) :
	return render( request, 'index.html' )