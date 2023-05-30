from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver


from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user ,**kwargs):
    print("--------------------")
    print("User login successfully")
    print(f" sender: {sender} \n request: {request} \n user: {user} \n kwargs: {kwargs}\n")

#user_logged_in.connect(login_success,sender=User)  


@receiver(user_logged_out,sender=User)
def loggout(sender,request,user,**kwargs):
    print("----------------------------------------------")
    print("User logout successfully")
    print(f" sender: {sender} \n request: {request} \n user: {user} \n kwargs: {kwargs}\n")


@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("----------------------------------------------")
    print("User login faild ")
    print(f" sender: {sender} \n credentials: {credentials} \n request: {request} \n kwargs: {kwargs}\n")



@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("-----------------------------")
    print(" Pre Save Signal...")
    print(f" sender: {sender} \n Instance: {instance} \n kwargs: {kwargs}\n")



@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    print("-----------------------------")
    if created:
        print(" post Save created Signal...")
        print(f" sender: {sender} \n Instance: {instance} \n created:{created} \n kwargs: {kwargs}\n")
    else:
        print(" post Save updated Signal...")
        print(f" sender: {sender} \n Instance: {instance} \n created:{created} \n kwargs: {kwargs}\n")



