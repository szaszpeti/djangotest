from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer



def customer_profile(sender, instance, created, **kwargs):
	if created:
		#after registration the user will be added to the customer group 
		#and will get a customer profile
		group = Group.objects.get(name='customer')
		instance.groups.add(group)
		print('DONE TILL GROUPING')
		Customer.objects.create(
			user = instance,
			name = instance.username,
			)

		print('Customer created')
	else:
		print('NO SIGNALS BEEING ACTIVATED')
		print(sender, instance, created)

post_save.connect(customer_profile, sender=User)

