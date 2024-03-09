from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subject, Ticket
from .serializers import SubjectSerializer, TicketSerializer

class SubjectListView(APIView):
    def get(self, request, format=None):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Get all the tickets
class TicketListView(APIView):
    def get(self, request, format=None):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create a ticket 
class TicketCreateAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        from Users.models import Student, Tutor
        serializer = TicketSerializer(data=request.data)
        
        if serializer.is_valid():
            # Extract `student_id`, `tutor_id`, and `subject_id` from the request
            student_id = request.data.get('student')
            tutor_id = request.data.get('tutor')
            subject_id = request.data.get('subject')

            subject = Subject.objects.get(id=subject_id)
            student = Student.objects.get(id=student_id)
            tutor = Tutor.objects.get(id=tutor_id)

            # Manually set the student, tutor, and subject before saving
            ticket = serializer.save(student=student, tutor=tutor, subject=subject)
            tutor.tickets.add(ticket)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)