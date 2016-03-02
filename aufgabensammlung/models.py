from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Aufgabensammlung(models.Model):
	"""Eine Sammlung an Aufgaben Hausaufgabe Test etc."""
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name

	



class Simpleaufgabe(models.Model):
	"""Eine Simple Aufgabe ist eine Aufgabe die nur eine richtige
	Loesung hatt und von der Website ausgewertet werden kann"""
	frage_text = models.CharField('Frage', max_length=600)
	# Wie lange der Schueler fuer die Aufgabe zeit hatt
	# angegeben in sekunden, -1 bedeutet unendlich Zeit
	bearbeitungszeit = models.IntegerField('Bearbeitungszeit (Sekunden)', default=-1)
	# sammlung gibt die Aufgabensammlung an in der sich diese Aufgabe befindet 
	
	sammlung = models.ForeignKey(Aufgabensammlung, on_delete=models.CASCADE, default=1)

	richtige_loesung = models.CharField('Richtige Loesung', max_length=20)
	# Um wieviel Prozent die gegebne loesung von der richtigen abweichen kann
	# um trotzdem als richtig angezeigt zu werden
	abweichungsprozent = models.IntegerField('Maximale prozentuale Abweichung von der gebenen Loesung', default=0)
	
	def __str__(self):
		return 'Simpleaufgabe: '+self.frage_text



class Antwort(models.Model):
	"""Eine von einem Schueler gegebene Antwort
	auf eine Frage"""
	antwort_text = models.CharField('Antworttext', max_length=600, default="")
	aufgabe = models.ForeignKey(Simpleaufgabe, on_delete=models.CASCADE)



class ErweiterterNutzer(models.Model):
	"""Ein Schueler oder Lehrer"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	schule = models.CharField(max_length=60)
	lehrer = models.BooleanField(default=False)

	


