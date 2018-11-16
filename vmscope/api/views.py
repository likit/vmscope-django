from rest_framework import generics


from microscope.models import MicroscopeSection
from .serializers import MicroscopeSectionSerializer


class MicroscopeSectionListView(generics.ListAPIView):
    queryset = MicroscopeSection.objects.all()
    serializer_class = MicroscopeSectionSerializer


class MicroscopeSectionDetailView(generics.RetrieveAPIView):
    queryset = MicroscopeSection.objects.all()
    serializer_class = MicroscopeSectionSerializer
