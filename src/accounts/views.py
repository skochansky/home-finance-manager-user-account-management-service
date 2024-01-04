from http import HTTPStatus

from django.http import JsonResponse


def test_endpoint(request):
    return JsonResponse(
        {"message": "correctly connected to the hfm-user-account-management service"},
        status=HTTPStatus.OK,
    )
