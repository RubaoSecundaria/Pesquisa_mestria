from django.db import models

class Feedback(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    recomendacao = models.IntegerField(help_text="Escala de 0 a 10 para NPS")
    comentarios = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback de {self.nome} - {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"
        
    def get_categoria_nps(self):
        """Retorna a categoria do NPS: Detrator, Neutro ou Promotor"""
        if self.recomendacao <= 6:
            return "Pouco provável"
        elif self.recomendacao <= 8:
            return "Indiferente"
        else:
            return "Muito Provável"