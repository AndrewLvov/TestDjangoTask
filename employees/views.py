import json

from django.http import HttpResponse

from .models import Employee


def get_users(request):
    """Return json in format:
    {
        'status':
            'ok' or <custom error message>

        'data':
            [{
                'id': user id
                'first_name': ...
                'last_name': ...
                'department': department name
            },
                ...
            ]
            or
            null in case of error
    }
    """

    user_data = []
    employees = Employee.objects.all()
    for e in employees:
        user_data.append({
            'id': e.id,
            'first_name': e.first_name,
            'last_name': e.last_name,
            'department': e.department.name,
        })

    result = {
        'status': 'ok',
        'data': user_data,
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


def get_user(request):
    """Return json in format:
    {
        'status':
            'ok' or <custom error message>

        'data':
            [{
                'first_name': ...
                'last_name': ...
                'department': department name
            },
                ...
            ]
            or
            null in case of error
    }
    """

    # helper function so get_user could be disassembled later
    def get_response_data(request):
        if 'id' not in request.GET:
            return 'id parameter not specified'

        try:
            employee_id = int(request.GET['id'])
        except ValueError:
            return 'id should be a numeric value'

        try:
            e = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return 'user not found'

        result = {
            'first_name': e.first_name,
            'last_name': e.last_name,
            'department': e.department.name,
        }
        return result

    user_data = get_response_data(request)
    if isinstance(user_data, str):
        result = {
            'status': user_data,
            'data': None,
        }
    else:
        result = {
            'status': 'ok',
            'data': user_data,
        }

    return HttpResponse(json.dumps(result),
                        content_type='application/json')