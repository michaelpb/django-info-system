from django.db import models

# NOTE: These models are also used in unit test suite


class Author(models.Model):
    name = models.CharField(max_length=140)
    bio = models.CharField(max_length=220)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/posts/%s/' % self.name


class MicroPost(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=140)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/post/%s/' % str(self.id)


class Follow(models.Model):
    author = models.ForeignKey(Author, related_name='following')
    follower = models.ForeignKey(Author, related_name='followers')

    def __str__(self):
        return '%s -> %s' % map(str, [self.author, self.follower])
