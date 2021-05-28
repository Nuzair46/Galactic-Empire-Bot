import googletrans
from googletrans import Translator

class language():
	def translateto(text, lang):
		translator = Translator()
		final = translator.translate(text, dest = lang)
		language = googletrans.LANGUAGES
		return final.text,language[final.src]
