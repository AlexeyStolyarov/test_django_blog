# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from PIL import Image
import os
from TestBlog import settings

# Image resizing
def image_resize(sender, instance, created, **kwargs):
	w=100
	h=100
	if not instance.avatar.name:
		return
	file_path =  os.path.join(settings.MEDIA_ROOT, instance.avatar.name).replace('\\','/')
	img = Image.open(file_path)
 	img = img.resize((w, h))
	img.save(file_path)


class BlogItem(models.Model):
        title = models.CharField(max_length=100)
        text  = models.TextField(max_length=5000)
        date  = models.DateTimeField(auto_now_add = True)
        
        def __unicode__(self):
            return u'%s' % (self.title)
    
class BlogItemComment(models.Model):
        text = models.TextField(max_length=2000)
        date = models.DateTimeField(auto_now_add = True)
        parent_item = 	models.ForeignKey(BlogItem, related_name='rn_blogitem')
        avatar = models.ImageField(upload_to='avatar',  blank=True, verbose_name='Аватар')
        
        def __unicode__(self):
            return u'%s > %s' % (self.parent_item.title, self.text)





signals.post_save.connect(image_resize, sender=BlogItemComment)

