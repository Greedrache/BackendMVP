from django.db import models

class Thema(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "theme"
        verbose_name_plural = "themes"

    def str(self):
        return self.name


class These(models.Model):
    # Definition der Antwortmöglichkeiten für die MVP
    POSITION_CHOICES = [
        ('JA', 'Ja'),
        ('NEIN', 'Nein'),
        ('NEUTRAL', 'Neutral'),
    ]

    thema = models.ForeignKey(Thema, on_models=models.CASCADE, related_name='thesen')
    titel = models.CharField(max_length=200, help_text="Kurztitel, z.B. '4-Tage-Woche' oder 'Massenüberwachung'")
    text = models.TextField(help_text="Die eigentliche These, der der Nutzer zustimmen oder widersprechen kann.")

    mvp_position = models.CharField(
        max_length=7, 
        choices=POSITION_CHOICES, 
        default='NEUTRAL',
        help_text="Die offizielle Position der MVP zu dieser These."
    )

    begruendung = models.TextField(
        help_text="Der gestern optimierte Text aus dem Wahlprogramm, warum die MVP so positioniert ist."
    )
    erstellt_am = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "These"
        verbose_name_plural = "Thesen"
        ordering = ['erstellt_am']

    def str(self):
        return f"{self.thema.name} - {self.titel}"