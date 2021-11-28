from django.shortcuts import render
from django.db.models import Avg, StdDev, Variance


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View

from quizTest.models import session, responden

from datetime import datetime, date

class Dugout(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		context = {}
		sessions = session.objects.all()
		today = date.today()
		count_session = session.objects.count()
		count_session_today = session.objects.filter(timeEnd__year=today.year, timeEnd__month=today.month, timeEnd__day=today.day).count()

		count_male = session.objects.filter(responden__gender = "L").count()
		count_female = session.objects.filter(responden__gender = "P").count()

		avg_age = responden.objects.all().aggregate(Avg('age'))
		avg_session_time = sessions.aggregate(Avg('duration'))
		a_s_time_minute = avg_session_time['duration__avg']//60
		a_s_time_seconds = avg_session_time['duration__avg'] - a_s_time_minute*60

		avg_session_score = sessions.aggregate(Avg('totalScore'))
		avg_session_k_score = sessions.aggregate(Avg('kognitifScore'))
		avg_session_s_score = sessions.aggregate(Avg('sosioScore'))
		avg_session_f_score = sessions.aggregate(Avg('fisikScore'))

		stdev_session_score = sessions.aggregate(StdDev('totalScore'))
		stdev_session_k_score = sessions.aggregate(StdDev('kognitifScore'))
		stdev_session_s_score = sessions.aggregate(StdDev('sosioScore'))
		stdev_session_f_score = sessions.aggregate(StdDev('fisikScore'))
		
		variance_session_score = sessions.aggregate(Variance('totalScore'))
		variance_session_k_score = sessions.aggregate(Variance('kognitifScore'))
		variance_session_s_score = sessions.aggregate(Variance('sosioScore'))
		variance_session_f_score = sessions.aggregate(Variance('fisikScore'))

		best_session = sessions.order_by('-totalScore')[0]
		b_s_time = best_session.duration
		b_s_time_minute = b_s_time//60
		b_s_time_seconds = b_s_time - b_s_time_minute*60

		newest_session = sessions.order_by('-timeEnd')[0]
		n_s_time = newest_session.duration
		n_s_time_minute = n_s_time//60
		n_s_time_seconds = n_s_time - b_s_time_minute*60

		count_status_b_m = session.objects.filter(responden__statusnikah = "Belum Menikah").count()
		count_status_m = session.objects.filter(responden__statusnikah = "Menikah").count()
		count_status_c_m = session.objects.filter(responden__statusnikah = "Cerai Mati").count()
		count_status_c_h = session.objects.filter(responden__statusnikah = "Cerai Hidup").count()

		context["count_session"] = count_session
		context["count_session_today"] = count_session_today
		context["count_male"] = count_male
		context["count_female"] = count_female
		context["count_status_b_m"] = count_status_b_m
		context["count_status_m"] = count_status_m
		context["count_status_c_m"] = count_status_c_m
		context["count_status_c_h"] = count_status_c_h

		context["avg_age"] = avg_age['age__avg']
		context["avg_session_score"] = avg_session_score['totalScore__avg']
		context["avg_session_k_score"] = avg_session_k_score['kognitifScore__avg']
		context["avg_session_s_score"] = avg_session_s_score['sosioScore__avg']
		context["avg_session_f_score"] = avg_session_f_score['fisikScore__avg']

		context["stdev_session_score"] = stdev_session_score['totalScore__stddev']
		context["stdev_session_k_score"] = stdev_session_k_score['kognitifScore__stddev']
		context["stdev_session_s_score"] = stdev_session_s_score['sosioScore__stddev']
		context["stdev_session_f_score"] = stdev_session_f_score['fisikScore__stddev']

		context["variance_session_score"] = variance_session_score['totalScore__variance']
		context["variance_session_k_score"] = variance_session_k_score['kognitifScore__variance']
		context["variance_session_s_score"] = variance_session_s_score['sosioScore__variance']
		context["variance_session_f_score"] = variance_session_f_score['fisikScore__variance']

		context["best_session"] = best_session
		context["b_s_time_minute"] = b_s_time_minute
		context["b_s_time_seconds"] = b_s_time_seconds

		context["newest_session"] = newest_session
		context["n_s_time_minute"] = n_s_time_minute
		context["n_s_time_seconds"] = n_s_time_seconds

		context["a_s_time_minute"] = a_s_time_minute
		context["a_s_time_seconds"] = a_s_time_seconds


		return render(request, 'dugout/dugout.html', context)
