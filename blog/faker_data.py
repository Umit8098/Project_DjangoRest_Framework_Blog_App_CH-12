from .models import Category, Post
from faker import Faker

def run():
    fake = Faker(['tr-TR'])
    categories = (
        "Life",
        "Science",
        "Politics",
        "Sports"
    )

    for category in categories:
        new_category = Category.objects.create(name = category)
        for _ in range(30):  # neden _? normalde i yazıyorduk? döngünün içinde i'yi kullanmadığımız zamanlarda _ kullanırız, i yazmış olsaydık döngünün içinde i'yi kullanmamız gerekirdi.
            Post.objects.create(category = new_category, title = fake.name(), content = fake.text())
    
    print('Finished')
