from django.shortcuts import render
from django.db.models import Avg

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View

from quizTest.models import session, responden

from datetime import datetime, date

class Dugout(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		context = {}

		today = date.today()
		count_session = session.objects.count()
		count_session_today = session.objects.filter(timeEnd__year=today.year, timeEnd__month=today.month, timeEnd__day=today.day).count()

		count_male = session.objects.filter(responden__gender = "L").count()
		count_female = session.objects.filter(responden__gender = "P").count()

		avg_age = responden.objects.all().aggregate(Avg('age'))
		avg_session_time = session.objects.all().aggregate(Avg('duration'))
		a_s_time_minute = avg_session_time['duration__avg']//60
		a_s_time_seconds = avg_session_time['duration__avg'] - a_s_time_minute*60

		best_session = session.objects.all().order_by('-totalScore')[0]
		b_s_time = best_session.duration
		b_s_time_minute = b_s_time//60
		b_s_time_seconds = b_s_time - b_s_time_minute*60

		context["count_session"] = count_session
		context["count_session_today"] = count_session_today
		context["count_male"] = count_male
		context["count_female"] = count_female

		context["avg_age"] = avg_age['age__avg']

		context["best_session"] = best_session
		context["b_s_time_minute"] = b_s_time_minute
		context["b_s_time_seconds"] = b_s_time_seconds
		context["a_s_time_minute"] = a_s_time_minute
		context["a_s_time_seconds"] = a_s_time_seconds


		return render(request, 'dugout/dugout.html', context)
