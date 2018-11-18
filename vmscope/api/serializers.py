from rest_framework import serializers

from microscope.models import (MicroscopeSection, ParasiteComponent,
                                ArtifactComponent, ParasiteImage,
                               ParasiteItem, ArtifactItem)


class ParasiteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParasiteImage
        fields = ('image',)


class ArtifactImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParasiteImage
        fields = ('image',)


class ArtifactItemSerializer(serializers.ModelSerializer):
    item = ArtifactImageSerializer(read_only=True)
    class Meta:
        model = ArtifactItem
        fields = ('pk', 'item')


class ParasiteItemSerializer(serializers.ModelSerializer):
    item = ArtifactImageSerializer(read_only=True)
    class Meta:
        model = ParasiteItem
        fields = ('pk', 'item')


class MicroscopeSectionSerializer(serializers.ModelSerializer):
    parasites = ParasiteItemSerializer(many=True, read_only=True)
    artifacts = ArtifactItemSerializer(many=True, read_only=True)
    class Meta:
        model = MicroscopeSection
        fields = ('name', 'desc', 'parasites', 'artifacts')
