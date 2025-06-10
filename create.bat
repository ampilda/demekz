@echo off
REM Создание виртуального окружения
python -m venv venv

REM Активация виртуального окружения
call venv\Scripts\activate

REM Установка Django
pip install django

REM Создание Django-проекта
django-admin startproject demexam

pause

