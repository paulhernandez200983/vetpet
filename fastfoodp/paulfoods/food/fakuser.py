
__author__      = "Mohit Kumar"
__version__     = "Beta"
__maintainer__  = "https://github.com/mohit4"
__email__       = "mohitkumar2801@gmail.com"

# assigning env variables from django project
import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','paulfoods.settings')

# Setting up django configurations
import django
django.setup()

# python libraries for creating fake data
import random
from faker import Faker

# django app models for which data has to be populated
from django.contrib.auth.models import User
from food.forms import CustomUser

# Initializing fake generator
fakegen = Faker(['es_MX'])

def create_entities(N=100):
    '''
    Populate multiple entities here
    '''
    # get lists of all users in django db 
    # NOTE : Make sure at least one user exists, superuser will also work
    all_users = User.objects.all()

    # creating N entries
    for i in range(N):
        # generating fake data
     
     
        
    
        f_email = fakegen.email()
        f_user = random.choice(all_users)
        f_name=fakegen.name()
        f_pas=fakegen.password()
        state=fakegen.state()
        direc=fakegen.address()
        
        # creating data object and saving to DB
        entity = CustomUser(
          
            
            username=f_user,
            email=f_email,
            password1=f_pas,
            first_name=f_name,
            
            direccion=direc,
             estado=state,
        )
        entity.save()
    
    # finished
    print("Finished...{} entries populated.".format(N))

if __name__ == "__main__":
    
    # Verify the number of command line arguments
    print("Initializing... checking syntax...")

    try:
        if len(sys.argv) == 2:
            N = int(sys.argv[1])
            print("Found parameter N = {}".format(N))
            # calling method for data population
            create_entities(N)
        else:
            print("No additional parameter provided, populating default no. of entries.")
            create_entities()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Exception occurred at line : {}! {}".format(exc_tb.tb_lineno, e))
        sys.exit(1)
