from api.serializers import PostSerializer
from api.models import Post
from rest_framework import viewsets
from api.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    



# Create your views here.
