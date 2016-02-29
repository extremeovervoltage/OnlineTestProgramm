from __future__ import unicode_literals

from django.db import models


class Aufgabe(models.Model):
	frage_text = models.CharField(max_length=600)
	gegebene_antwort_text = models.CharField(max_length=600,default="")
	# Wie lange der Schueler fuer die Aufgabe zeit hatt
	# angegeben in sekunden, -1 bedeutet unendlich Zeit
	bearbeitungszeit = models.IntegerField(default=-1)

	def __str__(self):
		return 'Aufgabe'+self.frage_text


class Simpleaufgabe(Aufgabe):
	"""Eine Simple Aufgabe ist eine Aufgabe die nur eine richtige
	Loesung hatt und von der Website ausgewertet werden kann"""
	richtige_loesung = models.CharField(max_length=20)
	# Um wieviel Prozent die gegebne loesung von der richtigen abweichen kann
	# um trotzdem als richtig angezeigt zu werden
	abweichungsprozent = models.IntegerField(default=0)
	
	def __str__(self):
		return 'Simpleaufgabe:'+self.frage_text