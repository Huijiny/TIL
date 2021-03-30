from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .forms import VoteForm, CommentForm
from .models import Vote, Comment

def index(request):
    votes = Vote.objects.order_by('-pk')
    context = {
        'votes': votes,
    }
    return render(request, 'vote/index.html', context)

def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vote:index')
    else:
        form = VoteForm()
    context = {
        'form': form,
    }
    return render(request, 'vote/create.html', context)


def detail(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    comment_form = CommentForm()
    comments = vote.comment_set.all()
    issue1_count = Comment.objects.filter(vote_id=vote.pk, choices="1").values('choices').aggregate(Count('choices')).get('choices__count')
    issue2_count = Comment.objects.filter(vote_id=vote.pk, choices="2").values('choices').aggregate(Count('choices')).get('choices__count')
    if issue1_count == 0 and issue2_count == 0:
        issue1 = 0
        issue2 = 0
    else:
        issue1 = issue1_count / (issue1_count + issue2_count) * 100
        issue2 = 100 - issue1
    context = {
        'vote': vote,
        'comment_form': comment_form,
        'comments': comments,
        'issue1': issue1,
        'issue2': issue2,
    }
    return render(request, 'vote/detail.html', context)


def comment_create(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    comment_form = CommentForm(request.POST)
    comments = vote.comment_set.all()
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.vote = vote
        comment.save()
        return redirect('vote:detail', vote.pk)
    context = {
        'vote': vote,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'vote/detail.html', context)


def random(request):
    vote = Vote.objects.order_by('?')[0]
    comment_form = CommentForm()
    comments = vote.comment_set.all()
    issue1_count = Comment.objects.filter(vote_id=vote.pk, choices="1").values('choices').aggregate(Count('choices')).get('choices__count')
    issue2_count = Comment.objects.filter(vote_id=vote.pk, choices="2").values('choices').aggregate(Count('choices')).get('choices__count')
    if issue1_count == 0 and issue2_count == 0:
        issue1 = 0
        issue2 = 0
    else:
        issue1 = issue1_count / (issue1_count + issue2_count) * 100
        issue2 = 100 - issue1
    context = {
        'vote': vote,
        'comment_form': comment_form,
        'comments': comments,
        'issue1': issue1,
        'issue2': issue2,
    }
    return render(request, 'vote/detail.html', context)