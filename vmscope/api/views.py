from rest_framework import generics


from microscope.models import MicroscopeSection, ParasiteComponent
from .serializers import MicroscopeSectionSerializer, ParasiteComponentSerializer


class MicroscopeSectionListView(generics.ListAPIView):
    queryset = MicroscopeSection.objects.all()
    serializer_class = MicroscopeSectionSerializer


class MicroscopeSectionDetailView(generics.RetrieveAPIView):
    queryset = MicroscopeSection.objects.all()
    serializer_class = MicroscopeSectionSerializer


class ParasiteComponentDetailView(generics.RetrieveAPIView):
    queryset = ParasiteComponent.objects.all()
    serializer_class = ParasiteComponentSerializer
