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
	if request.is_ajax():
		if request.method == "GET":
			print(context)
			print("GET")
			return JsonResponse({'data':list(context['regionFilter'])})
		else:
			dataTemp = json.dumps(request.POST)
			data = json.loads(dataTemp)
			print(data["id"])
			#print(data)
			if data["id"] == "1":
				jsonTemp = data["data"]
				jsonData = json.loads(jsonTemp)
				ipTemp = data["jsonIP"]
				ipData = json.loads(ipTemp)
				print(jsonTemp)
				#print(ipData["ip"])
				#print(data["jsonIP"])
				#r = responden(
				#	name = jsonData["nama"],
				#	age = jsonData["age"],
				#	prov = jsonData["prov"],
				#	kab = jsonData["kabupaten"],)
				#r.save()
				print(data["id"])
				return render(request, "quiz.html", context)
			elif data["id"] == "2":
				print(data["data"])
				kab = wilayah.objects.filter(provinsi=data["data"]).values('kabupaten')
				context['regionFilter'] = kab
				print(context)
				print("2")
				return render(request, "quiz.html", context)
			elif data["id"] == "3":
				print(context)
				print("3")
				return render(request, "quiz.html", context)
			elif data["id"] == "4":
				print("4")
				print(data["userData"])
				print(data["quizOrder"])
				print(data["quizAnswer"])
				print(data["quizChoice"])
				print(data["duration"] + " seconds")
				print(datetime.now())
				print(datetime.now() - timedelta(seconds= int(data["duration"])))
				#print(int(data["correctChess"]) + " - " + int(data["correctMath"]) + " - " + int(data["correctGeography"]) + " - " + int(data["correctFootball"]))
				jsonTemp = data["userData"]
				jsonData = json.loads(jsonTemp)
				quizOrderTemp = data["quizOrder"]
				quizOrder = json.loads(quizOrderTemp)
				quizAnswerTemp = data["quizAnswer"]
				quizAnswer = json.loads(quizAnswerTemp)
				quizChoiceTemp = data["quizChoice"]
				quizChoice = json.loads(quizChoiceTemp)
				ipTemp = data["jsonIP"]
				ipData = json.loads(ipTemp)
				#print(ipData)
				total = int(data["correctKognitif"]) + int(data["correctSosio"]) + int(data["correctFisik"])
				
				r = responden.objects.create(
					name = jsonData["nama"],
					age = jsonData["age"],
					prov = jsonData["prov"],
					kab = jsonData["kabupaten"],
					gender = jsonData["gender"],
					agama = jsonData["agama"],
					statusnikah = jsonData["marriage"],
					jumlahanak = jsonData["children"],
					usiaanak1 = jsonData["childrenage1"],
					usiaanak2 = jsonData["childrenage2"],
					educ = jsonData["pendidikan"],
					educg = jsonData["educbg"],
					job = jsonData["job"],
					jobg = jsonData["jobbg"],
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
					quest37Ans = quizChoice["37"],quest38Ans = quizChoice["38"],quest39Ans = quizChoice["39"],quest40Ans = quizChoice["40"],
					quest41Ans = quizChoice["41"],quest42Ans = quizChoice["42"],quest43Ans = quizChoice["43"],quest44Ans = quizChoice["44"],
					quest45Ans = quizChoice["45"],quest46Ans = quizChoice["46"],quest47Ans = quizChoice["47"],quest48Ans = quizChoice["48"],
					quest49Ans = quizChoice["49"],quest50Ans = quizChoice["50"],quest51Ans = quizChoice["51"],quest52Ans = quizChoice["52"],
					quest53Ans = quizChoice["53"],quest54Ans = quizChoice["54"],quest55Ans = quizChoice["55"],quest56Ans = quizChoice["56"],
					quest57Ans = quizChoice["57"],quest58Ans = quizChoice["58"],quest59Ans = quizChoice["59"],quest60Ans = quizChoice["60"],
					quest61Ans = quizChoice["61"],quest62Ans = quizChoice["62"],quest63Ans = quizChoice["63"],quest64Ans = quizChoice["64"],
					quest65Ans = quizChoice["65"],quest66Ans = quizChoice["66"],quest67Ans = quizChoice["67"],quest68Ans = quizChoice["68"],
					quest69Ans = quizChoice["69"],quest70Ans = quizChoice["70"],quest71Ans = quizChoice["71"],quest72Ans = quizChoice["72"],
					quest73Ans = quizChoice["73"],quest74Ans = quizChoice["74"],quest75Ans = quizChoice["75"],quest76Ans = quizChoice["76"],
					quest77Ans = quizChoice["77"],quest78Ans = quizChoice["78"],quest79Ans = quizChoice["79"],quest80Ans = quizChoice["80"],
					quest81Ans = quizChoice["81"],quest82Ans = quizChoice["82"],quest83Ans = quizChoice["83"],quest84Ans = quizChoice["84"],
					quest85Ans = quizChoice["85"],quest86Ans = quizChoice["86"],quest87Ans = quizChoice["87"]
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
					quest37Pos = quizOrder["37"],quest38Pos = quizOrder["38"],quest39Pos = quizOrder["39"],quest40Pos = quizOrder["40"],
					quest41Pos = quizOrder["41"],quest42Pos = quizOrder["42"],quest43Pos = quizOrder["43"],quest44Pos = quizOrder["44"],
					quest45Pos = quizOrder["45"],quest46Pos = quizOrder["46"],quest47Pos = quizOrder["47"],quest48Pos = quizOrder["48"],
					quest49Pos = quizOrder["49"],quest50Pos = quizOrder["50"],quest51Pos = quizOrder["51"],quest52Pos = quizOrder["52"],
					quest53Pos = quizOrder["53"],quest54Pos = quizOrder["54"],quest55Pos = quizOrder["55"],quest56Pos = quizOrder["56"],
					quest57Pos = quizOrder["57"],quest58Pos = quizOrder["58"],quest59Pos = quizOrder["59"],quest60Pos = quizOrder["60"],
					quest61Pos = quizOrder["61"],quest62Pos = quizOrder["62"],quest63Pos = quizOrder["63"],quest64Pos = quizOrder["64"],
					quest65Pos = quizOrder["65"],quest66Pos = quizOrder["66"],quest67Pos = quizOrder["67"],quest68Pos = quizOrder["68"],
					quest69Pos = quizOrder["69"],quest70Pos = quizOrder["70"],quest71Pos = quizOrder["71"],quest72Pos = quizOrder["72"],
					quest73Pos = quizOrder["73"],quest74Pos = quizOrder["74"],quest75Pos = quizOrder["75"],quest76Pos = quizOrder["76"],
					quest77Pos = quizOrder["77"],quest78Pos = quizOrder["78"],quest79Pos = quizOrder["79"],quest80Pos = quizOrder["80"],
					quest81Pos = quizOrder["81"],quest82Pos = quizOrder["82"],quest83Pos = quizOrder["83"],quest84Pos = quizOrder["84"],
					quest85Pos = quizOrder["85"],quest86Pos = quizOrder["86"],quest87Pos = quizOrder["87"]
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
					quest37Scr = quizAnswer["37"],quest38Scr = quizAnswer["38"],quest39Scr = quizAnswer["39"],quest40Scr = quizAnswer["40"],
					quest41Scr = quizAnswer["41"],quest42Scr = quizAnswer["42"],quest43Scr = quizAnswer["43"],quest44Scr = quizAnswer["44"],
					quest45Scr = quizAnswer["45"],quest46Scr = quizAnswer["46"],quest47Scr = quizAnswer["47"],quest48Scr = quizAnswer["48"],
					quest49Scr = quizAnswer["49"],quest50Scr = quizAnswer["50"],quest51Scr = quizAnswer["51"],quest52Scr = quizAnswer["52"],
					quest53Scr = quizAnswer["53"],quest54Scr = quizAnswer["54"],quest55Scr = quizAnswer["55"],quest56Scr = quizAnswer["56"],
					quest57Scr = quizAnswer["57"],quest58Scr = quizAnswer["58"],quest59Scr = quizAnswer["59"],quest60Scr = quizAnswer["60"],
					quest61Scr = quizAnswer["61"],quest62Scr = quizAnswer["62"],quest63Scr = quizAnswer["63"],quest64Scr = quizAnswer["64"],
					quest65Scr = quizAnswer["65"],quest66Scr = quizAnswer["66"],quest67Scr = quizAnswer["67"],quest68Scr = quizAnswer["68"],
					quest69Scr = quizAnswer["69"],quest70Scr = quizAnswer["70"],quest71Scr = quizAnswer["71"],quest72Scr = quizAnswer["72"],
					quest73Scr = quizAnswer["73"],quest74Scr = quizAnswer["74"],quest75Scr = quizAnswer["75"],quest76Scr = quizAnswer["76"],
					quest77Scr = quizAnswer["77"],quest78Scr = quizAnswer["78"],quest79Scr = quizAnswer["79"],quest80Scr = quizAnswer["80"],
					quest81Scr = quizAnswer["81"],quest82Scr = quizAnswer["82"],quest83Scr = quizAnswer["83"],quest84Scr = quizAnswer["84"],
					quest85Scr = quizAnswer["85"],quest86Scr = quizAnswer["86"],quest87Scr = quizAnswer["87"]
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

				return render(request, "quiz.html", context)
			elif data["id"] == "5":
				print("5")
				print(data["nama"])
				print(data["comment"])

				c = comment(nama = data["nama"], comment = data["comment"])
				c.save()

				return render(request, "quiz.html", context)
	else:
		#print("request = " + str(request))
		#print(regions[0])
		return render(request, "quiz.html", context)

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
	respHeader = ["Name","L/P","Age","Provinsi","Kabupaten","Agama","Status Nikah","Jumlah Anak",
				  "Umur Anak1","Umur Anak2","Pendidikan","Latar Pendidikan",
				  "Pekerjaan","Latar Pekerjaan","NoHP","Tanggal"]
	sessHeader = ["Score Kognitif","Score Sosio","Score Fisik"," Score Total",
				  "Time Start", "Time End", "Duration(Sec)"]
	scoreHeader = ["Q1 Score","Q2 Score","Q3 Score","Q4 Score","Q5 Score","Q6 Score","Q7 Score","Q8 Score","Q9 Score","Q10 Score",
				  "Q11 Score","Q12 Score","Q13 Score","Q14 Score","Q15 Score","Q16 Score","Q17 Score","Q18 Score","Q19 Score","Q20 Score",
				  "Q21 Score","Q22 Score","Q23 Score","Q24 Score","Q25 Score","Q26 Score","Q27 Score","Q28 Score","Q29 Score","Q20 Score",
				  "Q31 Score","Q32 Score","Q33 Score","Q34 Score","Q35 Score","Q36 Score","Q37 Score","Q38 Score","Q39 Score","Q30 Score",
				  "Q41 Score","Q42 Score","Q43 Score","Q44 Score","Q45 Score","Q46 Score","Q47 Score","Q48 Score","Q49 Score","Q40 Score",
				  "Q51 Score","Q52 Score","Q53 Score","Q54 Score","Q55 Score","Q56 Score","Q57 Score","Q58 Score","Q59 Score","Q50 Score",
				  "Q61 Score","Q62 Score","Q63 Score","Q64 Score","Q65 Score","Q66 Score","Q67 Score","Q68 Score","Q69 Score","Q60 Score",
				  "Q71 Score","Q72 Score","Q73 Score","Q74 Score","Q75 Score","Q76 Score","Q77 Score","Q78 Score","Q79 Score","Q70 Score",
				  "Q81 Score","Q82 Score","Q83 Score","Q84 Score","Q85 Score","Q86 Score","Q87 Score"]
	markHeader = ["Q1 Mark","Q2 Mark","Q3 Mark","Q4 Mark","Q5 Mark","Q6 Mark","Q7 Mark","Q8 Mark","Q9 Mark","Q10 Mark",
				  "Q11 Mark","Q12 Mark","Q13 Mark","Q14 Mark","Q15 Mark","Q16 Mark","Q17 Mark","Q18 Mark","Q19 Mark","Q20 Mark",
				  "Q21 Mark","Q22 Mark","Q23 Mark","Q24 Mark","Q25 Mark","Q26 Mark","Q27 Mark","Q28 Mark","Q29 Mark","Q20 Mark",
				  "Q31 Mark","Q32 Mark","Q33 Mark","Q34 Mark","Q35 Mark","Q36 Mark","Q37 Mark","Q38 Mark","Q39 Mark","Q30 Mark",
				  "Q41 Mark","Q42 Mark","Q43 Mark","Q44 Mark","Q45 Mark","Q46 Mark","Q47 Mark","Q48 Mark","Q49 Mark","Q40 Mark",
				  "Q51 Mark","Q52 Mark","Q53 Mark","Q54 Mark","Q55 Mark","Q56 Mark","Q57 Mark","Q58 Mark","Q59 Mark","Q50 Mark",
				  "Q61 Mark","Q62 Mark","Q63 Mark","Q64 Mark","Q65 Mark","Q66 Mark","Q67 Mark","Q68 Mark","Q69 Mark","Q60 Mark",
				  "Q71 Mark","Q72 Mark","Q73 Mark","Q74 Mark","Q75 Mark","Q76 Mark","Q77 Mark","Q78 Mark","Q79 Mark","Q70 Mark",
				  "Q81 Mark","Q82 Mark","Q83 Mark","Q84 Mark","Q85 Mark","Q86 Mark","Q87 Mark"]
	orderHeader = ["Q1 Order","Q2 Order","Q3 Order","Q4 Order","Q5 Order","Q6 Order","Q7 Order","Q8 Order","Q9 Order","Q10 Order",
				  "Q11 Order","Q12 Order","Q13 Order","Q14 Order","Q15 Order","Q16 Order","Q17 Order","Q18 Order","Q19 Order","Q20 Order",
				  "Q21 Order","Q22 Order","Q23 Order","Q24 Order","Q25 Order","Q26 Order","Q27 Order","Q28 Order","Q29 Order","Q20 Order",
				  "Q31 Order","Q32 Order","Q33 Order","Q34 Order","Q35 Order","Q36 Order","Q37 Order","Q38 Order","Q39 Order","Q30 Order",
				  "Q41 Order","Q42 Order","Q43 Order","Q44 Order","Q45 Order","Q46 Order","Q47 Order","Q48 Order","Q49 Order","Q40 Order",
				  "Q51 Order","Q52 Order","Q53 Order","Q54 Order","Q55 Order","Q56 Order","Q57 Order","Q58 Order","Q59 Order","Q50 Order",
				  "Q61 Order","Q62 Order","Q63 Order","Q64 Order","Q65 Order","Q66 Order","Q67 Order","Q68 Order","Q69 Order","Q60 Order",
				  "Q71 Order","Q72 Order","Q73 Order","Q74 Order","Q75 Order","Q76 Order","Q77 Order","Q78 Order","Q79 Order","Q70 Order",
				  "Q81 Order","Q82 Order","Q83 Order","Q84 Order","Q85 Order","Q86 Order","Q87 Order"]
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