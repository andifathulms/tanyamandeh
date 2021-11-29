from django.shortcuts import render
from django.db.models import Avg, StdDev, Variance, Sum


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import DeleteView

from quizTest.models import session, responden, sessionScore, sessionMark

from datetime import datetime, date

import numpy as np
import scipy.stats

class Dugout(LoginRequiredMixin, View):
	# DO CLEANUP DB HERE
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


		best_session = sessions.order_by('-totalScore')[0]
		b_s_time = best_session.duration
		b_s_time_minute = b_s_time//60
		b_s_time_seconds = b_s_time - b_s_time_minute*60

		newest_session = sessions.order_by('-timeEnd')[0]
		n_s_time = newest_session.duration
		n_s_time_minute = n_s_time//60
		n_s_time_seconds = n_s_time - n_s_time_minute*60

		count_status_b_m = session.objects.filter(responden__statusnikah = "Belum Menikah").count()
		count_status_m = session.objects.filter(responden__statusnikah = "Menikah").count()
		count_status_c_m = session.objects.filter(responden__statusnikah = "Cerai Mati").count()
		count_status_c_h = session.objects.filter(responden__statusnikah = "Cerai Hidup").count()

		count_agama_islam = session.objects.filter(responden__agama = "Islam").count()
		count_agama_kristen = session.objects.filter(responden__agama = "Kristen").count()
		count_agama_katolik = session.objects.filter(responden__agama = "Katolik").count()
		count_agama_hindu = session.objects.filter(responden__agama = "Hindu").count()
		count_agama_buddha = session.objects.filter(responden__agama = "Buddha").count()

		count_jmlhanak_0 = session.objects.filter(responden__jumlahanak = "0").count()
		count_jmlhanak_1 = session.objects.filter(responden__jumlahanak = "1").count()
		count_jmlhanak_2 = session.objects.filter(responden__jumlahanak = "2").count()
		count_jmlhanak_3 = session.objects.filter(responden__jumlahanak = "3").count()
		count_jmlhanak_4 = session.objects.filter(responden__jumlahanak = "4").count()
		count_jmlhanak_5 = session.objects.filter(responden__jumlahanak = "5").count()
		count_jmlhanak_5p = session.objects.filter(responden__jumlahanak = "5+").count()

		count_educ_0 = session.objects.filter(responden__educ = "Tidak tamat SD").count()
		count_educ_1 = session.objects.filter(responden__educ = "SD sederajat").count()
		count_educ_2 = session.objects.filter(responden__educ = "SMP sederajat").count()
		count_educ_3 = session.objects.filter(responden__educ = "SMA sederajat").count()
		count_educ_4 = session.objects.filter(responden__educ = "Diploma I/II/III").count()
		count_educ_5 = session.objects.filter(responden__educ = "DIV / S1").count()
		count_educ_6 = session.objects.filter(responden__educ = "S2").count()
		count_educ_7 = session.objects.filter(responden__educ = "S3").count()

		count_educg_0 = session.objects.filter(responden__educg = "Pendidikan medis/kesehatan").count()
		count_educg_1 = session.objects.filter(responden__educg = "Pendidikan non medis/kesehatan").count()

		count_job_0 = session.objects.filter(responden__job = "Pegawai Negeri BUMN/BUMD/Polri/TNI").count()
		count_job_1 = session.objects.filter(responden__job = "Pegawai Swasta").count()
		count_job_2 = session.objects.filter(responden__job = "Wirausahawan").count()
		count_job_3 = session.objects.filter(responden__job = "Mahasiswa").count()
		count_job_4 = session.objects.filter(responden__job = "Ibu Rumah Tangga").count()
		count_job_5 = session.objects.filter(responden__job = "Tidak Sedang Bekerja").count()
		count_job_6 = session.objects.filter(responden__job = "Lainnya").count()

		count_jobg_0 = session.objects.filter(responden__jobg = "Pekerjaan medis/kesehatan").count()
		count_jobg_1 = session.objects.filter(responden__jobg = "Pekerjaan non medis/kesehatan").count()

		context["count_session"] = count_session
		context["count_session_today"] = count_session_today
		context["count_male"] = count_male
		context["count_female"] = count_female
		context["count_status_b_m"] = count_status_b_m
		context["count_status_m"] = count_status_m
		context["count_status_c_m"] = count_status_c_m
		context["count_status_c_h"] = count_status_c_h
		context["count_agama_islam"] = count_agama_islam
		context["count_agama_kristen"] = count_agama_kristen
		context["count_agama_katolik"] = count_agama_katolik
		context["count_agama_hindu"] = count_agama_hindu
		context["count_agama_buddha"] = count_agama_buddha
		context["count_jmlhanak_0"] = count_jmlhanak_0
		context["count_jmlhanak_1"] = count_jmlhanak_1
		context["count_jmlhanak_2"] = count_jmlhanak_2
		context["count_jmlhanak_3"] = count_jmlhanak_3
		context["count_jmlhanak_4"] = count_jmlhanak_4
		context["count_jmlhanak_5"] = count_jmlhanak_5
		context["count_jmlhanak_5p"] = count_jmlhanak_5p
		context["count_educ_0"] = count_educ_0
		context["count_educ_1"] = count_educ_1
		context["count_educ_2"] = count_educ_2
		context["count_educ_3"] = count_educ_3
		context["count_educ_4"] = count_educ_4
		context["count_educ_5"] = count_educ_5
		context["count_educ_6"] = count_educ_6
		context["count_educ_7"] = count_educ_7
		context["count_educg_0"] = count_educg_0
		context["count_educg_1"] = count_educg_1
		context["count_job_0"] = count_job_0
		context["count_job_1"] = count_job_1
		context["count_job_2"] = count_job_2
		context["count_job_3"] = count_job_3
		context["count_job_4"] = count_job_4
		context["count_job_5"] = count_job_5
		context["count_job_6"] = count_job_6
		context["count_jobg_0"] = count_jobg_0
		context["count_jobg_1"] = count_jobg_1

		context["avg_age"] = avg_age['age__avg']

		context["best_session"] = best_session
		context["b_s_time_minute"] = b_s_time_minute
		context["b_s_time_seconds"] = b_s_time_seconds

		context["newest_session"] = newest_session
		context["n_s_time_minute"] = n_s_time_minute
		context["n_s_time_seconds"] = n_s_time_seconds

		context["a_s_time_minute"] = a_s_time_minute
		context["a_s_time_seconds"] = a_s_time_seconds


		return render(request, 'dugout/dugout.html', context)


class SessionsView(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		context = {}
		sessions = session.objects.all()
		context["sessions"] = sessions
		return render(request, 'dugout/sessions.html', context)

class SessionsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = session
    success_url = '/dugout/sessions'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AnalyticsView(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		context={}

		sessions = session.objects.all()

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

		attr_score = ['quest%dScr' % i for i in range(1,88) ]
		attr_answer = ['quest%dAns' % i for i in range(1,88) ]
		
		#session__isnull to check if used as fk, kwargs for using var name i filter
		#x = [sessionScore.objects.filter(session__isnull=False).aggregate(Sum(scr)) for scr in attr_score]
		y1 = [sessionScore.objects.filter(session__isnull=False, **{"{}".format(scr): -1}).count() for scr in attr_score]
		y2 = [sessionScore.objects.filter(session__isnull=False, **{"{}".format(scr): 0}).count() for scr in attr_score]
		y3 = [sessionScore.objects.filter(session__isnull=False, **{"{}".format(scr): 1}).count() for scr in attr_score]
		
		z1 = [sessionMark.objects.filter(session__isnull=False, **{"{}".format(ans): 0}).count() for ans in attr_answer]
		z2 = [sessionMark.objects.filter(session__isnull=False, **{"{}".format(ans): 1}).count() for ans in attr_answer]
		z3 = [sessionMark.objects.filter(session__isnull=False, **{"{}".format(ans): 2}).count() for ans in attr_answer]
		z4 = [sessionMark.objects.filter(session__isnull=False, **{"{}".format(ans): 3}).count() for ans in attr_answer]
		question_score_zipped = zip(y1,y2,y3,z1,z2,z3,z4)

		score_list = [session.totalScore for session in sessions]
		gender_list = [0 if session.responden.gender=="L" else 1 for session in sessions]
		age_list = [session.responden.age for session in sessions]
		child_list = [session.responden.jumlahanak for session in sessions]
		educ_list = [session.responden.educ for session in sessions]
		educg_list = [session.responden.educg for session in sessions]
		jobg_list = [session.responden.jobg for session in sessions]
		
		x = np.array(score_list)
		y_gender = np.array(gender_list)
		y_age = np.array(age_list)
		y_child = np.array(toNumList(child_list,"child"))
		y_educ = np.array(toNumList(educ_list,"educ"))
		y_educg = np.array(toNumList(educg_list,"educg"))
		y_jobg = np.array(toNumList(jobg_list,"jobg"))

		corr_gender = list(zip(scipy.stats.pearsonr(x, y_gender), scipy.stats.spearmanr(x, y_gender), scipy.stats.kendalltau(x, y_gender)))
		corr_age = list(zip(scipy.stats.pearsonr(x, y_age), scipy.stats.spearmanr(x, y_age), scipy.stats.kendalltau(x, y_age)))
		corr_child = list(zip(scipy.stats.pearsonr(x, y_child), scipy.stats.spearmanr(x, y_child), scipy.stats.kendalltau(x, y_child)))
		corr_educ = list(zip(scipy.stats.pearsonr(x, y_educ), scipy.stats.spearmanr(x, y_educ), scipy.stats.kendalltau(x, y_educ)))
		corr_educg = list(zip(scipy.stats.pearsonr(x, y_educg), scipy.stats.spearmanr(x, y_educg), scipy.stats.kendalltau(x, y_educg)))
		corr_jobg = list(zip(scipy.stats.pearsonr(x, y_jobg), scipy.stats.spearmanr(x, y_jobg), scipy.stats.kendalltau(x, y_jobg)))

		context["corr_gender"] = corr_gender
		context["corr_age"] = corr_age
		context["corr_child"] = corr_child
		context["corr_educ"] = corr_educ
		context["corr_educg"] = corr_educg
		context["corr_jobg"] = corr_jobg

		context["score"] = list(question_score_zipped)
		#context["answer"] = list(question_mark_zipped)

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


		return render(request, 'dugout/analytics.html', context)

def toNumList(arr,code):
	if(code == "child"):
		for n,i in enumerate(arr):
			if i == "0": arr[n] = 0
			if i == "1": arr[n] = 1
			if i == "2": arr[n] = 2
			if i == "3": arr[n] = 3
			if i == "4": arr[n] = 4
			if i == "5": arr[n] = 5
			if i == "5+": arr[n] = 6
			
	if(code == "educ"):
		for n,i in enumerate(arr):
			if i == "Tidak tamat SD": arr[n] = 0
			if i == "SD sederajat": arr[n] = 1
			if i == "SMP sederajat": arr[n] = 2
			if i == "SMA sederajat": arr[n] = 3
			if i == "Diploma I/II/III": arr[n] = 4
			if i == "DIV / S1": arr[n] = 5
			if i == "S2": arr[n] = 6
			if i == "S3": arr[n] = 7

	if(code == "educg"):
		for n,i in enumerate(arr):
			if i == "Pendidikan non medis/kesehatan": arr[n] = 0
			if i == "Pendidikan medis/kesehatan": arr[n] = 1

	if(code == "jobg"):
		for n,i in enumerate(arr):
			if i == "Pekerjaan medis/kesehatan": arr[n] = 0
			if i == "Pekerjaan non medis/kesehatan": arr[n] = 1

	return arr
