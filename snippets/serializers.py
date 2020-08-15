"""
# using model serializer

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User 


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'lineous','language','style', 'owner']


    def create(self, validated_data):
        # create and return  a new snippet instance given the validated data
        return Snippet.objects.create(**validated_data)


    def update(self, instance, validated_data):
        # update and return an existing snippet instance, given the validated data
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code),
        instance.lineous = validated_data.get('lineous', instance.lineous),
        instance.language = validated_data.get('language', instance.language),
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


"""
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User 


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    # Using Basic serializer class
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    lineous = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'lineous','language','style', 'owner', 'highlight']


    def create(self, validated_data):
        # create and return  a new snippet instance given the validated data
        return Snippet.objects.create(**validated_data)


    def update(self, instance, validated_data):
        # update and return an existing snippet instance, given the validated data
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code),
        instance.lineous = validated_data.get('lineous', instance.lineous),
        instance.language = validated_data.get('language', instance.language),
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']