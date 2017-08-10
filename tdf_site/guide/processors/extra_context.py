from django.conf import settings # import the settings file

def googleapis(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}
