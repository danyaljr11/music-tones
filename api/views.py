from rest_framework import generics
from rest_framework.response import Response

from .models import Section, Item
from .serializers import Sections_Serializer, Items_Serializer


class SectionList(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = Sections_Serializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'sections': serializer.data})


class ItemList(generics.ListAPIView):
    serializer_class = Items_Serializer

    def get_queryset(self):
        queryset = Item.objects.all()
        section_id = self.kwargs.get('pk', None)
        if section_id is not None:
            queryset = queryset.filter(section__pk=section_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'items': serializer.data})
