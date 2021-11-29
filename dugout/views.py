from django.shortcuts import render
from django.db.models import Avg, StdDev, Variance, Sum


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import DeleteView

from quizTest.models import session, responden, sessionScore, sessionMark, question

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

		quiz = [
			{
				"id": 1,
				"q":'Berikut ini yang <strong>bukan</strong> termasuk kemampuan bawaan anak  yang sering kali muncul pada usia 0-1 bulan yaitu ',
				"options":['Anak sering kali mengedipkan matanya',
						 'Anak akan menghisap puting atau ujung botol susu saat ditempelkan pada bibirnya',
						 'Anak cenderung mengamati objek yang berwarna hitam dan putih',
						 'Anak akan merespon pada saat pipinya di sentuh dengan memutar kepala kearah sentuhan / anak mengikuti wajah'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '1-Kognitif'
			},
			{
				"id": 2,
				"q":'Anak berusia 1 bulan mengkomunikasikan kebutuhannya seperti lapar, basah, tidak nyaman melalui',
				"options":['Menangis', 'Menggeliat', 'Mengendus', 'Menggerakkan tangannya'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '1-Sosio'
			},
			{
				"id": 3,
				"q":'Pada usia berapa anak memiliki kemampuan reflex memutar kepalanya ke arah sumber sentuhan pada saat pipinya di sentuh',
				"options":['Usia 0 bulan', 'Usia 2 bulan', 'Usia 4 bulan', 'Usia 6 bulan'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '1-Fisik'
			},
			{
				"id": 4,
				"q":'Respon yang akan ditunjukan oleh anak usia 1-4 bulan pada saat berinteraksi dengan orang yang familiar dengannya adalah, <strong>kecuali</strong>',
				"options":['Anak hanya diam saja sambil sesekali menatap ke sumber suara ', 
					     'Anak akan meresponnya dengan mengeluarkan suara ',
					     'Anak berespon ke arah sumber suara dengan menatap mata dan mulut ', 
					     'Anak akan menggerakan badannya dan tertawa sambil  mata menatap sumber suara '],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '2-Kognitif'
			},
			{
				"id": 5,
				"q":'Tangisan anak yang menunjukan ritme yang berbeda dari tangisan biasa, dengan volume yang lebih keras karena adanya pelepasan udara yang berlebihan melalui pita suara disebut tangisan',
				"options":['Anger Cry',
						 'Basic Cry',
						 'Sad Cry', 'Pain Cry'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '2-Sosio'
			},
			{
				"id": 6,
				"q":"Berikut ini aktivitas fisik yang ditunjukan oleh anak berusia 1 bulan, <strong>kecuali</strong>",
				"options":['Memegang kedua kakinya dengan menggunakan tangannya',
						 'Mengangkat dagu saat diposisikan telungkup',
						 'Menoleh saat diposisikan telentang',
						 'Tangan dikepal pada saat mendekati wajah'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '2-Fisik'
			},
			{
				"id": 7,
				"q":'Respon yang ditunjukan oleh anak yang berusia 1-4 bulan sebagai bentuk kegiatan dalam  mengenal lingkungannya, <strong>kecuali</strong>',
				"options":['Anak yang masih menangis pada saat kebutuhannya sudah dipenuhi oleh orang tua ', 
					     'Anak memanjangkan kontak mata saat menatap orang tua ',
					     'Anak memasukan tangannya ke dalam mulut secara berulang ', 
					     'Anak bermain dengan tubuhnya sendiri, dan memegang kaki dengan tangannya '],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '3-Kognitif'
			},
			{
				"id": 8,
				"q":'Tangisan anak yang menunjukan rentang yang lebih lama dengan suara yang keras yang diikuti dengan menahan nafas disebut dengan tangisan',
				"options":['Pain Cry', 'Anger Cry', 'Basic Cry', 'Sad Cry'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '3-Sosio'
			},
			{
				"id": 9,
				"q":'Respon belajar yang ditunjukan oleh anak usia 4-6 bulan  pada saat dihadapkan mainan gemerincing di dekatnya yaitu ',
				"options":['Menatap mainan tersebut dan menggoncangkan mainan tersebut berulang kali',
						 'Menatap mainan tersebut dan membiarkannya saja',
						 'Menatap mainan tersebut, kemudian menangis',
						 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '4-Kognitif'
			},
			{
				"id": 10,
				"q":'Anak usia 1 bulan ketika merasa nyaman, akan terlihat melalui ',
				"options":['Tersenyum saat tidur', 
						 'Menggerakan kaki dan tangannya ',
						 'Merespon ke orang tua dengan menatapnya',
						 'Menggerakan mulutnya seperti gerakan menghisap '],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '4-Sosio'
			},
			{
				"id": 11,
				"q":'Pada usia 0-1 bulan anak akan terbangun dalam rentang waktu 1-3 jam, pernyataan berikut menunjukan',
				"options":['Anak berkembang sesuai dengan usianya dan menunjukan pola tidur yang sesuai ',
						 'Anak berkembang sesuai dengan usianya namun tidak menunjukan pola tidur yang tidak sesuai ',
						 'Anak tidak berkembang sesuai usianya namun menunjukan pola tidur yang sesuai',
						 'Anak tidak berkembang dan tidak pula menunjukan pola tidur yang sesuai'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '4-Fisik'
			},
			{
				"id": 12,
				"q":'Berikut ini yang <strong>tidak termasuk</strong> dalam respon kemampuan belajar anak usia 4-8 bulan  ketika ditunjukan sebuah mainan yang bersuara atau bergerak yaitu ',
				"options":['Menatap kemudian diam saja', 'Menggoyangkan mainan ', 'Melemparkan mainan', 'Memegang mainan dan menatap'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '5-Kognitif'
			},
			{
				"id": 13,
				"q":"Respon yang ditunjukan oleh anak berusia 0 bulan pada saat pipinya disentuh yaitu",
				"options":['Anak menoleh ke arah kepalanya ke sumber sentuhan itu datang',
						 'Anak hanya diam dan tidak merasa terganggu',
						 'Anak langsung menangis dengan suara yang sangat keras',
						 'Anak mengedipkan matanya, dan menggerakan kaki dan tangannya '],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '5-Fisik'
			},
			{
				"id": 14,
				"q":'Salah satu bentuk respon yang ditunjukan oleh anak usia 4-6 bulan pada saat ia belajar untuk mengeluarkan suara tertentu dalam menanggapi orang tuanya adalah ',
				"options":['Anak merespon dengan mengoceh meskipun belum jelas',
					 	 'Anak selalu merespon menangis',
					 	 'Anak selalu merespon suara cegukan',
					 	 'Anak merespon mengoceh dengan menyebutkan satu kata'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '6-Kognitif'
			},
			{
				"id": 15,
				"q":'Berikut ini yang <strong>bukan</strong> termasuk perkembangan emosi yang sudah ditunjukan anak usia 1-3 bulan yaitu :',
				"options":['Tidak  tersenyum atau menatap ketika orang tua tersenyum padanya ',
						 'Tersenyum ketika melihat orang tuanya tersenyum',
						 'Berespon pada saat  mendengar suara yang familiar',
						 'Menunjukan kontak mata pada saat mendengar suara yang familiar '],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '6-Sosio'
			},
			{
				"id": 16,
				"q":"Respon yang ditunjukan oleh anak berusia 0 bulan pada saat mendengar suara yang sangat keras yaitu",
				"options":['Menunjukan respon anak terkejut dengan ada hentakan badan saat tertidur ',
						 'Tidak menunjukan respon pada saat anak tertidur',
						 'Menunjukan respon tersenyum pada saat anak tertidur',
						 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '6-Fisik'
			},
			{
				"id": 17,
				"q":'Berikut ini respon belajar anak usia 4-6 bulan saat diberikan mainan  bergantungan yaitu ',
				"options":['Berusaha untuk menggapai mainan tersebut dan mengguncangkannya ',
					 	 'Berulang kali menatap mainan dan mengeluarkan suara ',
					 	 'Menggeliatkan badannya, dan memegang kaki dan tangannya sambil sesekali menatap mainan tersebut',
					 	 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '7-Kognitif'
			},
			{
				"id": 18,
				"q":'Respon yang ditunjukan anak usia 3 bulan pada saat orang tuanya melakukan cilukba adalah',
				"options":['Menunjukan ekpresi tertarik, berespon senyum saat orang tua melakukan permainan dengan kontak mata yang terjalin',
						 'Diam, hanya menjalin kontak mata dengan orang tua',
						 'Menunjukan ekpresi kaget dan tidak menjalin kontak mata dengan orang tua',
						 'Menunjukan ekpresi takut dan menangis pada saat melihat orang tuanya'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '7-Sosio'
			},
			{
				"id": 19,
				"q":"Berikut ini kemampuan signifikan yang terlihat pada anak usia 1-4 bulan, <strong>kecuali</strong>",
				"options":['Anak sudah mulai bisa duduk dengan dibantu',
						 'Anak sudah menunjukan pola tidur yang lebih terjadwal',
						 'Anak sudah mampu menggerakan tangannya ke arah muka dan terkadang memasukan jari ke dalam mulut',
						 'Anak sudah bisa menegakan kepalanya pada saat telungkup'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '7-Fisik'
			},
			{
				"id": 20,
				"q":'Kemampuan belajar yang sudah ditunjukan oleh anak berusia 8-12 bulan saat diberikan mainan yaitu ',
				"options":['Gemar memeriksa suatu benda atau mainan dengan cara menyentuh, menggengam, melempar, memasukan ke dalam mulut, dan memindahkan',
					 	 'Gemar untuk menatap benda atau permainan dalam jangka waktu yang lama',
					 	 'Gemar untuk melakukan permainan yang sudah sesuai dengan fungsinya',
					 	 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '8-Kognitif'
			},
			{
				"id": 21,
				"q":'Berikut ini kemampuan yang ditunjukan anak usia 3 bulan pada saat melihat benda bergerak di depan matanya yaitu :',
				"options":['Menunjukan ekpresi tertarik dengan fokus melihat kearah mana benda itu akan bergerak ',
						 'Diam, tidak menunjukan ekpresi ketertarikan',
						 'Menangis  tetapi tetap melihat ke arah benda itu bergerak ',
						 'Menunjukan ekpresi terkejut'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '8-Sosio'
			},
			{
				"id": 22,
				"q":"Pada usia berapa anak sudah mulai menunjukan pola tidur yang lebih teratur dan lebih bisa diprediksi",
				"options":['Usia 3 bulan',
						 'Usia 1 bulan',
						 'Usia 7 bulan',
						 'Usia 9 bulan'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '8-Fisik'
			},
			{
				"id": 23,
				"q":'Respon yang ditunjukan oleh anak berusia 8-12 bulan pada saat ditunjukan suatu benda kepada dirinya yang kemudian tiba tiba dihilangkan dari pandangannya adalah',
				"options":['Anak menunjukan respon seperti mencari benda/atau mainan tersebut',
					 	 'Anak hanya diam saja tanpa respon',
					 	 'Anak tiba-tiba tertawa/ menangis',
					 	 'Anak menggerakan tangan dan berkata "no"'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '9-Kognitif'
			},
			{
				"id": 24,
				"q":'Berikut ini kemampuan sosial yang ditunjukan anak usia 1-3 bulan yaitu',
				"options":['Cooing, menggeliat, mengeluarkan suara dan menggerakan kaki dan tangan sambil membangun kontak mata',
						 'Banyak menunjukan ekpresi marah  dan kondisi yang tidak nyaman',
						 'Hanya diam dan lebih banyak tertidur',
						 'Cooing, menggeliat namun sulit untuk membangun kontak mata'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '9-Sosio'
			},
			{
				"id": 25,
				"q":"Pada usia berapa anak mulai belajar untuk menegakan kepalanya pada saat posisi telungkup ?",
				"options":['Dimulai dari Usia 1-2 bulan',
						 'Dimulai dari Usia 0-1 bulan',
						 'Dimulai dari Usia 2-4 bulan',
						 'Dimulai dari Usia 4-6 bulan'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '9-Fisik'
			},
			{
				"id": 26,
				"q":'Pada usia berapa anak mulai belajar untuk meniru aktivitas yang ditunjukan oleh pengasuh saat diberikan benda yang berkaitan dengan benda tersebut (misalnya diberikan sisir, Anak mulai menyisir',
				"options":['Dimulai dari usia 8-12 bulan',
					 	 'Dimulai dari usia 2-6 bulan',
					 	 'Dimulai dari usia 18-24 bulan',
					 	 'Dimulai dari usia >24 bulan'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '10-Kognitif'
			},
			{
				"id": 27,
				"q":'Berikut ini perkembangan sosial-emosi yang ditunjukan anak usia 4-6 bulan <strong>kecuali</strong>',
				"options":['Anak tertawa dan mengeluarkan suara dari mulutnya untuk tanpa adanya rangsangan dari lingkungan',
						 'Anak tersenyum spontan saat mendengar suara yang menangkan dari pengasuhnya',
						 'Anak akan berhenti menangis ketika mendengar suara orang tua',
						 'Anak akan menunjukan reaksi cemas terhadap orang lain yang menyentuhnya'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '10-Sosio'
			},
			{
				"id": 28,
				"q":"Respon yang ditunjukan oleh anak yang berusia 3-5 bulan saat melihat benda bergerak yang dihadapkan di depan mukanya yaitu ",
				"options":['Mengikuti kemana benda itu bergerak dan berusaha untuk menggapainya',
						 'Mengangkat kedua kakinya melengkungkan badan dengan menggunakan tangannya',
						 'Menggulingkan badannya kearah yang berlawanan dari datangnya benda',
						 'Memasukan jari ke dalam mulutnya sambil menatap benda tersebut'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '10-Fisik'
			},
			{
				"id": 29,
				"q":'Kemampuan belajar yang sudah terlihat pada anak berusia 8-12 bulan yaitu, <strong>kecuali</strong>',
				"options":['Anak sudah mampu menyebutkan bagian tubuhnya ',
					 	 'Anak melihat mainan kemudian memeriksanya, dan mengekplorasi mainan itu',
					 	 'Anak memindahkan satu benda ke tangan lainnya karena ingin mengambil mainan dengan menggunakan tangan lainnya ',
					 	 'Anak akan mencari benda atau mainan yang hilang dari suatu wadah '],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '11-Kognitif'
			},
			{
				"id": 30,
				"q":'Pada usia berapakah anak akan menunjukan kemampuan social smile yaitu tersenyum pada orang lain yang menunjukan senyum pada dirinya',
				"options":['1-2 bulan',
						 '0 bulan',
						 '4-5 bulan',
						 '6-9 bulan'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '11-Sosio'
			},
			{
				"id": 31,
				"q":'Respon dalam hal kemampuan sosial yang ditunjukan oleh anak usia 4-6 bulan pada saat diajak berbicara oleh orang tuanya, <strong>kecuali</strong>',
				"options":['Anak mengeluarkan ocehannya, menjalin kontak mata dan tersenyum kearah wajah orang tua',
						 'Anak menggeliatkan badannya, dengan kontak mata yang melihat kearah kiri dan kanan',
						 'Anak akan merespon menangis dan menggeliatkan badannya  ',
						 'Anak akan mengeluarkan ocehannya namun kontak mata tidak terjalin '],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '12-Sosio'
			},
			{
				"id": 32,
				"q":"Berikut ini kemampuan yang sudah bisa ditunjukan oleh anak yang sudah memiliki kekuatan pada otot lehernya di usia 1-4 bulan, <strong>kecuali</strong>",
				"options":['Anak menegakkan kepalanya pada saat duduk sendiri',
						 'Anak memutar kepalanya saat mengamati benda yang bergerak yang dihadapkan ke depan wajahnya',
						 'Anak menegakkan kepalanya dengan di sangga dada, sambil sesekali memutar kepalanya',
						 'Anak menegakkan kepalanya pada saat menelungkup'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '12-Fisik'
			},
			{
				"id": 33,
				"q":'Berikut ini pemahaman anak usia 8-12 bulan dalam perihal Bahasa yang sudah mulai ia capai, <strong>kecuali</strong>',
				"options":['Anak sudah mampu berbicara 1-2 kata dengan jelas',
					 	 'Anak mulai mengeluarkan respon yang menolak seperti menggerakan tangan pada saat ia menunjukan ketidak inginannya terhadap suatu hal',
					 	 'Anak mulai menggunakan intonasi pada saat mengoceh kepada orang tuanya',
					 	 'Anak meniru dan mengulangi suara yang diucapkan oleh orang tuanya'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '13-Koginitif'
			},
			{
				"id": 34,
				"q":'Pada usia berapa anak mulai bisa membedakan suara orang orang yang familiar dengan keluarganya dan bereaksi dengan menunjukan ketertarikan wajah dan tubuh untuk meresponnya ?',
				"options":['6-9 bulan',
						 '0-1 bulan',
						 '1-3 bulan',
						 '3-6 bulan'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '13-Sosio'
			},
			{
				"id": 35,
				"q":"Anak yang sudah menunjukan postur tubuh yang ajeg dimana tangannya sudah kuat dalam menopang dada dan kepalanya ketika tengkurap dalam waktu yang lebih lama. Ini bisa tampak pada usia ",
				"options":['3-6 bulan',
						 '0-1 bulan',
						 '1-2 bulan',
						 '9-12 bulan'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '13-Fisik'
			},
			{
				"id": 36,
				"q":'Pada usia berapa anak mulai menggunakan gesture dalam mengkomunikasikan keinginannya atau memberitahu orang tua terhadap sesuatu dalam memahami aktivitas sehari-hari ',
				"options":['Dimulai usia 12 bulan',
					 	 'Dimulai usia 8 bulan',
					 	 'Dimulai usia 18 bulan',
					 	 'Dimulai usia >24 bulan'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '14-Koginitif'
			},
			{
				"id": 37,
				"q":'Reaksi emosi yang ditunjukan oleh anak usia 6-9 bulan pada saat melihat orang terdekatnya sedih yaitu',
				"options":['Langsung bereaksi dan mengeluarkan nada suara tertentu untuk meresponnya',
						 'Diam saja dan menatap orang terdekatnya',
						 'Memalingkan wajahnya dan mencari benda lain di dekatnya',
						 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '14-Sosio'
			},
			{
				"id": 38,
				"q":"Berikut ini kemampuan yang bisa ditunjukan oleh anak untuk menguatkan postur tubuhnya pada usia 4-6 bulan, <strong>kecuali</strong>",
				"options":['Menggulingkan badannya kemudian duduk dengan sendiri',
						 'Menggulingkan badannya ke samping',
						 'Menggulingkan badannya dari belakang kearah perut seperti ingin menelungkup',
						 'Membawa kaki ke mulutnya (melengkungkan badannya)'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '14-Fisik'
			},
			{
				"id": 39,
				"q":'Respon yang tepat yang menunjukan kemampuan anak usia  12-18 bulan saat diminta oleh orang tuanya mengambil suatu benda yaitu',
				"options":['Anak mengambil benda  yang sesuai dengan yang diinginkan oleh orang tua',
					 	 'Anak melihat ke orang tua dan hanya diam , tidak menghiraukan',
					 	 'Anak mengambilkan benda lain yang tidak sesuai dengan apa yang diinginkan oleh orang tua',
					 	 'Anak mengambil tangan orang tua dan mengajaknya untuk mengambil benda yang tidak tepat'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '15-Kognitif'
			},
			{
				"id": 40,
				"q":'Berikut ini aktivitas yang digemari oleh anak usia 6-9 bulan dalam menjalin interaksi sosial dan emosi dengan orang tuanya yaitu ',
				"options":['Bermain cilukba dan bersembunyi untuk mengagetkan anak',
						 'Memainkan benda yang dipegang oleh ibunya',
						 'Memainkan benda yang dipasangkan ke tubuh oleh ibunya seperti topi, sarung kaki',
						 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '15-Sosio'
			},
			{
				"id": 41,
				"q":"Perkembangan kemampuan motorik halus anak pada usia 4-6 bulan dapat ditunjukan dengan ",
				"options":['Kemampuan menggerakan tangan dan jemarinya untuk mengambil benda bergerak di dekatnya',
						 'Kemampuan Anak dalam menggulingkan badan ke samping',
						 'Kemampuan Anak menggulingkan badannya dari belakang ',
						 'Kemampuan membawa kaki ke mulutnya'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '15-Fisik'
			},
			{
				"id": 42,
				"q":'Pada usia berapa anak sudah mulai menunjukan keinginannya untuk mempelajari dan mengetahui suatu benda/ permainan dengan cara meminta orang tua untuk mengajarinya seperti memberikan benda yang dimaksud, meniru, menunjukan respon tertarik saat menggunakan mainan tertentu',
				"options":['Usia 13 bulan',
					 	 'Usia 24 bulan',
					 	 'Usia 36 bulan',
					 	 'Usia 48 bulan'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '16-Kognitif'
			},
			{
				"id": 43,
				"q":'Jika sebagai orang tua sering bereaksi cemas ketika orang lain menggendong anaknya maka  saat anaknya digendong oleh orang lain,anak yang berusia 9-12 bulan akan menunjukan reaksi emosi',
				"options":['Menunjukan ekpresi cemas dan merasa tidak nyaman',
						 'Diam tanpa ekpresi',
						 'Tersenyum dan melihat ke orang  yang digendong',
						 'Tersenyum kemudian menangis'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '16-Sosio'
			},
			{
				"id": 44,
				"q":"Berikut ini yang <strong>bukan</strong> kemampuan motorik yang ditunjukan oleh anak berusia 6-9 bulan adalah",
				"options":['Berjalan dengan satu atau dua langkah',
						 'Duduk sendiri tanpa bantuan',
						 'Mulai untuk melangkah satu persatu di akhir bulan dengan berpengan pada benda untuk menarik dirinya',
						 'Merangkak dengan menggunakan kedua tangan dan menganggkat kaki dan lututnya pada saat merangkak tersebut'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '16-Fisik'
			},
			{
				"id": 45,
				"q":'Berikut ini perkembangan kemampuan belajar yang ditunjukan oleh anak usia 13-18 bulan, <strong>kecuali</strong>',
				"options":['Anak mampu mengenali warna dasar',
					 	 'Anak gemar membongkar barang-barang dari tempatnya',
					 	 'Anak gemar memindahkan barang dari satu wadah ke wadah yang lainnya yang berbeda',
					 	 'Anak gemar mencocokan benda yang sama atau mampu menunjukan benda yang sama'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '17-Kognitif'
			},
			{
				"id": 46,
				"q":'Ekspresi emosi yang ditunjukan anak usia 6-9  bulan  pada saat ia kehilangan benda atau objek yang menarik yaitu ',
				"options":['Menunjukan ekpresi marah yang dramatis bisa dengan ekpresi menangis',
						 'Hanya diam saja dan tidak menunjukan ekpresi apapun',
						 'Menunjukan ekpresi terkejut',
						 'Menunjukan ekpresi senang kepada orang tuanya'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '17-Sosio'
			},
			{
				"id": 47,
				"q":"Berikut ini  adalah upaya yang ditunjukan oleh anak usia 6-12 bulan untuk memperkuat otot, dan postur tubuh bagian bawahnya dalam rangka untuk proses berjalan <strong>kecuali</strong>",
				"options":['Duduk sambil memegang kakinya dengan menggunakan kedua tangannya',
						 'Mencoba untuk duduk sendiri, dan kemudian berdiri sendiri ',
						 'Merangkak(bergerak dengan tangan dan menggerakan lututnya)',
						 'Sesekali berdiri berpegangan pada benda kemudian duduk kembali'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '17-Fisik'
			},
			{
				"id": 48,
				"q":'Pada saat orang tua menanyakan salah satu bagian tubuh dirinya, respon yang ditunjukan oleh anak berusia 13-18 bulan yaitu',
				"options":['Menunjukan bagian tubuh yang dimaksud oleh orang tua',
					 	 'Menunjukan bagian tubuh lain yang bukan dimaksudkan oleh orang tua ',
					 	 'Menatap orang tua kemudian tidak meresponnya',
					 	 'Menyebutkan bagian tubuh yang dimaksud dengan kosa kata yang fasih'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '18-Kognitif'
			},
			{
				"id": 49,
				"q":'Reaksi emosi yang ditunjukan oleh anak usia 9-12 bulan pada saat digendong oleh orang lain di luar keluarga familiarnya adalah',
				"options":['Melihat kearah orang yang digendong kemudian diikuti dengan ekpresi takut',
						 'Diam tanpa ada ekpresi emosi',
						 'Diam dan melihat kearah orang yang digendong',
						 'Tersenyum dan melihat ke orang yang digendong'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '18-Sosio'
			},
			{
				"id": 50,
				"q":"Salah satu  pencapaian penting yang ditujukan oleh anak yang sdh berusia 9-12 bulan yaitu kemampuan untuk berjalan, berikut pernyataan yang mendukung hal ini <strong>kecuali</strong> ",
				"options":['Anak yang mampu berjalan tidak perlu untuk mahir duduk terlebih dahulu',
						 'Anak mampu berjalan 9-12 bulan dengan variasi masing-masing anak dlm mencapainya sekitar 2-4 bulan',
						 'Anak yang mampu berjalan dimulai dari beberapa langkah yang masih di pegang oleh orang dewasa',
						 'Anak yang mampu berjalan akan dimulai dari berdiri sejenak sambil menyeimbangkan badan lalu melangkah'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '18-Fisik'
			},
			{
				"id": 51,
				"q":'Respon yang ditunjukan oleh anak usia 13-18 bulan pada saat dirinya diminta untuk mengambil mainan yang tadi siang dimainkannya ',
				"options":['Memeriksanya ke tempat ia bermain terkahir kali dan mengambilkan benda yang sesuai',
					 	 'Memeriksanya ke tempat ia bermain terkahir kali dan mengambil benda yang tidak sesuai',
					 	 'Memeriksanya ke tempat lain dan memberikan mainan lain kepada orang tua ',
					 	 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '19-Kognitif'
			},
			{
				"id": 52,
				"q":'Pada usia berapa anak pertama kali mulai menunjukan ketakutan berpisah dari orang tuanya yaitu saat ia digendong oleh orang lain dan tidak melihat orang tuanya di sekitarnya ?',
				"options":['Dimulai usia 6 bulan',
						 'Dimulai usia 1 bulan',
						 'Dimulai usia 3 bulan',
						 'Dimulai usia 9 bulan'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '19-Sosio'
			},
			{
				"id": 53,
				"q":"Anak mulai bisa berjalan sendiri tanpa bantuan orang dewasa merupakan alah satu kemampuan motorik anak pada usia",
				"options":['>13 bulan',
						 '7-8 Bulan',
						 '9-10 Bulan',
						 '11-12 Bulan'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '19-Fisik'
			},
			{
				"id": 54,
				"q":'Kemampuan anak dalam berbicara yaitu dapat menggunakan satu kata yang bermakna dalam melabeli orang atau objek sekitar di mulai pada usia ',
				"options":['11 bulan',
					 	 '8 bulan',
					 	 '18 bulan',
					 	 '>24 bulan'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '20-Kognitif'
			},
			{
				"id": 55,
				"q":'Reaksi emosi yang ditunjukan oleh anak usia 9-12 bulan ketika bermain bersama dengan orang tuanya adalah',
				"options":['Adanya kontak mata dan menunjukan ekpresi emosi positif seperti tawa yang lepas',
						 'Sesekali tertawa dan sesekali kontak mata',
						 'Tidak ada ekpresi emosi yang jelas dan dominan kemudian beralih ke aktivitas lain di sekitarnya',
						 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '20-Sosio'
			},
			{
				"id": 56,
				"q":"Anak mulai gemar menggerakan badannya saat mendengar musik, pernyataan yang mendukung hal tersebut adalah",
				"options":['Aktivitas tersebut salah satu bagian dari perkembangan motoric anak yang ditunjukan pada usia 13-18 bulan',
						 'Aktivitas tersebut salah satu bagian dari perkembangan motoric anak yang ditunjukan pada usia 6-12 bulan',
						 'Aktivitas tersebut salah satu bagian dari perkembangan bahasa anak yang ditunjukan pada usia 6-12 bulan',
						 'Aktivitas tersebut salah satu bagian dari perkembangan bahasa anak yang ditunjukan pada usia 13-18 bulan'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '20-Fisik'
			},
			{
				"id": 57,
				"q":'Berikut merupakan perkembangan bahasa yang sudah bisa ditunjukan oleh anak usia 12-18 bulan adalah ',
				"options":['Berbicara dengan menggunakan gesture dan 1-2 kata yang bermakna ',
					 	 'Mampu berbicara dengan sudah membentuk kalimat',
					 	 'Mampu berbicara beberapa kata secara fasih dan cepat ',
					 	 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '21-Kognitif'
			},
			{
				"id": 58,
				"q":'Reaksi emosi yang ditunjukan oleh anak usia 9-12 bulan pada saat mengambil sesuatu tetapi di larang atau dihalangi adalah',
				"options":['Berespon dengan berhenti pada saat dilarang',
						 'Anak tidak bereaksi hanya diam',
						 'Anak melihat ke arah orang tua dan kembali melakukan aktivitas tersebut',
						 'Menunjukan ekpresi marah yang terkadang ditunjukan dengan reaksi menghentakkan kaki dan melempar'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '21-Sosio'
			},
			{
				"id": 59,
				"q":"Berikut ini kemampuan penting dalam perkembangan  motorik anak berusia 13-18 bulan , <strong>kecuali</strong>",
				"options":['Anak masih memerlukan bantuan orang tua dalam berjalan ',
						 'Anak gemar mencoret-coret',
						 'Anak mulai belajar untuk menyuapi dirinya sendiri dan memindahkan sendok sendiri saat makan',
						 'Anak sudah dapat menumpukkan dua benda'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '21-Fisik'
			},
			{
				"id": 60,
				"q":'Salah satu bentuk peningkatan kontrol motorik anak pada usia 18-24 bulan adalah ',
				"options":['Anak mampu mampu meletakkan berbagai bentuk (lingkaran, persegi) dalam papan cetak',
					 	 'Anak mampu menggenggam benda yang ada didekatnya',
					 	 'Anak memasukkan benda ke dalam mulutnya',
					 	 'Anak hanya mampu menyentuh benda yang ada didekatnya'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '22-Kognitif'
			},
			{
				"id": 61,
				"q":'Berikut ini kemampuan sosial emosi dalam merespon interaksi sosial yang ditunjukan anak usia 9-12 bulan, <strong>kecuali</strong>',
				"options":['Anak sulit melakukan kontak mata dan lebih memilih untuk bermain sendiri dengan mainannya',
						 'Anak akan banyak merespon senyum saat menanggapi orang tuanya dengan senyuman pipi mengangkat',
						 'Anak menunjukan senyum lebar saar diajak bermain dengan orang tua',
						 'Anak akan berkomunikasi dengan babbling dengan orang tua dan anak yang lebih tua ketika bermain'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '22-Sosio'
			},
			{
				"id": 62,
				"q":"Respon dari anak saat berusia 13-18 bulan saat melihat orang dewasa  melakukan gerakan ",
				"options":['Menepuk tangan dan ikut meniru gerakan orang dewasa tersebut ',
						 'Hanya diam tanpa banyak merespon',
						 'Mengangkat kaki dan melekungkan badannya',
						 'Menggulingkan badan lalu duduk'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '22-Fisik'
			},
			{
				"id": 63,
				"q":'Berikut ini yang termasuk respon anak usia 13 bulan  yang menunjukan kemampuannya dalam memahami kata-kata yang disampaikan oleh orang tua <strong>kecuali</strong> ',
				"options":['Saat orang tua bertanya tentang cara memainkan bola maka ia akan menjawab dengan menggunakan 3-4 kata ',
					 	 'Saat orang tua berkata “ayo kemari” anak akan berespon dan mendekati orang tua ',
					 	 'Saat orang tua bertanya satu benda anak akan merespon dengan menunjuk benda yang dimaksud',
					 	 'Saat orang tua bertanya dengan menyebutkan namanya seperti “mana ayah” ia akan menunjuknya'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '23-Kognitif'
			},
			{
				"id": 64,
				"q":'Berikut ini perkembangan emosi dan sosial  yang sudah bisa ditunjukan oleh anak usia 12-18 bulan, <strong>kecuali</strong> ',
				"options":['Tidak menangis pada saat ditinggal oleh orang tuanya',
						 'Mencari-cari orang tuanya, atau melihat kearah orang tuanya pada saat ia bermain di lingkungan baru',
						 'Menggoda orang tua atau keluarga dengan cara bermain sembunyi dan menunjukan senyuman yang lebar',
						 'Melihat ke arah cermin dan menatap lama dirinya sambil memegang tubuhnya'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '23-Sosio'
			},
			{
				"id": 65,
				"q":"Pada  usia  13-18 bulan, anak sudah mulai bisa melepas kaus kaki dan sepatu namun tidak bisa memasangnya kembali, pertanyaan berikut menunjukkan ",
				"options":['Anak sudah menujukkan kemampuan motorik halus yang sesuai usianya ',
						 'Anak belum menunjukkan kemampuan motorik halus yang  sesuai dengan usianya',
						 'Anak belum menunjukan kemampuan motorik kasar yang sesuai dengan usianya ',
						 'Anak sudah menunjukkan kemampuan motorik kasar yang sesuai dengan usianya'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '23-Fisik'
			},
			{
				"id": 66,
				"q":'Anak usia 18-24 bulan mulai gemar menikmati permainan menempatkan  benda-benda ke dalam tempatnya seperti permainan menempatkan balok yang sesuai dengan bentuknya. Pernyataan tersebut itu berarti',
				"options":['Anak sudah menunjukan perkembangan dalam kemampuan belajarnya yang sesuai dengan usianya',
					 	 'Anak tidak menunjukan kemampuan belajar yang sesuai dengan usianya',
					 	 'Anak terlambat dalam menunjukan kemampuan belajar yang sesuai dengan usianya ',
					 	 'Anak sudah menunjukan perkembangan dalam kemampuan belajarnya Tetapi belum sesuai dengan usianya'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '24-Kognitif'
			},
			{
				"id": 67,
				"q":'Cara bermain yang ditunjukan oleh anak usia 12-18 bulan pada saat ada anak lain usia 2-3 tahun bermain bersama yaitu  ',
				"options":['Mengambil permainan yang serupa dan meniru cara bermain',
						 'Diam dan tidak banyak berespon, hanya melihat temannya bermain',
						 'Mengambil mainan milik temannya dan kemudian melemparnya ',
						 'Hanya melihat saja kemudian tidak tertarik dan beralih ke kegiatan lain'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '24-Sosio'
			},
			{
				"id": 68,
				"q":"Berikut ini kemampuan motorik halus yang sudah bisa kembangkan oleh anak usia 13-18 bulan, <strong>kecuali</strong>",
				"options":['Anak mulai gemar untuk menendang bola dengan kakinya',
						 'Anak mulai menggunakan tangan dan jemarinya untuk mengambil benda atau mainan, dan bisa menggunakan jarinya dalam hal menyusun, atau menumpuk atau memindahkan mainan',
						 'Anak mulai gemar mencoret-coret saat mnemukan alat tulis ',
						 'Anak mulai gemar meleparkan kaus kaki dan sepatu dengan menggunakan tangannya'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '24-Fisik'
			},
			{
				"id": 69,
				"q":'Respon yang diberikan anak yang berusia 18-24 bulan  Ketika berdiri dihadapan cermin, yaitu  ',
				"options":['Tersenyum saat menyadari dirinya dan mulai mengujungi beberapa kali untuk memastikan dirinya yang berada di cermin',
					 	 'Tidak memberikan respon apapun',
					 	 'Anak menunjukan reaksi emosi yang negatif, marah dan memukul cermin',
					 	 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '25-Kognitif'
			},
			{
				"id": 70,
				"q":'Berikut ini upaya yang ditunjukan oleh anak yang berusia 12-18 bulan dalam membangun interaksi sosial dengan pengasuhnya, <strong>kecuali</strong>',
				"options":['Anak akan berguling-guling tanpa penyebab kondisi yang jelas',
						 'Anak akan menggunakan gestur atau menyebutkan satu kata dari apa yang dia inginkan atua dia tanyakan dengan melihat ke orang tua',
						 'Anak akan melihat benda/ permainan secara bersamaan dengan orang tua sambil menanyakan nya ',
						 'Anak akan mengoceh, mengeluarkan gerakan, dan tertawa untuk menarik perhatian orang tua'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '25-Sosio'
			},
			{
				"id": 71,
				"q":"Berikut ini kemampuan-kemampuan yang sudah bisa ditunjukan oleh anak usia 18-24 dalam hal perkembangan fisiknya, <strong>kecuali</strong>",
				"options":['Berjalan dengan satu kaki tanpa adanya bantuan',
						 'Mulai belajar dalam melakukan toilet training',
						 'Mampu berjalan dan terkadang sesekali terjatuh di permukaan yang tidak rata dengan adanya bantuan',
						 'Mulai ada ketertarikan untuk makan sendiri, sehingga bisa untuk menyuapi makanan ke mulutnya sendiri '],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '25-Fisik'
			},
			{
				"id": 72,
				"q":'Anak usia 24 bulan pada saat orang tuanya menanyakan 1 warna yang sudah sering disebutkan dan diajarkan oleh tuanya, mampu menunjukan warna yang ditanya dengan tepat, pernyataan berikut menunjukkan',
				"options":['Anak sudah memiliki kemampuan yang sesuai dengan usianya',
					 	 'Anak memiliki kemampuan yang melebih usianya',
					 	 'Anak sudah hampir menunjukkan perkembangan yang sesuai namun terdapat beberapa poin yang belum sesuai',
					 	 'Anak belum memiliki perkembangan yang sesuai usianya'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '26-Kognitif'
			},
			{
				"id": 73,
				"q":'Anak saat melakukan eksplorasi di lingkungan baru, akan selalu melihat ke arah orang tuanya, memastikan orang tuanya tetap berada di sekitar dirinya. Pada usia berapakah hal itu terjadi ',
				"options":['Mulai usia 16 bulan',
						 'Mulai usia 6 bulan',
						 'Mulai usia 12 bulan',
						 'Mulai usia 24 bulan'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '26-Sosio'
			},
			{
				"id": 74,
				"q":"Berikut perkembangan yang dimiliki oleh anak dalam hal pengendalian keseimbangan dirinya pada usia 18-24 bulan <strong>kecuali</strong>",
				"options":['Mampu menggunakan mainan beroda dan mengendarainya seperti mobil-mobilan',
						 'Berdiri dengan satu kaki dengan menggunakan bantuan',
						 'Mampu berlari sesekali',
						 'Mampu berjalan naik turun tangga dengan bantuan orang lain'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '26-Fisik'
			},
			{
				"id": 75,
				"q":'Respon yang sudah ditunjukan oleh anak usia 18-24 bulan pada saat orang tua menanyakan benda-benda yang familiar di rumahnya yaitu ',
				"options":['Anak menunjukan benda yang dimaksud dengan benar',
					 	 'Anak hanya diam dan tidak merespon, mengalihkan pandangan',
					 	 'Anak tidak menjalin kontak mata pada saat orang tua bertanya',
					 	 'Anak meresponnya tetapi banyak benda yang ditunjukanya tidak sesuai dengan yang dimaksud oleh orang tua'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '27-Kognitif'
			},
			{
				"id": 76,
				"q":'Berikut ini yang <strong>tidak termasuk</strong> pada respon sosial  yang ditunjukan oleh anak berusia 18-24 bulan pada saat masuk ke lingkungan baru dengan posisi orang tua yang jauh dari jangkauan anak',
				"options":['Tidak menangis dan tidak melihat orang tua dalam jangka waktu yang cukup lama',
						 'Berusaha untuk mencari-cari orang tua dan melihat ke arah orang tuanya',
						 'Tampak takut, berusaha untuk bermain sendiri tetapi tetap mencari dan melihat orang taunya dari jauh sesekali',
						 'Terkadang emosinya akan intens dan kemudian akan reda dan ingin bermain sendiri setelah ditemani oleh orang tua'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '27-Sosio'
			},
			{
				"id": 77,
				"q":"Berikut ini bentuk perkembangan motoric kasar anak usia 18-24 bulan yang ditunjukannya pada saat menaiki tangga, <strong>kecuali</strong>",
				"options":['Anak menaiki tangga dengan menggunakan kaki yang sudah fasih bergantian',
						 'Anak menaiki tangga melangkahi satu per satu kakinnya',
						 'Anak menaiki tangga dengan melangkahi kakinya sambil berpegangan atau dengan bantuan',
						 'Anak menuruni anak tangga dengan menggunakan kaki satu persatu dengan bantuan'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '27-Fisik'
			},
			{
				"id": 78,
				"q":'Berikut ini kemampuan belajar yang sudah dimiliki anak berusianya 18-24 bulan, <strong>kecuali</strong>',
				"options":['Anak bisa menggunakan sepeda tanpa bantuan ',
					 	 'Anak mampu membalikan halaman buku dan menunjukan gambar yang tepat yang ditanyakan oleh orang tua',
					 	 'Anak sudah mulai untuk membuat coret-coretan di kertas ',
					 	 'Anak mampu menunjuk dirinya saat ditanya namanya'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '28-Kognitif'
			},
			{
				"id": 79,
				"q":'Reaksi emosi yang ditunjukan oleh anak usia 18-24 bulan pada saat ia sedang bermain kemudian menyadari orang tuanya tidak berada di dekatnya maka akan',
				"options":['Menunjukan tanda-tanda stress, seperti mencari, ekpresi takut dan kemudian menangis',
						 'Melihat sekeliling dan diam melanjutkan permainan',
						 'Menunjukan ekpresi senang sebagaimana ia bermain sebelumnya',
						 'Semua jawaban benar'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '28-Sosio'
			},
			{
				"id": 80,
				"q":"Anak yang berusia 18-24 bulan pada saat diberikan kertas dan baru bisa mengguakan alat tulis dengan membuat coretan, artinya",
				"options":['Anak menunjukan perkembangan motorik halus yang sudah sesuai dengan usianya',
						 'Anak menunjukan perkembangan motorik halus yang belum sesuai dengan usianya',
						 'Anak menunjukan perkembangan motorik kasar yang sudah sesuai dengan usianya',
						 'Anak menunjukan perkembangan motoric kasar yang belum sesuai dengan usianya'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '28-Fisik'
			},
			{
				"id": 81,
				"q":'Salah satu pencapaian penting yang ditunjukkan oleh anak yang berusia 18-24 bulan yaitu kemampuan Bahasa yang sudah mulai berkembang, <strong>kecuali</strong>',
				"options":['Anak hanya mengetahui 1-2 objek familiar yang ditanya oleh ibunya ',
					 	 'Anak mengetahui binatang dengan menyebutkan dan menirukan suara binatang',
					 	 'Anak mampu menunjukkan 5 bagian tubuhnya saat diminta oleh orang tuanya',
					 	 'Anak sudah dapat menggunakan 50+ kata, membuat kalimat dari 2 kata '],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '29-Kognitif'
			},
			{
				"id": 82,
				"q":'Kemampuan sosial dalam bermain yang ditunjukan oleh anak usia 18-24 bulan, <strong>kecuali</strong>',
				"options":['Anak enggan untuk bermain dengan menunjukan perilaku yang berguling-guling dan emosi yang intens',
						 'Anak mampu untuk bermain sendiri  dengan mainan yang tampak dan disediakan oleh orang tua',
						 'Anak sering kali meniru perilaku yang ditunjukan oleh anak yang lebih besar (usia 2-3 tahun) pada saat bermain',
						 'Anak mampu menanggapi orang tuanya dengan 1-2 kata yang bisa dipahami oleh orang tua saat bermain '],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '29-Sosio'
			},
			{
				"id": 83,
				"q":"Anak yang sudah mulai bisa menggerakan badannya  dari duduk kemudian berdiri dan berjalan sendiri diusia 18-24, pernyataan yang tidak mendukung yaitu",
				"options":['Anak sedang berlatih dalam memahirkan kemampuan motoric halusnya',
						 'Anak sudah menunjukan pengendalian tubuh bagian bawah yang cukup kuat diusianya',
						 'Anak sedang berlatih dalam memahirkan kemampuan motoric kasarnya',
						 'Anak sedang belajar untuk mengendalikan keseimbangan tubuhnya di usianya'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '29-Fisik'
			},
			{
				"id": 84,
				"q":'Pada usia berapa anak mulai menunjukkan kemampuan untuk bisa paham dan mengikuti  instruksi 2 langkah yang diberikan oleh orang tua ?',
				"options":['Usia 24 bulan',
					 	 'Usia 8 bulan',
					 	 'Usia 12 bulan',
					 	 'Usia 18 bulan'],
				"answer": 0,
				"category": 'Aspek Kognititf',
				"paralel": '30-Kognitif'
			},
			{
				"id": 85,
				"q":'Anak pada usia 18 bulan anak akan menunjukan ketergantungan pada sosok orang tuanya, selalu ingin berada di dekat dan ingin dipenuhi segala keinginannya dan  ingin ditenangkan saat menangis, pernyataan tersebut menunjukan bahwa',
				"options":['Anak menunjukan perkembangan emosi yang sesuai dengan usianya',
						 'Anak tidak menunjukan perkembangan emosi yang sesuai dengan usianya',
						 'Anak menunjukan keterlambatan dalam perkembangan emosinya diusia tersebut',
						 'Anak menunjukan ketidakmampuan dalam mengendalikan emosinya di usia tersebut'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '30-Sosio'
			},
			{
				"id": 86,
				"q":"Di bawah ini yang <strong>bukan</strong> menunjukkan perkembangan kemampuan motorik halus anak usia 18-24 bulan adalah",
				"options":['Melempar bola dengan satu tangannya',
						 'Memainkan mainan yang beroda dengan cara mendorongnya ke depan dan kebelakang untuk menggerakan roda mainanya tersebut',
						 'Menggenggam sendok untuk makan sendiri',
						 'Mencoret-coret dan memindahkan benda tanpa tujuan'],
				"answer": 0,
				"category": 'Aspek Fisik',
				"paralel": '30-Fisik'
			},
			{
				"id": 87,
				"q":'Berikut ini yang <strong>bukan</strong> termasuk capaian perkembangan sosial emosi anak usia 12-24 bulan yaitu',
				"options":['Anak selalu menggunakan gesture saat menunjukan sesuatu dan tidak pernah memverbalkan apa yang diinginkannya',
						 'Anak sering kali meniru aktivitas yang sering dikerjakan oleh orang tua',
						 'Anak mampu bermain sendiri, secara aktif mengekplorasi mainan dengan mengeluarkan suara dan menggerakan mainan',
						 'Anak melakukan kegiatan berulang yang dapat membuat orang lain menjawa tertawa dan senang'],
				"answer": 0,
				"category": 'Aspek Sosio Emosional',
				"paralel": '31-Sosio'
			},
		]

		print(type(quiz))
		print(quiz[0]["options"][3])

		if question.objects.all().count() < 1:
			for idx,q in enumerate(quiz):
				quest = question.objects.create(
					questionID=idx,
					question=q["q"],
					category=q["category"],
					option1=q["options"][0],
					option2=q["options"][1],
					option3=q["options"][2],
					option4=q["options"][3],
					paralel=q["paralel"])
				quest.save()

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
