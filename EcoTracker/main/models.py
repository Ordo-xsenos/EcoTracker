from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def add_points(self, amount):
        self.points += amount
        self.save()

# models.py

from django.db import models
from django.conf import settings

class Achievement(models.Model):
    title       = models.CharField(max_length=100, help_text="Заголовок достижения")
    description = models.TextField(help_text="Описание достижения")
    icon        = models.CharField(
        max_length=50,
        help_text="CSS-класс иконки или emoji, например '🎖️' или имя FontAwesome-класса"
    )
    order       = models.PositiveIntegerField(
        default=0,
        help_text="Порядок вывода в списке"
    )
    class Meta:
        ordering = ['order']
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
    def __str__(self):
        return self.title
    def as_view(cls):
        pass

class UserAchievement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)    # ← добавляем это

class Tip(models.Model):
    title = models.CharField(max_length=100, help_text="Краткое название совета")
    icon = models.ImageField(upload_to='tips/icons/',
                             help_text="Минималистичная иконка для совета")
    text = models.TextField(help_text="Полный текст совета")
    order = models.PositiveIntegerField(default=0,
                                        help_text="Порядок отображения в ленте")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title