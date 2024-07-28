from rest_framework import serializers

from reviews.models import Category, Survey

class CategorySerializer(serializers.ModelSerializer):
      class Meta:
            model = Category
            fields = '__all__'
            
class SurveySerializer(serializers.ModelSerializer):
      categories = serializers.ListField(child=serializers.CharField(), write_only=True)

      class Meta:
            model = Survey
            fields = '__all__'
            
      def create(self, validated_data):
        category_names = validated_data.pop('categories')
        survey = Survey.objects.create(**validated_data)
        if category_names is not None:
            for name in category_names:
                category, created = Category.objects.get_or_create(title=name)
                survey.categories.add(category)
        return survey

      def update(self, instance, validated_data):
            category_names = validated_data.pop('categories', None)
            instance = super().update(instance, validated_data)
            if category_names is not None:
                instance.categories.clear()
                for name in category_names:
                    category, created = Category.objects.get_or_create(title=name)
                    instance.categories.add(category)
            return instance