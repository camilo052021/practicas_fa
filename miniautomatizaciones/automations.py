import calendar
from pathlib import Path

meses_anio = list(calendar.month_name[1:])
dias_semana = ['dia 1', 'dia 15', 'dia 22', 'dia 28']


for i, meses in enumerate(meses_anio):
    for dia in dias_semana:
        Path(f'miniautomatizaciones/2022/{i+1}.{meses}/{dia}').mkdir(parents=True, exist_ok=True)

