from django.db import models

"""
CREATE TABLE FUNCIONARIO (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME VARCHAR(255) UNIQUE,
    CPF VARCHAR(11) UNIQUE NOT NULL,
    CARGO VARCHAR(255)
);
"""


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    nome = models.CharField(max_length=255, db_column='NOME', null=False)
    cpf = models.CharField(max_length=11, db_column='CPF', unique=True, null=False)
    cargo = models.CharField(max_length=255, db_column='CARGO')
    salario = models.FloatField(db_column='SALARIO', default=0.0)

    class Meta:
        db_table = 'FUNCIONARIO'

    def salarioX2(self):
        return self.salario * 2


class Produtos(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    nome = models.CharField(max_length=255, db_column='NOME', null=False)
    numero = models.IntegerField(unique=True, db_column='NUMERO')  # GTIN
    preco = models.FloatField(db_column='PRECO', default=0.0)

    class Meta:
        db_table = 'Produtos'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
