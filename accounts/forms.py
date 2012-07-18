from django import forms
from iStore.accounts.models import UserProfile
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user',)