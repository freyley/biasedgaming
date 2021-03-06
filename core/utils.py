from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response


def template(template_name):
    def decorator(fn):
        def render(request, *args, **kwargs):
            context_data = fn(request, *args, **kwargs)
            if isinstance(context_data, HttpResponse):
                # View returned an HttpResponse like a redirect
                return context_data
            else:
                # For any other type of data try to populate a template
                return render_to_response(
                    template_name,
                    context_data,
                    context_instance=RequestContext(request),
                )

        return render

    return decorator

