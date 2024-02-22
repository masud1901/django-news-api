from datetime import datetime
from django.utils.timesince import timesince

from rest_framework import serializers
from news.models import Article, Reporter





class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = ReporterSerializer()

    class Meta:
        model = Article
        fields = "__all__"

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        return timesince(publication_date, now)

    def validate(self, data):
        """checks that description and title are different"""
        if data["description"] == data["title"]:
            raise serializers.ValidationError(
                {"error": "description and title cannot be the same"}
            )
        return data

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                {"error": "title must be at least 5 characters"}
            )
        return value


class ReporterSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Reporter
        fields = "__all__"

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.author = validated_data.get("author", instance.author)
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)
#         instance.body = validated_data.get("body", instance.body)
#         instance.location = validated_data.get("location", instance.location)
#         instance.publication_date = validated_data.get(
#             "publication_date", instance.publication_date
#         )
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         """checks that description and title are different"""
#         if data["description"] == data["title"]:
#             raise serializers.ValidationError(
#                 {"error": "description and title cannot be the same"}
#             )
#         return data

#     def validate_title(self, value):
#         if len(value) < 5:
#             raise serializers.ValidationError(
#                 {"error": "title must be at least 5 characters"}
#             )
#         return value
