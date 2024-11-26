from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='citizenship_with_passport',
            field=models.BooleanField(default=True),
        ),
    ]
