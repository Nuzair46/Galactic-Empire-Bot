import pymongo
from pymongo import MongoClient

cluster = MongoClient("INSERT MONGO CONNECTION HERE")

db = cluster["Discord"]

class PrefixBase():
	

	def finding(guild_id):
		collection = db["prefix"]
		result = collection.find_one({str(guild_id) : { "$exists": "true" }})
		return result[str(guild_id)]

	def adding(guild_id):
		collection = db["prefix"]
		collection.insert_one({str(guild_id):"r!"})

	def remove(guild_id):
		collection = db["prefix"]
		collection.delete_one({str(guild_id) : { "$exists": "true" }})

	def new(guild_id,prefix):
		collection = db["prefix"]
		OldGuild = {str(guild_id) : { "$exists": "true" }}
		NewGuild = {str(guild_id) : prefix}
		NewValue = {"$set": NewGuild} 

		if collection.find_one({str(guild_id) : { "$exists": "true" }}):
			collection.update_one(OldGuild, NewValue)
		
		else :
			collection.insert_one(NewGuild)

class PublishChannel():

	def new(guild_id,publish):
		collection = db["publish"]
		OldGuild = {str(guild_id) : { "$exists": "true" }}
		NewGuild = {str(guild_id) : publish}
		NewValue = {"$push": NewGuild} 

		if collection.find_one(OldGuild):
			collection.update_one(OldGuild, NewValue)
		
		else :
			NewGuildArray = {str(guild_id) : [publish]}
			collection.insert_one(NewGuildArray)

	def remove(guild_id,publish):
		collection = db["publish"]
		OldGuild = {str(guild_id) : { "$exists": "true" }}
		NewGuild = {str(guild_id) : publish}
		NewValue = {"$pull": NewGuild}
		if collection.find_one(NewGuild):
			collection.update(OldGuild, NewValue)
			return 1
		else: 
			return 0

	def finding(guild_id,publish):
		collection = db["publish"]
		NewGuild = {str(guild_id) : str(publish)}
		if collection.find_one(NewGuild):
			return True
		else:
			return False

class InviteDump():

	def new(guild_id,channel):
		collection = db["invites"]
		OldGuild = {str(guild_id) : { "$exists": "true" }}
		NewGuild = {"$set":{str(guild_id) : channel}}
		NewGuildOne = {str(guild_id) : channel}

		if collection.find_one(OldGuild):
			collection.update_one(OldGuild, NewGuild)
			return 1
		
		else :
			collection.insert_one(NewGuildOne)
			return 0

	def remove(guild_id,channel):
		collection = db["invites"]
		NewGuild = {str(guild_id) : channel}
		if collection.find_one(NewGuild):
			collection.delete_one(NewGuild)
			return 1
		else: 
			return 0

	def finding(guild_id):
		collection = db["invites"]
		NewGuild = {str(guild_id) : { "$exists": "true" }}
		result = collection.find_one(NewGuild)
		if result:
			return result[str(guild_id)], True
		else:
			return None, False

class StarboardChannel():

	def new(guild_id,channel):
		collection = db["starboard"]
		OldGuild = {str(guild_id) : { "$exists": "true" }}
		NewGuild = {"$set":{str(guild_id) : channel}}
		NewGuildOne = {str(guild_id) : channel}

		if collection.find_one(OldGuild):
			collection.update_one(OldGuild, NewGuild)
			return 1
		
		else :
			collection.insert_one(NewGuildOne)
			return 0

	def remove(guild_id,channel):
		collection = db["starboard"]
		NewGuild = {str(guild_id) : channel}
		if collection.find_one(NewGuild):
			collection.delete_one(NewGuild)
			return 1
		else: 
			return 0

	def finding(guild_id):
		collection = db["starboard"]
		NewGuild = {str(guild_id) : { "$exists": "true" }}
		result = collection.find_one(NewGuild)
		if result:
			return result[str(guild_id)], True
		else:
			return None, False