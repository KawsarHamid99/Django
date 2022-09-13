from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete,pre_migrate,post_migrate

from django.core.signals import request_finished,request_started,got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in,sender=User)
def login_succes(sender,request,user,**kwargs):
    print("-----------------------------------------------------")
    print("Logged-in Signal... Run Intro..")
    print("Sender: ",sender )
    print("Request: ",request)
    print("User: ",user)
    print(f"Kwargs: {kwargs}")
#user_logged_in.connect(login_succes,sender=User)

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("-----------------------------------------------------")
    print("Logged-out Signal... Run Intro..")
    print("Sender: ",sender )
    print("Request: ",request)
    print("User: ",user)
    print(f"Kwargs: {kwargs}")
#user_logged_out.connect(log_out,sender=User)


@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("-----------------------------------------------------")
    print("Login failed Signal... Run Intro..")
    print("Sender: ",sender )
    print("Request: ",request)
    print("Credentials: ",credentials)
    print(f"Kwargs: {kwargs}")
#user_login_failed.connect(login_failed)


@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("-----------------------------------------------------")
    print("Pre Save signal Signal... Run Intro..")
    print("Sender: ",sender )
    print("Instance: ",instance)
    print(f"Kwargs: {kwargs}")
#pre_save.connect(at_beginning_save,sender=User)

@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("-----------------------------------------------------")
        print("Post Save signal Signal... ")
        print("New Record")
        print("Sender: ",sender )
        print("Instance: ",instance)
        print("Created: ",created)
        print(f"Kwargs: {kwargs}")
    else:
        print("-----------------------------------------------------")
        print("Post Save signal Signal..")
        print("updated..")
        print("Sender: ",sender )
        print("Instance: ",instance)
        print("Created: ",created)
        print(f"Kwargs: {kwargs}")
#post_save.connect(at_ending_save,sender=User)

@receiver( pre_delete,sender=User)
def at_beginning_delete(sender,instance,**kwargs):
    print("-----------------------------------------------------")
    print("Pre delete signal ...")
    print("Sender: ",sender )
    print("Instance: ",instance)
    print(f"Kwargs: {kwargs}")
#pre_delete.connect(at_beginning_delete,sender=User)

@receiver( post_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("-----------------------------------------------------")
    print("Post delete signal ...")
    print("Sender: ",sender )
    print("Instance: ",instance)
    print(f"Kwargs: {kwargs}")
#post_delete.connect(at_ending_delete,sender=User)




@receiver( pre_init,sender=User)
def at_beginning_init(sender,*arg,**kwargs):
    print("-----------------------------------------------------")
    print("Pre init signal ...")
    print("Sender: ",sender )
    print("Arg: ",arg)
    print(f"Kwargs: {kwargs}")
#pre_init.connect(at_beginning_init,sender=User)

@receiver( post_init,sender=User)
def at_ending_init(sender,*arg,**kwargs):
    print("-----------------------------------------------------")
    print("Post init signal ...")
    print("Sender: ",sender )
    print("Arg: ",arg)
    print(f"Kwargs: {kwargs}")
#post_init.connect(at_ending_init,sender=User)



@receiver(request_started)
def at_beginning_request(sender,environ,**kwargs):
    print("-----------------------------------------------------")
    print("at begining request ...")
    print("Sender: ",sender )
    print("environ: ",environ)
    print(f"Kwargs: {kwargs}")
    print("-----------------------------------------------------")
#request_started.connect(at_beginning_request,sender=User)

@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print("-----------------------------------------------------")
    print("At ending request ...")
    print("Sender: ",sender)
    print(f"Kwargs: {kwargs}")
    print("-----------------------at_ending_request------------------------------")
#request_finished.connect(at_ending_request,sender=User)

@receiver(got_request_exception)
def at_req_exception(sender,request,**kwargs):
    print("-----------------------------------------------------")
    print("At exception request ...")
    print("Sender: ",sender )
    print("request: ",request)
    print(f"Kwargs: {kwargs}")
#got_request_exception.connect(at_req_exception,sender=User)



@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("-----------------------------------------------------")
    print("Before Install Apps ...")
    print("Sender: ",sender )
    print("app_config: ",app_config)
    print("verbosity: ",verbosity)
    print("interactive: ",interactive)
    print("using: ",using)
    print("plan: ",plan)
    print("apps: ",apps)
    print(f"Kwargs: {kwargs}")
#pre_migrate.connect(before_install_app)


@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("-----------------------------------------------------")
    print("at_end_migrate_flush ...")
    print("Sender: ",sender )
    print("app_config: ",app_config)
    print("verbosity: ",verbosity)
    print("interactive: ",interactive)
    print("using: ",using)
    print("plan: ",plan)
    print("apps: ",apps)
    print(f"Kwargs: {kwargs}")
#post_migrate.connect(at_end_migrate_flush)


@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
    print("-----------------------------------------------------")
    print("Logged-in Signal... Run Intro..")
    print("Sender: ",sender )
    print("connection: ",connection)
    print(f"Kwargs: {kwargs}")
#connection_created.connect(conn_db)