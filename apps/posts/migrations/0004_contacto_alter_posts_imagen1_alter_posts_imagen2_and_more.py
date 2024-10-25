# Generated by Django 5.1.2 on 2024-10-24 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_posts_imagen1_alter_posts_imagen2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='imagen1',
            field=models.ImageField(default='media/posts/default.png', upload_to='media/posts'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='imagen2',
            field=models.ImageField(default='media/posts/default.png', upload_to='media/posts'),
        ),
        migrations.AlterField(
            model_name='user',
            name='icono',
            field=models.ImageField(blank=True, default='media/usuarios/default.png', null=True, upload_to='media/usuarios'),
        ),
    ]
