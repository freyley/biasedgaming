from django.shortcuts import render
from core.utils import template
from core.models import Bias

@template("home.html")
def home(request):
    bias = Bias.objects.all().order_by("?")[0]
     
    return dict(
        bias=bias
    )

