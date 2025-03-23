from django.shortcuts import render

## custom error -- page not found error page(404)
def page_error(request,exception):
    return render(request,'404_page.html', status=404)
