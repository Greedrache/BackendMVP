from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from ..models import Statement
from .serializers import StatementSerializer

class StatementListView(generics.ListAPIView):
    serializer_class = StatementSerializer

    def get_queryset(self):
        queryset = Statement.objects.all().order_by('created_at')
        limit = self.request.query_params.get('limit')
        if limit and limit.isdigit():
            return queryset[: int(limit)]
        return queryset[:15]


class EvaluateVotingView(APIView):
    def post(self, request):
        """
        Backend needs from Frontend YES NO NEUTRAL
        """
        
        user_answers = request.data.get('answers', {})
        if not user_answers:
            return Response(
                {"error": "No answers provided."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        statements = Statement.objects.filter(id__in=user_answers.keys())
        
        total_statements = statements.count()
        if total_statements == 0:
            return Response(
                {"error": "No matching statements found."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        matches = 0
        
        for statement in statements:
            user_answer = user_answers.get(str(statement.id))
            
            if user_answer == statement.mvp_position:
                matches += 1
                
        match_percentage = round((matches / total_statements) * 100, 2)
        
        return Response({
            "match_percentage": match_percentage,
            "total_questions": total_statements,
            "correct_matches": matches
        }, status=status.HTTP_200_OK)