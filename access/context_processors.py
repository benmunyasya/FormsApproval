from viewflow.models import Task
from .flows import RMS_ApplicationFlow


def tasks_counts(request):
    if request.user.is_authenticated:
        return {
            'inbox_count': Task.objects.inbox([RMS_ApplicationFlow], request.user).count(),
            'queue_count': Task.objects.queue([RMS_ApplicationFlow], request.user).count()
        }
    return {}
