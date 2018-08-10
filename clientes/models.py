from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string


class Documento(models.Model):
    num_doc = models.CharField(max_length=14)

    def __str__(self):
        return self.num_doc


class Pessoa(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clientes_photos', null=True, blank=True)
    num_doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('deletar_clientes', 'Permissão para deletar clientes'),
        )

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super(Pessoa, self).save(*args, **kwargs)

        plain_text = render_to_string('clientes/emails/novo_cliente.txt')
        html_text = render_to_string('clientes/emails/novo_cliente.html')

        data = {'cliente': self.first_name}

        send_mail(
            'Um novo cliente foi cadastrado',
            'O nome dele é: %s' % self.first_name,
            'robsonsilv41-@gmail.com',
            ['robsonsilv41-@gmail.com'],
            html_message=html_text,
            fail_silently=False,
        )

    def __str__(self):
        return self.first_name + ' ' + self.last_name
