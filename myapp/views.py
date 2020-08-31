from django.shortcuts import render, HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template

from . models import online_course

# Create your views here.
def home(request):

    return render(request,'index.html')
    # return HttpResponse('index page bro')

def render_pdf_view(request):
    data_pdf =   online_course.objects.all()


    template_path = 'index.html'
    context = {'datass': data_pdf}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # if auto download the pdf 
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # if download pdf manualy with pdf name
    response['Content-Disposition'] = ' filename="report.pdf"'


    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response    