from django.shortcuts import render,redirect
from quizTest.models import responden
from quizTest.models import wilayah, session, sessionMark, sessionOrder, comment, sessionScore
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from datetime import datetime, timedelta
import json
import csv

json_serializer = serializers.get_serializer("json")()
# this = companies = json_serializer.serialize(responden.objects.all().order_by('id'), ensure_ascii=False)
django_list = responden.objects.all()
#regions = json_serializer.serialize(wilayah.objects.all().order_by('id'), ensure_ascii=False)
#regions = wilayah.objects.all()
regions = wilayah.objects.values('provinsi').distinct()
# Create your views here.
context = {
		'regions' : regions,
	}
@csrf_protect
def home_view(request, *args, **kwargs):
	request.session.set_test_cookie()
	if request.session.test_cookie_worked():
		print("Cookies Worked")
		print(request.COOKIES.get('visits', '1'))
	if 'idResponden' in request.COOKIES:
		print("IT IS !")
	if request.is_ajax():
		print(request.session)
		if request.method == "GET":
			#print(context)
			#print("GET")
			return JsonResponse({'data':list(context['regionFilter'])})
		else:
			dataTemp = json.dumps(request.POST)
			data = json.loads(dataTemp)
			#print(data["id"])
			#print(data)
			if data["id"] == "1":
				jsonTemp = data["data"]
				jsonData = json.loads(jsonTemp)
				ipTemp = data["jsonIP"]
				ipData = json.loads(ipTemp)
				#print(jsonTemp)
				#print(data["id"])
				#print(data["data"])

				#Create the user
				jsonTemp = data["data"]
				jsonData = json.loads(jsonTemp)

				r = responden.objects.create(
					name = jsonData["nama"],
					age = jsonData["age"],
					prov = jsonData["prov"],
					kab = jsonData["kabupaten"],
					gender = jsonData["gender"],
					statusnikah = jsonData["marriage"],
					jumlahanak = jsonData["children"],
					usiaanak1 = jsonData["childrenage1"],
					usiaanak2 = jsonData["childrenage2"],
					educ = jsonData["pendidikan"],
					job = jsonData["job"],
					nohp = jsonData["nohp"])

				r.save()

				res = responden.objects.get(name=jsonData["nama"],age=jsonData["age"],kab=jsonData["kabupaten"],nohp=jsonData["nohp"])
				#COOKIE Settings
				visits = int(request.COOKIES.get('visits', '1'))
				reset_last_visit_time = False
				response = render(request, "main.html", context)
				if 'last_visit' in request.COOKIES:
					# Yes it does! Get the cookie's value.
					last_visit = request.COOKIES['last_visit']
					# Cast the value to a Python date/time object.
					last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

					# If it's been more than a day since the last visit...
					if (datetime.now() - last_visit_time).days > 0:
						visits = visits + 1
						# ...and flag that the cookie last visit needs to be updated
						reset_last_visit_time = True
				else:
					# Cookie last_visit doesn't exist, so flag that it should be set.
					reset_last_visit_time = True

					context['visits'] = visits

					#Obtain our Response object early so we can add cookie information.
					response = render(request, "main.html", context)

				if 'responden' in request.COOKIES:
					pass
				else:
					context['responden'] = res.id
					idResponden = res.id
					print(idResponden)
					response = render(request, "main.html", context)
					response.set_cookie('idResponden', idResponden)

				if reset_last_visit_time:
					response.set_cookie('last_visit', datetime.now())
					response.set_cookie('visits', visits)


				return response
			elif data["id"] == "2":
				#print(data["data"])
				kab = wilayah.objects.filter(provinsi=data["data"]).values('kabupaten')
				context['regionFilter'] = kab
				#print(context)
				print("Data = 2")
				return render(request, "main.html", context)
			elif data["id"] == "3":
				#print(context)
				print("Data = 3")
				return render(request, "main.html", context)
			elif data["id"] == "4":
				print("Data = 4")
				
				quizOrderTemp = data["quizOrder"]
				quizOrder = json.loads(quizOrderTemp)
				quizAnswerTemp = data["quizAnswer"]
				quizAnswer = json.loads(quizAnswerTemp)
				quizChoiceTemp = data["quizChoice"]
				quizChoice = json.loads(quizChoiceTemp)
				
				total = int(data["correctKognitif"]) + int(data["correctSosio"]) + int(data["correctFisik"])
				

				try:
					resID = data["idResponden"] 
					r = responden.objects.get(id=resID)
				except:
					jsonTemp = data["userData"]
					jsonData = json.loads(jsonTemp)
					r = responden.objects.create(
						name = jsonData["nama"],
						age = jsonData["age"],
						prov = jsonData["prov"],
						kab = jsonData["kabupaten"],
						gender = jsonData["gender"],
						statusnikah = jsonData["marriage"],
						jumlahanak = jsonData["children"],
						usiaanak1 = jsonData["childrenage1"],
						usiaanak2 = jsonData["childrenage2"],
						educ = jsonData["pendidikan"],
						job = jsonData["job"],
						nohp = jsonData["nohp"])

				mark = sessionMark.objects.create(
					quest1Ans = quizChoice["1"],quest2Ans = quizChoice["2"],quest3Ans = quizChoice["3"],quest4Ans = quizChoice["4"],
					quest5Ans = quizChoice["5"],quest6Ans = quizChoice["6"],quest7Ans = quizChoice["7"],quest8Ans = quizChoice["8"],
					quest9Ans = quizChoice["9"],quest10Ans = quizChoice["10"],quest11Ans = quizChoice["11"],quest12Ans = quizChoice["12"],
					quest13Ans = quizChoice["13"],quest14Ans = quizChoice["14"],quest15Ans = quizChoice["15"],quest16Ans = quizChoice["16"],
					quest17Ans = quizChoice["17"],quest18Ans = quizChoice["18"],quest19Ans = quizChoice["19"],quest20Ans = quizChoice["20"],
					quest21Ans = quizChoice["21"],quest22Ans = quizChoice["22"],quest23Ans = quizChoice["23"],quest24Ans = quizChoice["24"],
					quest25Ans = quizChoice["25"],quest26Ans = quizChoice["26"],quest27Ans = quizChoice["27"],quest28Ans = quizChoice["28"],
					quest29Ans = quizChoice["29"],quest30Ans = quizChoice["30"],quest31Ans = quizChoice["31"],quest32Ans = quizChoice["32"],
					quest33Ans = quizChoice["33"],quest34Ans = quizChoice["34"],quest35Ans = quizChoice["35"],quest36Ans = quizChoice["36"],
					quest37Ans = quizChoice["37"],quest38Ans = quizChoice["38"],quest39Ans = quizChoice["39"],quest40Ans = quizChoice["40"]
					)

				order = sessionOrder.objects.create(
					quest1Pos = quizOrder["1"],quest2Pos = quizOrder["2"],quest3Pos = quizOrder["3"],quest4Pos = quizOrder["4"],
					quest5Pos = quizOrder["5"],quest6Pos = quizOrder["6"],quest7Pos = quizOrder["7"],quest8Pos = quizOrder["8"],
					quest9Pos = quizOrder["9"],quest10Pos = quizOrder["10"],quest11Pos = quizOrder["11"],quest12Pos = quizOrder["12"],
					quest13Pos = quizOrder["13"],quest14Pos = quizOrder["14"],quest15Pos = quizOrder["15"],quest16Pos = quizOrder["16"],
					quest17Pos = quizOrder["17"],quest18Pos = quizOrder["18"],quest19Pos = quizOrder["19"],quest20Pos = quizOrder["20"],
					quest21Pos = quizOrder["21"],quest22Pos = quizOrder["22"],quest23Pos = quizOrder["23"],quest24Pos = quizOrder["24"],
					quest25Pos = quizOrder["25"],quest26Pos = quizOrder["26"],quest27Pos = quizOrder["27"],quest28Pos = quizOrder["28"],
					quest29Pos = quizOrder["29"],quest30Pos = quizOrder["30"],quest31Pos = quizOrder["31"],quest32Pos = quizOrder["32"],
					quest33Pos = quizOrder["33"],quest34Pos = quizOrder["34"],quest35Pos = quizOrder["35"],quest36Pos = quizOrder["36"],
					quest37Pos = quizOrder["37"],quest38Pos = quizOrder["38"],quest39Pos = quizOrder["39"],quest40Pos = quizOrder["40"]
					)

				score = sessionScore.objects.create(
					quest1Scr = quizAnswer["1"],quest2Scr = quizAnswer["2"],quest3Scr = quizAnswer["3"],quest4Scr = quizAnswer["4"],
					quest5Scr = quizAnswer["5"],quest6Scr = quizAnswer["6"],quest7Scr = quizAnswer["7"],quest8Scr = quizAnswer["8"],
					quest9Scr = quizAnswer["9"],quest10Scr = quizAnswer["10"],quest11Scr = quizAnswer["11"],quest12Scr = quizAnswer["12"],
					quest13Scr = quizAnswer["13"],quest14Scr = quizAnswer["14"],quest15Scr = quizAnswer["15"],quest16Scr = quizAnswer["16"],
					quest17Scr = quizAnswer["17"],quest18Scr = quizAnswer["18"],quest19Scr = quizAnswer["19"],quest20Scr = quizAnswer["20"],
					quest21Scr = quizAnswer["21"],quest22Scr = quizAnswer["22"],quest23Scr = quizAnswer["23"],quest24Scr = quizAnswer["24"],
					quest25Scr = quizAnswer["25"],quest26Scr = quizAnswer["26"],quest27Scr = quizAnswer["27"],quest28Scr = quizAnswer["28"],
					quest29Scr = quizAnswer["29"],quest30Scr = quizAnswer["30"],quest31Scr = quizAnswer["31"],quest32Scr = quizAnswer["32"],
					quest33Scr = quizAnswer["33"],quest34Scr = quizAnswer["34"],quest35Scr = quizAnswer["35"],quest36Scr = quizAnswer["36"],
					quest37Scr = quizAnswer["37"],quest38Scr = quizAnswer["38"],quest39Scr = quizAnswer["39"],quest40Scr = quizAnswer["40"]
					)
				
				s = session(
						responden = r,
						timeStart = datetime.now() - timedelta(seconds= int(data["duration"])),
						timeEnd = datetime.now(),
						duration = data["duration"],
						kognitifScore = data["correctKognitif"],
						sosioScore = data["correctSosio"],
						fisikScore = data["correctFisik"],
						totalScore = total,
						mark = mark,
						order = order,
						score = score
					)
				s.save()
				response = render(request, "main.html", context)
				response.set_cookie('idResponden', "0")
				response.set_cookie('quizOrder', "0")
				response.set_cookie('quizAnswer', "0")
				response.set_cookie('quizChoice', "0")
				response.set_cookie('quizOption', "0")
				response.set_cookie('isStart',"0")
				return response
			elif data["id"] == "5":
				print("5")
				print(data["nama"])
				print(data["comment"])

				c = comment(nama = data["nama"], comment = data["comment"])
				c.save()

				return render(request, "main.html", context)
			elif data["id"] == "6":
				print(6)

				quizOrderTemp = data["quizOrder"]
				quizOrder = json.loads(quizOrderTemp)
				quizAnswerTemp = data["quizAnswer"]
				quizAnswer = json.loads(quizAnswerTemp)
				quizChoiceTemp = data["quizChoice"]
				quizChoice = json.loads(quizChoiceTemp)
				quizOptionTemp = data["quizOption"]
				quizOption = json.loads(quizOptionTemp)

				response = render(request, "main.html", context)

				response.set_cookie('isStart', '1')

				response.set_cookie('quizOrder', quizOrder)
				response.set_cookie('quizAnswer', quizAnswer)
				response.set_cookie('quizChoice', quizChoice)
				response.set_cookie('quizOption', quizOption)

				return response

	else:
		#print("request = " + str(request))
		#print(regions[0])
		return render(request, "main.html", context)

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def addUser(request, *args, **kwargs):
	if request.method == 'POST':
		print(request.POST)
	else:
		print("FUCK OFF")
	#responden.objects.create(**kwargs);

def exportsCSV(request):
	sessions = session.objects.all()
	respondens = responden.objects.all()
	marks = sessionMark.objects.all()
	orders = sessionOrder.objects.all()
	scores = sessionScore.objects.all()
	response = HttpResponse('')
	response['Content-Disposition'] = 'attachment; filename=sessions.csv'
	writer = csv.writer(response,delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	header = ["ID"]
	respHeader = ["Name","L/P","Age","Provinsi","Kabupaten","Status Nikah","Jumlah Anak",
				  "Umur Anak1","Umur Anak2","Pendidikan",
				  "Pekerjaan","NoHP","Tanggal"]
	sessHeader = ["Score Kognitif","Score Sosio","Score Fisik"," Score Total",
				  "Time Start", "Time End", "Duration(Sec)"]
	scoreHeader = ["Q1 Score","Q2 Score","Q3 Score","Q4 Score","Q5 Score","Q6 Score","Q7 Score","Q8 Score","Q9 Score","Q10 Score",
				  "Q11 Score","Q12 Score","Q13 Score","Q14 Score","Q15 Score","Q16 Score","Q17 Score","Q18 Score","Q19 Score","Q20 Score",
				  "Q21 Score","Q22 Score","Q23 Score","Q24 Score","Q25 Score","Q26 Score","Q27 Score","Q28 Score","Q29 Score","Q30 Score",
				  "Q31 Score","Q32 Score","Q33 Score","Q34 Score","Q35 Score","Q36 Score","Q37 Score","Q38 Score","Q39 Score","Q40 Score",]
	markHeader = ["Q1 Mark","Q2 Mark","Q3 Mark","Q4 Mark","Q5 Mark","Q6 Mark","Q7 Mark","Q8 Mark","Q9 Mark","Q10 Mark",
				  "Q11 Mark","Q12 Mark","Q13 Mark","Q14 Mark","Q15 Mark","Q16 Mark","Q17 Mark","Q18 Mark","Q19 Mark","Q20 Mark",
				  "Q21 Mark","Q22 Mark","Q23 Mark","Q24 Mark","Q25 Mark","Q26 Mark","Q27 Mark","Q28 Mark","Q29 Mark","Q30 Mark",
				  "Q31 Mark","Q32 Mark","Q33 Mark","Q34 Mark","Q35 Mark","Q36 Mark","Q37 Mark","Q38 Mark","Q39 Mark","Q40 Mark",]
	orderHeader = ["Q1 Order","Q2 Order","Q3 Order","Q4 Order","Q5 Order","Q6 Order","Q7 Order","Q8 Order","Q9 Order","Q10 Order",
				  "Q11 Order","Q12 Order","Q13 Order","Q14 Order","Q15 Order","Q16 Order","Q17 Order","Q18 Order","Q19 Order","Q20 Order",
				  "Q21 Order","Q22 Order","Q23 Order","Q24 Order","Q25 Order","Q26 Order","Q27 Order","Q28 Order","Q29 Order","Q30 Order",
				  "Q31 Order","Q32 Order","Q33 Order","Q34 Order","Q35 Order","Q36 Order","Q37 Order","Q38 Order","Q39 Order","Q40 Order"]
	header.extend(respHeader)
	header.extend(sessHeader)
	header.extend(scoreHeader)
	header.extend(markHeader)
	header.extend(orderHeader)
	writer.writerow(header)
	id = sessions.values_list('id')
	sess = sessions.values_list()
	resp = respondens.values_list()
	mark = marks.values_list()
	order = orders.values_list()
	score = scores.values_list()
	ready = []
	i = 0
	for s in sess:
		for r in resp:
			if (r[0] == s[1]):
				ready.append(s[0])
				ready.extend(list(r[1:]))
				ready.extend(list(s[2:9]))
				break
		for sc in score:
			if (sc[0] == s[11]):
				ready.extend(list(sc[1:]))
				break
		for m in mark:
			if (m[0] == s[9]):
				ready.extend(list(m[1:]))
				break
		for ord in order:
			if (ord[0] == s[10]):
				ready.extend(list(ord[1:]))
				break
		writer.writerow(ready)
		ready = []
		i += 1
	return response

def exportsComment(request):
	comments = comment.objects.all()
	response = HttpResponse('')
	response['Content-Disposition'] = 'attachment; filename=comments.csv'
	writer = csv.writer(response,delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	header = ["ID","Date","Name","Comment"]
	writer.writerow(header)
	com = comments.values_list()
	for c in com:
		writer.writerow(c)
	return response

@csrf_exempt
def load_kab(request):
    category = request.GET.get('category')
    subcategory = wilayah.objects.filter(provinsi=data["data"]).values('kabupaten')
    
    return render(request, 'snippets/subcategory.html', {'subcategories': subcategory})