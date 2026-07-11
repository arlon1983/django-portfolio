from django.db import models


class Service(models.Model):
    icon = models.CharField(max_length=10, help_text="Emoji or short glyph")
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=280)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=280)
    tech_stack = models.CharField(max_length=200, help_text="Comma-separated, e.g. Django, HTMX, PostgreSQL")
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    project_type = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} <{self.email}>"
