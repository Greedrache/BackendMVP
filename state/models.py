from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "theme"
        verbose_name_plural = "themes"

    def __str__(self):
        return self.name


class Statement(models.Model):
    POSITION_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('NEUTRAL', 'Neutral'),
    ]

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='statements')
    title = models.CharField(max_length=200, help_text="Short title of the statement/question")
    text = models.TextField(help_text="The actual statement the user can agree or disagree with")
    
    mvp_position = models.CharField(
        max_length=7, 
        choices=POSITION_CHOICES, 
        default='NEUTRAL',
        help_text="The official position of the MVP party"
    )
    
    explanation = models.TextField(
        help_text="The background text explaining why the party chose this position"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "statement"
        verbose_name_plural = "statements"
        ordering = ['created_at']

    def __str__(self):
        return f"{self.theme.name} - {self.title}"