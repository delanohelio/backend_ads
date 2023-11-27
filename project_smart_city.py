from random import randrange
from datetime import timedelta
from datetime import datetime


def random_date():
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    start = datetime.strptime('1/1/2022 1:30 PM', '%d/%m/%Y %I:%M %p')
    end = datetime.strptime('31/8/2023 1:30 PM', '%d/%m/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

projects_comments = {
    "smart_grid":[
        {
            "name": "Noe Magalhães",
            "time": random_date(),
            "text": "A SmartCity foi muito importante na minha vida, sou prefeito de BlackWater e minha cidade melhorou consideravelmente depois que eu trouxe essa empresa para minha cidade."
        },
    ],
    "civil_construction": [
        {
            "name": "Claudio Barros",
            "time": random_date(),
            "text": "Essa empresa mudou minha vida, e dos meu eleitores sem eles não conseguiria chegar onde estou hoje, agradeço por tudo e super recomendo, abraços. "
        },
    ],
    "urban_mobility":[
        {
            "name": "Junior de Beto",
            "time": random_date(),
            "text": "Palmares melhorou um milhão de vezes depois do trabalho da SmartCity aqui."
        }
    ],
    "telecommunications":[
        {
            "name": "Claudio Barros",
            "time": random_date(),
            "text": "Essa empresa mudou minha vida, e dos meu eleitores sem eles não conseguiria chegar onde estou hoje, agradeço por tudo e super recomendo, abraços. "
        },
    ],
    "sanitary_system":[
        {
            "name": "Junior de Beto",
            "time": random_date(),
            "text": "Palmares melhorou um milhão de vezes depois do trabalho da SmartCity aqui."
        }
    ]
}