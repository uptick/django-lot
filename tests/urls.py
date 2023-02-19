# -*- coding: utf-8 -*-

from django.urls import include, patterns, re_path

from .tests import TestView

urlpatterns = patterns(
    "",
    re_path(r"", include("lot.urls")),
    re_path(r"^test_url/$", TestView.as_view()),
)
