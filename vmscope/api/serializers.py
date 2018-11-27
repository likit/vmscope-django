from rest_framework import serializers

from microscope.models import (MicroscopeSection, ParasiteComponent,
                               ArtifactComponent, ParasiteImage,
                               Parasite, Artifact, ParasiteComponent)


class ParasiteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParasiteImage
        fields = ('pk', 'image')


class ArtifactImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParasiteImage
        fields = ('pk', 'image')


class ParasiteSerializer(serializers.ModelSerializer):
    images = ParasiteImageSerializer(many=True, read_only=True)
    class Meta:
        model = Parasite
        fields = ('pk', 'genus', 'species', 'images')


class ArtifactSerializer(serializers.ModelSerializer):
    images = ArtifactImageSerializer(many=True, read_only=True)
    class Meta:
        model = Artifact
        fields = ('pk', 'group', 'images')


class ParasiteComponentSerializer(serializers.ModelSerializer):
    parasite = ParasiteSerializer(many=False, read_only=True)
    class Meta:
        model = ParasiteComponent
        fields = ('pk', 'number', 'parasite')


class ArtifactComponentSerializer(serializers.ModelSerializer):
    artifact = ArtifactSerializer(many=False, read_only=True)
    class Meta:
        model = ArtifactComponent
        fields = ('pk', 'number', 'artifact', 'oscillate', 'resizable')


class MicroscopeSectionSerializer(serializers.ModelSerializer):
    parasite_components = ParasiteComponentSerializer(many=True, read_only=False)
    artifact_components = ArtifactComponentSerializer(many=True, read_only=False)
    class Meta:
        model = MicroscopeSection
        fields = ('pk', 'name', 'desc', 'parasite_components', 'artifact_components')
