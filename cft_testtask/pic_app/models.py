from django.db import models

ANALYSIS_MODES = [
    ('WB', 'Черные vs Белые'),
    ('HEX', 'Цвет по HEX-коду'),
]

class Pictures(models.Model):
    # name = models.CharField(max_length=50)
    src = models.ImageField("Выберите картинку", upload_to='images/')
    mode = models.CharField("Режим", max_length=30, choices=ANALYSIS_MODES, default='HEX')
    color = models.CharField("Код цвета #", max_length=6, blank=True)
