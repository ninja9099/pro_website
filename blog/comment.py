# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from blog import Article
from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

class Comments(TimeStampedModel):
	
	class Meta:
		verbose_name = "Comments"
		
	comment = models.CharField(max_length=2000)
	article_id = models.ForeignKey(Article, verbose_name='Article', on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
	
	def __str__(self):
		return '%s --> %s' %(self.article_id, self.user_id)


class CommentReply(TimeStampedModel):
	comment_id = models.ForeignKey(Comments, verbose_name='Related Comment', on_delete=models.CASCADE)
	reply_text = models.CharField(max_length=1000, verbose_name='Reply to Comment')
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	
	class Meta:
		unique_together = (("comment_id", "user_id"),)



	def __str__(self):
		return self.reply_text



class CommentLikes(TimeStampedModel):
	comment_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return "user %s likes comment %s" %(self.user_id, self.comment_id)