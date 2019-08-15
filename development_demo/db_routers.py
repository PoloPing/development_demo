
APP_DB_MAPPING_TABLE = {
    'user': 'default',
    'mongo_test_app': 'mongo',
    'admin': 'default',
    'auth': 'default',
    'contenttypes': 'default',
    'sessions': 'default',
}


class ModelMetaRouter(object):
    def db_for_read(self, model, **hints):
        return APP_DB_MAPPING_TABLE.get(model._meta.app_label, None)

    def db_for_write(self, model, **hints):
        return APP_DB_MAPPING_TABLE.get(model._meta.app_label, None)

    def allow_relation(self, obj1, obj2, **hints):
        # only allow relations within a single database
        if APP_DB_MAPPING_TABLE.get(obj1._meta.app_label, None) == \
           APP_DB_MAPPING_TABLE.get(obj2._meta.app_label, None):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in APP_DB_MAPPING_TABLE.keys():
            return APP_DB_MAPPING_TABLE.get(app_label) == db

        return False