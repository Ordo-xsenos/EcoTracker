from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import UserAchievement,UserProfile,Achievement,Tip
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

def home(request):
    return render(request, 'index.html')  # Отдаём шаблон index.html

def award_achievement(user, code):
    # Ищем определение достижения (менеджер объекта)
    achievement = Achievement.objects.get(code=code)
    # Через менеджер UserAchievement создаём или возвращаем существующую запись
    user_achievement, created = UserAchievement.objects.get_or_create(
        user=user,
        achievement=achievement
    )
    if created:
        # Здесь можно добавить логику при первом получении значка
        # Например, отправить уведомление или залогировать событие
        pass
    return user_achievement

def complete_survey(request, survey_id):
    # логика проверки заполнения
    profile = get_object_or_404(UserProfile, user=request.user)
    profile.add_points(10)  # начисляем 10 баллов
    return redirect('survey_thanks')

def tracker(request):
    return render(request,'tracker.html')

def tips_view(request):
    tips = Tip.objects.all()   # или, если нужен только активные: .filter(is_active=True)
    return render(request, 'tips.html', {'tips': tips})

def achievements_view(request):
    # Если аноним — показываем приглашение
    if not request.user.is_authenticated:
        return render(request, 'achievements.html', {
            'show_login_prompt': True,
        })

    # Достаём все достижения из базы
    all_achievements = list(Achievement.objects.all())

    # Список ID выполненных пользователем достижений
    completed_ids = set(
        UserAchievement.objects
            .filter(user=request.user, completed=True)
            .values_list('achievement_id', flat=True)
    )

    # Формируем список объектов с доп. атрибутами
    achievements = []
    for ach in all_achievements:
        # добавляем поля, которые нужны в шаблоне
        ach.completed = ach.id in completed_ids
        ach.date_awarded = None
        if ach.completed:
            ua = UserAchievement.objects.get(
                user=request.user,
                achievement=ach
            )
            ach.date_awarded = ua.awarded_at
        achievements.append(ach)

    # Считаем общее число выполненных
    total_score = len([a for a in achievements if a.completed])

    return render(request, 'achievements.html', {
        'achievements': achievements,
        'total_score': total_score,
        'show_login_prompt': False,
    })

class Achievements(ListView):
    model = UserAchievement            # или Achievement, если нужно выводить все
    template_name = 'achievements.html'
    context_object_name = 'user_achievements.html'

    def get_queryset(self):
        # показывать только достижения текущего пользователя
        return UserAchievement.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['achievements'] = UserAchievement.objects.filter(user=self.request.user)
        completed = ctx['achievements'].filter(completed=True).count()
        ctx['total_score'] = completed * 100
        return ctx

def sharing_view(request):
    return render(request, 'sharing.html')
