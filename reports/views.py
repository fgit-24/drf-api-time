from rest_framework import generics, permissions
from .models import Report
from .serializers import ReportSerializer

class ReportList(generics.ListCreateAPIView):
    """
    Returns a list of all reports.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Manage individual report actions (retrieve, update, delete).
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer