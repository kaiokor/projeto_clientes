from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo"})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve conter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir este modelo: 11 91234-1234"})
        return data