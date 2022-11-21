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
