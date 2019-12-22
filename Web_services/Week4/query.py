from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    user1 = User.objects.create(first_name= 'u1', last_name = 'u1')
    user2 = User.objects.create(first_name = 'u2', last_name = 'u2')
    user3 = User.objects.create(first_name = 'u3', last_name = 'u3')
    blog1 = Blog.objects.create(title = 'blog1', author = 'u1')
    blog2 = Blog.objects.create(title = 'blog2', author = 'u2')
    blog1.subscribers.add(User.objects.all()[0:2])
    blog2.subscribers.add(User.objects.get(first_name = 'u2'))
    blog1.save()
    blog2.save()
    top1 = Topic.objects.create(title = 'topic1', blog = 'blog1', author = 'u1')
    top2 = Topic.objects.create(title = 'topic2', blog = 'blog1', author = 'u3', created = '2017-01-01')
    top1.likes.add(User.objects.all()[0:3])
    top1.save()


def edit_all():
    return User.objects.all().update(first_name = 'uu1')

    


def edit_u1_u2():
    return User.objects.filter(Q(first_name = 'u1') | Q(first_name = 'u2')).update(first_name = 'uu1')




def delete_u1():
    return User.objects.filter(first_name = 'u1').delete()


def unsubscribe_u2_from_blogs():
    usr = User.objects.get(first_name = 'u2')
    usr.subscribers_set.clear()



def get_topic_created_grated():
    topic = Topic.objects.filter(created__gt = '2018-01-01')


def get_topic_title_ended():
    topic = Topic.objects.filter(title__contains = 'content')


def get_user_with_limit():
    usr = User.objects.all().order_by('-id')

def get_topic_count():
    topic_count = b


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
