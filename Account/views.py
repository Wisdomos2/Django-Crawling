from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer
from rest_framework import status


# Create your views here.

# 사용자 CRUD
class AccountView(APIView):
    """
    POST /account
    """

    def post(self, request):
        # Request의 data를 AccountSerializer로 변환
        account_Serializer = AccountSerializer(data=request.data)

        if account_Serializer.is_valid():
            # UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            account_Serializer.save()
            # client에게 JSON response 전달
            return Response(account_Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(account_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    GET /account
    GET /account/{account_id} .. PK
    """

    # *args : Tuple
    # **kwarg : Dict
    def get(self, request, **kwargs):
        if kwargs.get('account_Id') is None:
            account_Queryset = Account.objects.all()
            account_Queryset_serializer = AccountSerializer(account_Queryset, many=True)
            return Response(account_Queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            account_Id = kwargs.get('account_Id')
            account_Serializer = AccountSerializer(Account.objects.get(id=account_Id))  # id에 해당하는 User의 정보를 불러온다
            return Response(account_Serializer.data, status=status.HTTP_200_OK)

    """
    PUT /account/{account}
    """

    def put(self, request, **kwargs):
        if kwargs.get('account_Id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            account_Id = kwargs.get('account_Id')
            account_Object = Account.objects.get(id=account_Id)

            update_Account_Serializer = AccountSerializer(account_Object, data=request.data)
            print(update_Account_Serializer)
            # is_valid() 에서 model에 기술 된 내용을 바탕으로 유효성 검사를 진행 함. (max_length, 등등..)
            if update_Account_Serializer.is_valid():
                update_Account_Serializer.save()
                return Response(update_Account_Serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    """
    DELETE /account/{account}
    """

    def delete(self, request, **kwargs):
        if kwargs.get('account_Id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            account_Id = kwargs.get('account_Id')
            account_Object = Account.objects.get(id=account_Id)
            account_Object.delete()
            return Response("Delete ok", status=status.HTTP_200_OK)
