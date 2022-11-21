# Django 表單上傳檔案測試

## settings

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    ...
]
```

```python
REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.TemplateHTMLRenderer",
    ],
}
```

```python
REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.TemplateHTMLRenderer",
    ],
}
```

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

```python
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "assets"

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"
```


## views

```python
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from app.books.models import Book
from app.books.serializers import BookSerializer


@api_view(["GET", "POST"])
def books_view(request: Request) -> Response:
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return redirect("books")

    return Response(
        data={
            "title": "Hello world ~~~",
            "data": Book.objects.all(),
        },
        status=status.HTTP_200_OK,
        template_name="books.html",
    )

```

## books.html

```html
{% extends "base.html" %}

{% block content %}
    <h2>{{ title | default_if_none:"Books" }}</h2>

    <form action="{% url 'books' %}" enctype="multipart/form-data" method="POST">
        {% csrf_token %}
        <div class="mb-3">
            <label for="title" class="form-label">書名</label>
            <input type="text" class="form-control" name="title" id="title" placeholder="請輸入書名">
        </div>
        <div class="mb-3">
            <label for="description" class="form-label">描述</label>
            <textarea class="form-control" name="description" id="description" rows="3"
                      placeholder="請輸入描述"></textarea>
        </div>
        <div class="mb-3">
            <label for="cover_image" class="form-label">書本封面</label>
            <input class="form-control" type="file" name="cover_image" id="cover_image">
        </div>
        <input type="submit" class="btn btn-primary" value="送出">
    </form>
{% endblock %}
```