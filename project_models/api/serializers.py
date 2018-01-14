from rest_framework import serializers
from project_models.models import Employee, Department
from rest_framework.authentication import TokenAuthentication


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'surname'
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id',
            'name'
        ]


class QueryStringBasedTokenAuthentication(TokenAuthentication):

    # Extend the TokenAuthentication class to support querystring authentication
    # in the form of "http://www.example.com/?auth_token=<token_key>"

    def authenticate(self, request):
        # Check if 'token_auth' is in the request query params.
        # Give precedence to 'Authorization' header.
        if 'auth_token' in request.query_params and \
                        'HTTP_AUTHORIZATION' not in request.META:
            return self.authenticate_credentials(request.query_params.get('auth_token'))
        else:
            return super(QueryStringBasedTokenAuthentication, self).authenticate(request)



"""
class QueryStringBasedTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        key = request.query_params.get('auth_token').strip()
        if key:
            return self.authenticate_credentials(key)
        else:
            return super(QueryStringBasedTokenAuthentication, self).authenticate(request)

"""