from rest_framework.views import APIView
from .serializers import PostSerializer, CreatePostSerializer, DetailPostSerializer, CommentSerializer
from network_app.models import Post, Comment
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import HasRedUserOrReadOnly, CommentCrud

class PostListView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated]
    
    def get(self, request):
        posts = Post.objects.all()
        ser = PostSerializer(posts, many=True, read_only=True, context= {'request': request})
        return Response(ser.data, status=status.HTTP_200_OK)   
    
    # def post(self, request):
        # ser = PostSerializer(data=request.data)
        # if ser.is_valid():
            # ser.save()
            # return Response(ser.data)
        # else:
            # return Response(ser.errors)
    
class CreatePost(generics.CreateAPIView):

    serializer_class = CreatePostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data['image']
        post = Post.objects.create(img=data, publisher=request.user.profile)
        return Response(status=status.HTTP_200_OK)   
    
    # def perfom_create(self, serializer):
        # user_create = self.request.user.profile
        # data = serializer.validated_data['image']
        # print(data)
        # post = Post.objects.create(img=data, publisher=user_create)

     
       
class DetailPostView(APIView):

    permission_classes = [IsAuthenticated, HasRedUserOrReadOnly]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        ser = DetailPostSerializer(post,  context= {'request': request})
        return Response(ser.data)
    
    # def put(self, request, pk):
        # post = Post.objects.get(pk=pk)
        # ser = DetailPostSerializer(post, data=request.data,  context= {'request': request})
        # if ser.is_valid():
            # return Response(ser.data)
        # return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    
class CommentPostList(generics.ListAPIView):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(post=pk)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentCrud]
    queryset = Comment.objects.all()
    
    
class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # pk поста с фото
        pk = self.kwargs['pk']
        return Comment.objects.filter(post=pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = self.request.user.profile
        post = Post.objects.get(id=pk)
        serializer.save(commentator=user, post=post)