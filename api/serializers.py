from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Genre


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    rating = serializers.DecimalField(
        read_only=True, max_digits=4, decimal_places=2, coerce_to_string=False
    )

    class Meta:
        fields = '__all__'
        read_only_fields = (
            'id',
            'name',
            'year',
            'description',
        )
        model = Title


class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all(), required=False
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug', queryset=Genre.objects.all(), many=True
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('id',)
        model = Title

    def to_representation(self, instance):
        return TitleReadSerializer(instance).data


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
    )

    def validate(self, data, *args, **kwargs):
        if self.context['request'].method == 'POST':
            title_id = int(
                self.context['request']
                .parser_context.get('kwargs')
                .get('title_id')
            )
            title = get_object_or_404(Title, id=title_id)
            if title.reviews.filter(
                author=self.context['request'].user
            ).exists():
                raise serializers.ValidationError('У вас уже есть отзыв')
        return data

    class Meta:
        fields = ('id', 'score', 'author', 'text', 'pub_date')
        read_only_fields = (
            'id',
            'pub_date',
        )
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
    )

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date')
        read_only_fields = (
            'id',
            'pub_date',
        )
        model = Comment
