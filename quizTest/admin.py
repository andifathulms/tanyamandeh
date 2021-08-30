from django.contrib import admin

# Register your models here.
from quizTest.models import responden, sessionMark, sessionOrder
from quizTest.models import wilayah, question, session

admin.site.register(responden)
admin.site.register(wilayah)
admin.site.register(question)
admin.site.register(session)
admin.site.register(sessionMark)
admin.site.register(sessionOrder)