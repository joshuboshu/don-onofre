from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Servicio
from .serializers import ServicioSerializer
from rest_framework.permissions import IsAuthenticated 

# Create your views here.
def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})


class ServicioList(APIView):
    permission_classes = [IsAuthenticated]  # Permiso para solo usuarios autenticados

    def get(self, request):
        servicios = Servicio.objects.all()
        serializer = ServicioSerializer(servicios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)