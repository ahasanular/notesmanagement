from rest_framework.response import Response        # importing Response to give a response for the request
from rest_framework.generics import CreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import json
from .models import ContentManagement

class AddNotesApi(CreateAPIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            feedback = {}

            # if not request.user or request.user == "":
            #     feedback['message'] = "No user found for the Request !"
            #     feedback['status'] = HTTP_400_BAD_REQUEST
            #     return Response(feedback)

            if 'note_content' not in data or data['note_content'] == "":
                feedback['message'] = "empty note cant be added !"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)

            heading = data['note_content'][:50]
            heading += "..."

            content = ContentManagement()

            content.heading = heading
            content.body = data['note_content']
            content.save()

            feedback['message'] = "successful !"
            feedback['status'] = HTTP_200_OK
            return Response(feedback)

        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_400_BAD_REQUEST
            return Response(feedback)

from .serializers import NoteContentSerializer

class GetNotesApi(CreateAPIView):
    permission_classes = []
    def get(self, request):
        try:
            data = ContentManagement.objects.filter(is_archived=False).all()
            data = NoteContentSerializer(data, many=True).data
            return Response(data)

        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_400_BAD_REQUEST
            return Response(feedback)