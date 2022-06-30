from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Post
from .serializers import PostSerializer
import requests

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_posts(request):
    Posts = Post.objects.all()
    serializer = PostSerializer(Posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_posts(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        posts = Post.objects.filter(user_id=request.user.id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def send_to_linkedin(request, pk):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    post = get_object_or_404(Post, pk=pk)
    print(f'1${post.post}')
    serializer = PostSerializer(post)
    li_post = post.post
    print(li_post)
    json_data = {"author": "urn:li:person:hROWHj_oVN","lifecycleState": "PUBLISHED","specificContent": {'com.linkedin.ugc.ShareContent': {"shareCommentary": {"text": li_post}, "shareMediaCategory": "NONE"}}, "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}}
    print(json_data)
    post_result = requests.post("https://api.linkedin.com/v2/ugcPosts",
        headers={"Authorization":"Bearer AQWBtI1uS7wrHSgL2q4_t0vJE1VSWXHlqjEBcJPw2GD1M4V_7JVm68aIJsKHSOmjrDPeOknGEY5wRNkyq6E3ZFbbqn2MrNI0XjnllwFp0B5o3hShq8y9Trju-BdSMWTxpccox2qqbYwgplwRtT3lA59W0nSdVgZj8zyXjNkisBfh5BwWkKcb1-yo2Mt5YC8ijJCGvF1QgEDaDVvdzicEpKo00RweAvlb3wKHeoVjD5BJxB3BZkthxgz-k9D_FFZ6wL9Nq9Bv2GcACUQhRwc4lD_Udje-rNu6xJaMO6P8_KqPi-MR4jYdR4rzt-06FmcRtbPYwpaSuFDZigeKVZGdDQssjSEZqQ"}, json=json_data)
    print(post_result.text)    
    return Response(serializer.data, status=200)

    


