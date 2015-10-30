from django.db import models
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your models here.

class mc_table_model(models.Model):
    mod_list = (())
    pack_version = None
    mc_version = None
    with open('./mousweb/static/mousweb/mc/ModList.txt') as f:
        pack_version = f.readline().strip()
        mc_version = f.readline().strip()
        for line in f.readlines():
            parts = line.split('=')
            #mod_dict[ parts[0].strip() ] = parts[1].strip()
            mod_list = mod_list + ((parts[0].strip(), parts[1].strip()),)

    download_path = static('mousweb/mc/MousLan-' + pack_version + '.zip')

