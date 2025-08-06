from celery import shared_task
from django.utils import timezone
from django_tenants.utils import schema_context, get_tenant_model
from MailTask.models import ScheduledTask

@shared_task
def dispatcher_task():
    TenantModel = get_tenant_model()
    tenants = TenantModel.objects.all()

    for tenant in tenants:
        with schema_context(tenant.schema_name):
            due_tasks = ScheduledTask.objects.filter(run_at__lte=timezone.now(), is_executed=False)
            for scheduled in due_tasks:
                task_map = {
                    'Task1': Task1,
                    'Task2': Task2,
                    'Task3': Task3,
                    'Task4': Task4,
                    'Task5': Task5,
                }
                task_func = task_map.get(scheduled.task_name)
                if task_func:
                    task_func.apply_async(args=[tenant.schema_name])
                    scheduled.is_executed = True
                    scheduled.save()

@shared_task
def Task1(schema_name):
    print(f"Task 1 {schema_name}")

@shared_task
def Task2(schema_name):
    print(f"Task 2 {schema_name}")

@shared_task
def Task3(schema_name):
    print(f"Task 3 {schema_name}")

@shared_task
def Task4(schema_name):
    print(f"Task 4 {schema_name}")

@shared_task
def Task5(schema_name):
    print(f"Task 5 {schema_name}")