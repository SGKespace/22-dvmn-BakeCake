from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):
    def get(self, request):

        context = {

        }
        return render(request, 'index.html', context=context)

    def post(self, request):
        print(request.POST)
        return redirect('index')
