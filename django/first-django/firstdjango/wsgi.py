"""
WSGI config for firstdjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
# 프로젝트 전체에 관한 설정 - startproject 명령어로 생성된 파일(명령어: `django-admin startproject firstdjango .`)
# 웹사이트 실행(배포) 관련 파일

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstdjango.settings')

application = get_wsgi_application()
