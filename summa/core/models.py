from django.db import models

class Filiado(models.Model):
    data_da_extracao = models.CharField('Data da extração', max_length=50, null=True, blank=True)
    hora_da_extracao = models.CharField('Hora da extração', max_length=50, null=True, blank=True)
    numero_da_incricao = models.CharField('Numero da inscrição', max_length=50, null=True, blank=True)
    nome_do_filiado = models.CharField('Nome do filiado', max_length=50, null=True, blank=True)
    sigla_do_partido = models.CharField('Sigla do partido', max_length=50, null=True, blank=True)
    nome_do_partido = models.CharField('Nome do partido', max_length=50, null=True, blank=True)
    uf = models.CharField('Unidade da federação', max_length=50, null=True, blank=True)
    codigo_do_municipio = models.CharField('Código do município', max_length=50, null=True, blank=True)
    nome_do_municipio = models.CharField('Nome do município', max_length=50, null=True, blank=True)
    zona_eleitoral = models.CharField('Zona eleitoral', max_length=50, null=True, blank=True)
    secao_eleitoral = models.CharField('Seção eleitoral', max_length=50, null=True, blank=True)
    data_da_filiacao = models.CharField('Data da filiação', max_length=50, null=True, blank=True)
    situacao_do_registro = models.CharField('Situação do registro', max_length=50, null=True, blank=True)
    tipo_do_registro = models.CharField('Tipo do registro', max_length=50, null=True, blank=True)
    data_do_processamento = models.CharField('Data do processamento', max_length=50, null=True, blank=True)
    data_da_desfiliacao = models.CharField('Data da desfiliação', max_length=50, null=True, blank=True)
    data_do_cancelamento = models.CharField('Data do cancelamento', max_length=50, null=True, blank=True)
    data_da_regularizacao = models.CharField('Data da regularização', max_length=50, null=True, blank=True)
    motivo_do_cancelamento = models.CharField('Motivo do cancelamento', max_length=50, null=True, blank=True)


    class Meta:
        ordering=('nome_do_filiado',)
        
    def __str__(self):
        return self.nome_do_filiado
