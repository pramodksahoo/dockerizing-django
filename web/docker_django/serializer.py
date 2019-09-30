from UserGroup.models import GroupInfo
from rest_framework import serializers

"""
Creating a GroupInfoSerializer
"""
class GroupInfoSerializer(serializers.ModelSerializer):
    ass_emps = serializers.ListField()
    class Meta:
        model = GroupInfo
        exclude = ['created', 'modified','id']

"""
Creating a GroupMemberSerializer
"""
class GroupMemberSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(read_only=True)
    ass_emps = serializers.ListField()
    class Meta:
        model = GroupInfo
        fields = '__all__'