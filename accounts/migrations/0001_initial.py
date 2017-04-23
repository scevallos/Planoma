# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 21:18
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorProfile',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dept', models.CharField(choices=[(b'AFRI', b'Africana Studies'), (b'AMST', b'American Studies'), (b'ANTH', b'Anthropology'), (b'ARHI', b'Art History'), (b'ART', b'Art'), (b'ASAM', b'Asian American Studies'), (b'ASIA', b'Asian Studies'), (b'ASTR', b'Astronomy'), (b'BIOL', b'Biology'), (b'CGSC', b'Cognitive Science'), (b'CHEM', b'Chemistry'), (b'CHIN', b'Chinese'), (b'CHST', b'Chicana/o-Latina/o Studies'), (b'CLAS', b'Classics'), (b'CSCI', b'Computer Science'), (b'DANC', b'Dance'), (b'EA', b'Environmental Analysis'), (b'ECON', b'Economics'), (b'ENGL', b'English'), (b'FREN', b'French'), (b'GEOL', b'Geology'), (b'GERM', b'German Studies'), (b'GWS', b"Gender & Women's Studies"), (b'HIST', b'History'), (b'IR', b'International Relations'), (b'JAPN', b'Japanese'), (b'LAMS', b'Late Antique-Medieval Studies'), (b'LAST', b'Latin American Studies'), (b'LG', b'Linguistics'), (b'MATH', b'Mathematics'), (b'MES', b'Middle Eastern Studies'), (b'MOBI', b'Molecular Biology'), (b'MS', b'Media Studies'), (b'MUS', b'Music'), (b'NEUR', b'Neuroscience'), (b'PHIL', b'Philosophy, Politics & Economics'), (b'PHYS', b'Physics & Astronomy'), (b'POLI', b'Politics'), (b'PPA', b'Public Policy Analysis'), (b'PSYC', b'Psychology'), (b'REST', b'Russian & Eastern European Studies'), (b'RLIT', b'Romance Languages & Literatures'), (b'RLST', b'Religious Studies'), (b'RUSS', b'Russian'), (b'SOC', b'Sociology'), (b'SPAN', b'Spanish'), (b'STS', b'Science, Technology & Society'), (b'THEA', b'Theatre')], default='CSCI', max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dept', models.CharField(choices=[(b'AFRI', b'Africana Studies'), (b'AMST', b'American Studies'), (b'ANTH', b'Anthropology'), (b'ARHI', b'Art History'), (b'ART', b'Art'), (b'ASAM', b'Asian American Studies'), (b'ASIA', b'Asian Studies'), (b'ASTR', b'Astronomy'), (b'BIOL', b'Biology'), (b'CGSC', b'Cognitive Science'), (b'CHEM', b'Chemistry'), (b'CHIN', b'Chinese'), (b'CHST', b'Chicana/o-Latina/o Studies'), (b'CLAS', b'Classics'), (b'CSCI', b'Computer Science'), (b'DANC', b'Dance'), (b'EA', b'Environmental Analysis'), (b'ECON', b'Economics'), (b'ENGL', b'English'), (b'FREN', b'French'), (b'GEOL', b'Geology'), (b'GERM', b'German Studies'), (b'GWS', b"Gender & Women's Studies"), (b'HIST', b'History'), (b'IR', b'International Relations'), (b'JAPN', b'Japanese'), (b'LAMS', b'Late Antique-Medieval Studies'), (b'LAST', b'Latin American Studies'), (b'LG', b'Linguistics'), (b'MATH', b'Mathematics'), (b'MES', b'Middle Eastern Studies'), (b'MOBI', b'Molecular Biology'), (b'MS', b'Media Studies'), (b'MUS', b'Music'), (b'NEUR', b'Neuroscience'), (b'PHIL', b'Philosophy, Politics & Economics'), (b'PHYS', b'Physics & Astronomy'), (b'POLI', b'Politics'), (b'PPA', b'Public Policy Analysis'), (b'PSYC', b'Psychology'), (b'REST', b'Russian & Eastern European Studies'), (b'RLIT', b'Romance Languages & Literatures'), (b'RLST', b'Religious Studies'), (b'RUSS', b'Russian'), (b'SOC', b'Sociology'), (b'SPAN', b'Spanish'), (b'STS', b'Science, Technology & Society'), (b'THEA', b'Theatre')], default='CSCI', max_length=4)),
                ('year', models.IntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017)),
                ('adv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.AdvisorProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
