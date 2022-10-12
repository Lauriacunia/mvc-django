from django.shortcuts import render

# Create your views here.

members = [
    {
        'name': 'Santiago',
        'age': 33,
        'birth_date': '1987-06-19',
        'thumbnail': 'https://xsgames.co/randomusers/assets/avatars/male/29.jpg'
    },
    {
        'name': 'Catalina',
        'age': 31,
        'birth_date': '1989-08-12',
        'thumbnail': 'https://xsgames.co/randomusers/assets/avatars/female/20.jpg'
    },
    {
        'name': 'Micaela',
        'age': 22,
        'birth_date': '2005-11-01',
        'thumbnail': 'https://xsgames.co/randomusers/assets/avatars/female/69.jpg'
    },
    {
        'name': 'Rodrigo',
        'age': 22,
        'birth_date': '2000-07-05',
        'thumbnail': 'https://xsgames.co/randomusers/assets/avatars/male/76.jpg'
    }
]

def show_family_members(request):
    return render(request, 'family.html', {'members': members})
