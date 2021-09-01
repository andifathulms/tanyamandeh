from django.contrib import admin

# Register your models here.
from quizTest.models import responden, sessionMark, sessionOrder, comment
from quizTest.models import wilayah, question, session, sessionScore

admin.site.register(responden)
admin.site.register(wilayah)
admin.site.register(question)
admin.site.register(session)
admin.site.register(sessionMark)
admin.site.register(sessionOrder)
admin.site.register(comment)