from django.db import models

class QuizResponse(models.Model):

    selected_button1 = models.fields.CharField(max_length=100)
    selected_button2 = models.fields.CharField(max_length=100)
    selected_button3 = models.fields.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
        #to save the data
    def register(self):
        self.save()

    