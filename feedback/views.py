from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Feedback

def feedback_form(request):
    return render(request, 'forms.html')

def enviar_feedback(request):
    if request.method == 'POST':
        # Coletar dados do formulário
        nome = request.POST.get('nome')
        recomendacao = request.POST.get('recomendacao')
        comentarios = request.POST.get('comentarios')
        
        # Criar novo objeto Feedback
        Feedback.objects.create(
            nome=nome,
            recomendacao=recomendacao,
            comentarios=comentarios
        )
        
        # Redirecionar para página de agradecimento
        return redirect('thank_you')
    
    # Se não for POST, redirecionar para o formulário
    return redirect('feedback_form')

def thank_you(request):
    return render(request, 'thank_you.html')

class RespostasPesquisaView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Feedback
    template_name = 'respostas.html'
    context_object_name = 'feedbacks'
    ordering = ['-data_criacao']
    paginate_by = 10
    
    # Redireciona para login se não estiver autenticado
    login_url = '/admin/login/'
    
    # Verifica se o usuário é superusuário (admin)
    def test_func(self):
        return self.request.user.is_superuser