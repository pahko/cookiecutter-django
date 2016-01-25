import cbs
import os


class BaseSettings(cbs.BaseSettings):
    PROJECT_NAME = '{{cookiecutter.project_name}}'

    @cbs.env(key='DJANGO_SECRET_KEY')
    def SECRET_KEY(self):
        return 'TESTING LOCALLY'

    @property
    def INSTALLED_APPS(self):
        contrib = super(BaseSettings, self).INSTALLED_APPS
        third_party = ()
        local = ()

        return contrib + third_party + local

    @property
    def DATABASES(self):
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(self.BASE_DIR, 'db.sqlite3'),
            }
        }


class LocalSettings(BaseSettings):
    DEBUG = True


class StagingSettings(BaseSettings):
    pass


class ProductionSettings(BaseSettings):
    ALLOWED_HOSTS = []


MODE = os.environ.get('DJANGO_MODE', 'Local')
cbs.apply('{}Settings'.format(MODE.title()), globals())
