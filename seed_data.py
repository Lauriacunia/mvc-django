from family.models import FamilyMember

description_1 = "El es mi papá. Trabaja como chef en un prestigioso restaurante de la ciudad. Es muy amable y siempre está dispuesto a ayudar a los demás."
description_2 = "Ella es mi mamá. Es docente universitaria. Ama las plantas y los animales. Es muy divertida y siempre está sonriendo."
description_3 = "Ella es mi hermana. Estudia música en el conservatorio. Su sueño es convertirse en una estrella del rock."
description_4 = "El es mi tío. Trabaja en sistemas. Siempre está muy ocupado. Cuando nos visita jugamos a la play. Siempre le gano."

FamilyMember(name='Santiago', age=36, birth_date='1986-10-15', description=description_1,           
             thumbnail='https://xsgames.co/randomusers/assets/avatars/male/29.jpg').save()
FamilyMember(name='Catalina', age=31, birth_date='1990-12-08', description=description_2,
             thumbnail='https://xsgames.co/randomusers/assets/avatars/female/20.jpg').save()
FamilyMember(name='Micaela', age=23, birth_date='1998-11-01', description=description_3,
             thumbnail='https://xsgames.co/randomusers/assets/avatars/female/69.jpg').save()
FamilyMember(name='Rodrigo', age=29, birth_date='1993-07-05', description=description_4,
             thumbnail='https://xsgames.co/randomusers/assets/avatars/male/76.jpg').save()


print('👨‍👩‍👧‍👧 Se han creado los miembros de la familia')

# correr script en la terminal
# python manage.py shell < seed_data.py
