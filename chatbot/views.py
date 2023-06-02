from django.shortcuts import render
from numpy import int32
from requests import post
from django.conf import settings 
from happytransformer import GENSettings


# Create your views here.
def home(request):
    print(request.POST)
    if request.method=="POST":    
         if getattr(settings, 'HAPPY_GEN'):  
            happy_gen = settings.HAPPY_GEN
            question=request.POST['question']
            maxlength=str(request.POST['maxlength'])
            print(maxlength)
            #args=GENSettings(no_repeat_ngram_size=2,max_length=int(maxlength))
            res = happy_gen(question, max_length=50, do_sample=True, temperature=0.9)
            #result=happy_gen.generate_text(question, args=args)
            print(res)
            return render(request, 'home.html',{"question":question,"maxlength": maxlength,"result": res[0]['generated_text']})
    
    return render(request, 'home.html',{})