from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from UserGroup.serializer import GroupInfoSerializer,GroupMemberSerializer
from UserGroup.models import GroupInfo

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

def test(request):
    return HttpResponse("Hello world")

def url_test(request):
    return HttpResponse("This is new World")

def docker_test(request):
    return HttpResponse("Docker testing")

def cicd_test(request):
    return HttpResponse("CICD testing")

# Create your views here.
"""
The Class GroupInfoView will provide the get, post, delete API for the GroupInfo table. 
"""
class GroupInfoView(APIView):
    #serializer_class = GroupInfoSerializer

    def get_serializer(self):
        return GroupInfoSerializer()

    """
    This is API Get request where the data of all the groups will returned.
    """
    def get(self, request):
        groups = GroupInfo.objects.all()
        serializer = GroupInfoSerializer(groups, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    """
    This is API Post request, it is used to create the new groups.
    """

    def post(self,request):
        groups = request.data
        serializer = GroupInfoSerializer(data=groups)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message":"Successfully created"},status=status.HTTP_201_CREATED)

    """
    This is API Delete request, API is used to delete the group.
    """
    def delete(self,request):
        name = request.data.get('group_name')
        try:
            g_name = GroupInfo.objects.get(group_name=name)
            if g_name:
                g_name.delete()
                return Response({"Message":"Data is deleted"},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"message": "Object is not present in Database"},status=status.HTTP_404_NOT_FOUND)

"""
The Class GroupMemberView will provide the get, post, delete API for the GroupInfo table. 
"""

class GroupMemberView(APIView):
    #serializer_class = GroupMemberSerializer
    def get_serializer(self):
        return GroupMemberSerializer()
    """
    This is used to set the 
    """
    @staticmethod
    def set_dynamic_fields(*args):
        c = GroupMemberSerializer
        c.Meta.fields = (args)
        return c
    """
    This is API Get request is used to get the data of requested Group Members.
    """
    def get(self,request,group_name):
        grp_emp_list = get_object_or_404(GroupInfo, group_name=group_name)
        serializer = self.set_dynamic_fields('ass_emps', 'group_name')
        ser=serializer(grp_emp_list)
        return Response(ser.data, status=status.HTTP_200_OK)

    """
    This is API Put request is used to update the Employees of requested Group.
    """
    def put(self,request,group_name):

        grp = get_object_or_404(GroupInfo, group_name=group_name)
        serializer = GroupMemberSerializer(grp, data=request.data, partial = True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message":"Successfully Updated the group"},status=status.HTTP_201_CREATED)

    """
    This is API delete request is used to delete the Employees of requested Group.
    """
    def delete(self,request,group_name):
        group = get_object_or_404(GroupInfo,group_name=group_name)
        ass_emps = request.data.get('ass_emps')
        group_ass_emps = group.ass_emps

        for emp in ass_emps:
            group_ass_emps.remove(emp)
        serializer = GroupMemberSerializer(group, data={"ass_emps":group_ass_emps})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message":"Successfully deleted"},status=status.HTTP_204_NO_CONTENT)