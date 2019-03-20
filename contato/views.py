from django.http import HttpResponseForbidden, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from contato.models import Contato
from django.forms.models import model_to_dict


@csrf_exempt
def contato(request):
    response = {
        'metodo': request.method
    }

    if request.method == 'GET':
        response['lista'] = list(Contato.objects.values())

    elif request.method == 'POST':
        post = QueryDict(request.body)
        novocontato = Contato()
        novocontato.nome = post['nome']
        novocontato.email = post['email']
        novocontato.telefone = post['telefone']
        novocontato.save()
        response['contato'] = model_to_dict(novocontato)

    elif request.method == 'PUT':
        put = QueryDict(request.body)

        try:
            novocontato = Contato.objects.get(pk=put['codigo'])
            novocontato.nome = put['nome']
            novocontato.email = put['email']
            novocontato.telefone = put['telefone']
            novocontato.save()
            response['contato'] = model_to_dict(novocontato)
        except:
            response['erro'] = 'Contato não localizado'
            JsonResponse(response)

    else:
        return HttpResponseForbidden("Método de requisição não permitido")

    return JsonResponse(response)


@csrf_exempt
def contato_codigo(request, codigo):
    response = {
        'metodo': request.method
    }

    if request.method != 'GET' and request.method != 'DELETE':
        return HttpResponseForbidden("Método de requisição não permitido")

    try:

        contato = Contato.objects.get(pk=codigo)

        if request.method == 'GET':
            response['contato'] = model_to_dict(contato)
        else:
            contato.delete()
            response['sucesso'] = 'Contato excluído com sucesso'

    except:
        response['erro'] = 'Contato não localizado'
        return JsonResponse(response)

    return JsonResponse(response)
