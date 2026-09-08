from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Crea el usuario administrador con usuario admin y contraseña admin123"

    def handle(self, *args, **options):
        User = get_user_model()
        user, created = User.objects.get_or_create(username="admin")

        if created:
            user.set_password("admin123")
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS("Usuario admin creado correctamente."))
        else:
            user.set_password("admin123")
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.WARNING("El usuario admin ya existía, se actualizó la contraseña a admin123."))

        self.stdout.write("Credenciales: usuario=admin, contraseña=admin123")
