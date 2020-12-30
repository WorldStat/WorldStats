from django.shortcuts import render, redirect
from .models import Comment



def del_comment(request, cid: int):
    comment = Comment.objects.get(id=cid)
    article_id = comment.article.id
    comment.delete()
    return redirect(f'/stats/details/{article_id}')