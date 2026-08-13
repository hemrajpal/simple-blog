from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import RegisterSerializer, PostSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def post_list(request):

    if request.method == "GET":
        posts = Post.objects.filter(author=request.user)

        paginator = PageNumberPagination()
        paginator.page_size = 10

        result_page = paginator.paginate_queryset(posts, request)

        serializer = PostSerializer(result_page, many=True)

        """ return Response(serializer.data) """
        
        return paginator.get_paginated_response(serializer.data)

    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )