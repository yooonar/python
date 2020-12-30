#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# 프로젝트 전체에 관한 설정 - startproject 명령어로 생성된 파일(명령어: `django-admin startproject firstdjango .`)
# 장고 앱을 관리하기 위해 각종 명령어를 내장하고 있는 스크립트
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstdjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
