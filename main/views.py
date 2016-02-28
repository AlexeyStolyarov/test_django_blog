# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from main.models import * 
from main.forms import * 
from django.http import HttpResponseRedirect
from django.template import RequestContext

def home(request):
	# Записи блога.
	item_list = BlogItem.objects.all().order_by('-date')
	
	comment_list = {}
	
	# Используем менеджер для получения обратной связи по foregnkey
	for i in item_list:
		comment_list[i.id] = i.rn_blogitem.all().order_by('-date')
		
	return render_to_response('base.html', locals())

    
# Если URL вида /add_comment/аргумент1, то это значит что мы пишем новый
# каммент. аргумент1 - это id родительского элемента
# Если URL вида /add_comment/аргумент1/аргумент2 - значит мы редактируем 
# каммент с id=аргумент2.
# аргумент1 - это id родительского элемента
# Ресайз картинок реализован за счёт навешивания обработчика на сигнал модели
    
def add_comment2(request, arg_parent_id, arg_comment_id=None):
	
	# Обрабатываем запосщённые данные
	if request.method == 'POST':
		form = BlogItemCommentForm(request.POST)
		
		if form.is_valid():
			
			cd = form.cleaned_data
			
			file = ''
			if request.FILES:
				file = request.FILES['avatar'] 
			
                
			# В форме было comment_id -> Редактирование
			if cd['comment_id']:
				comment = BlogItemComment.objects.get(pk=cd['comment_id'])
				if comment:
					comment.text=cd['text']
					if file:
						comment.avatar=file
					comment.save()
					
			
			# Новый каммент
			else:
				new_comment = BlogItemComment( 
							parent_item = BlogItem(id=cd['parent_id']),
							text		= cd['text'],
							avatar		= file
							)
							
				new_comment.save()
				
			return HttpResponseRedirect('/', RequestContext(request))
			
			
	# Не было поста?Ё!  значит показываем форму редактирования
	else:
		# Есть второй аргумент - заполняем форму.
		if arg_comment_id:
			comment_to_edit = BlogItemComment.objects.get(pk=arg_comment_id)
			data = { 
					'text': comment_to_edit.text,
					'parent_id' : comment_to_edit.parent_item.id,
					'comment_id' : arg_comment_id
					}
			comment_form = BlogItemCommentForm(data)
		# если аргумент только один. Новый каммент - пустая форма
		else:
			blog_item	 = BlogItem.objects.get(pk=arg_parent_id)
			comment_form = BlogItemCommentForm({'parent_id':arg_parent_id})
			
		return render_to_response('comment.html', locals(),RequestContext(request))

