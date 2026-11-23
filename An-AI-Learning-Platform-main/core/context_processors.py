from .models import UserProfile

def user_profile_context(request):
    if request.user.is_authenticated:
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        return {
            'user_profile': profile,
            'user_rank_tier': profile.calculate_rank_tier(),
            'user_rank_title': profile.get_title(),
        }
    return {
        'user_profile': None,
        'user_rank_tier': 1,
        'user_rank_title': 'Visitor',
    }

