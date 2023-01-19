class AuthRouter:
    route_app_labels = {'auth','contenttypes','sessions','admin',} # apps names
    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None    

    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None      
   

    def allow_migrate(self,db,app_label,model_name = None,**hints):    
        if app_label in self.route_app_labels:
            db = 'users_db'
            return db
        return None     


class BlueRouter:
    route_app_labels = {'auth','contenttypes','blue','sessions','admin'} # apps names
    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blues_db'
        return None    

    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blues_db'
        return None        

    def allow_relation(self, obj1, obj2, **hints):
        """
        Do not allow relations involving the remote database
        """
        # print("in allow relation")
        # if obj1._meta.app_label == Organization or \
        #    obj2._meta.app_label == Organization:
        #    return True
        # return None
        return True         

    def allow_migrate(self,db,app_label,model_name = None,**hints):    
        if app_label in self.route_app_labels:
            db = 'blues_db'
            return db
        return None     