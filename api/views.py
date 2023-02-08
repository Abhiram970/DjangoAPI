from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from googletrans import Translator 

@api_view(['POST']) 
def langTranslate(request):
    sentence = request.data.get("text")
    translator = Translator()
    sentence = translator.translate(sentence,dest = "en").text 
    return Response({"message":sentence})