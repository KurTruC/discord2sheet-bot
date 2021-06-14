# BSD 3-Clause License
# Copyright (c) 2019, Hugonun(https://github.com/hugonun)
# All rights reserved.

import discord
from gsheet import *




client = discord.Client()
sheet = gsheet()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Restrict the command to a role
    # Change REQUIREDROLE to a role id or None
    REQUIREDROLE = None
    if REQUIREDROLE is not None and discord.utils.get(message.author.roles, id=str(REQUIREDROLE)) is None:
        await message.channel.send('You don\'t have the required role!')
        return

    # Command to insert data to excel
    if message.content.startswith('!ev'):
        SPREADSHEET_ID = '1sKOLoQ054RbXuG5IW_ZSBc4wI6OZ0zp9_x-WieIeAfY' # Add ID here
        RANGE_NAME = 'A2'
        FIELDS = 4 # Amount of fields/cells

        # Code
        msg = message.content[3:]
        result = [x.strip() for x in msg.split(';')] ##+ ['=Q13'] + ['=R13']
        if len(result) == FIELDS:
            # Add
            print(message.created_at.strftime("%d.%m.%Y %H:%M"))
            DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at.strftime("%d.%m.%Y %H:%M"))] + [''] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            #await message.channel.send('Vos données ont été enregistrées', delete_after=5)
            embedVar = discord.Embed(title="Evolution", description="Vos donnees", color=0x00ffff)
            embedVar.set_author(name="Las Zetas Val", url='https://docs.google.com/spreadsheets/d/1tJC5mw110MwVmHeSsyHhP7kBcaU0Gmw2TZAw-x7Ge50/edit#gid=0')
            embedVar.add_field(name="Pseudo:", value=f"**{DATA[4]}**", inline=False)
            embedVar.add_field(name="Puissance:", value=f"**{DATA[5]}**", inline=True)
            embedVar.add_field(name="Level:", value=f"**{DATA[6]}**", inline=True)
            embedVar.add_field(name="Contribution", value=f"**{DATA[7]}**", inline=True)
            await message.channel.send(embed=embedVar, delete_after=30)
            await message.delete()
            #await message.channel.send(f"Pseudo:**{DATA[4]}**\nPuissance:**{DATA[5]}**\nLevel:**{DATA[6]}**\nContribution:**{DATA[7]}**\n\nVos données ont été enregistrées\nAuto destruction du message dans 15s", delete_after=15)
            #await message.channel.send(f"vous avez {DATA[3]}/s et vous voulez obtenir {DATA[4]}/s\nVous devez attendre ... ou ... (Temps hors ligne)\n**se message va s\'auto detruire dans 10 secondes**", delete_after=10) ## Voir le resultat

        else:
            # Needs more/less fields
            await message.channel.send('Erreur : Vous devez ajouter {0} champs, ce qui signifie qu\'il ne peut y avoir que {1} point virgule.'.format(FIELDS,FIELDS-1))

    if message.content.startswith('!ba') or message.content.startswith('!BA'):
        SPREADSHEET_ID = '1sKOLoQ054RbXuG5IW_ZSBc4wI6OZ0zp9_x-WieIeAfY' # Add ID here
        RANGE_NAME = 'K2'
        SAMPLE_RANGE = 'R1:S1'
        FIELDS = 2 # Amount of fields/cells

        # Code
        msg = message.content[3:]
        result = [x.strip() for x in msg.split(';')] #+ ['=R1'] #+ ['=S1']
        result2 = []
        if len(result) == FIELDS:
            # Add
            print(message.created_at.strftime("%d.%m.%Y %H:%M"))
            DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at.strftime("%d.%m.%Y %H:%M"))] + [''] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            #sheet.read(SPREADSHEET_ID, SAMPLE_RANGE,DATA)
            #await message.channel.send('Vos données ont été enregistrées', delete_after=5)
            await message.delete()
            await message.channel.send(f"Votre Argent:**{DATA[4]}/s** -- Votre Besoin:**{DATA[5]}/s**\n\nVos données ont été enregistrées\nAuto destruction du message dans 15s", delete_after=15)
            #await message.channel.send(f"vous avez {DATA[3]}/s et vous voulez obtenir {DATA[4]}/s\nVous devez attendre ... ou ... (Temps hors ligne)\n**se message va s\'auto detruire dans 10 secondes**", delete_after=10) ## Voir le resultat
            print()
        else:
            # Needs more/less fields
            await message.channel.send('Erreur : Vous devez ajouter {0} champs, ce qui signifie qu\'il ne peut y avoir que {1} point virgule.'.format(FIELDS,FIELDS-1))

    if message.content.startswith('!Lire') or message.content.startswith('!lire'):
        SPREADSHEET_ID = '1sKOLoQ054RbXuG5IW_ZSBc4wI6OZ0zp9_x-WieIeAfY' # Add ID here

        SAMPLE_RANGE = 'R1:S1'
        FIELDS = 0 # Amount of fields/cells
        value = []
        # Code
        msg = message.content[4:]

        result2 = []
        if len(result2) == FIELDS:
            # Add
            print(message.created_at.strftime("%d.%m.%Y %H:%M"))
            DATA = value
            sheet.read(SPREADSHEET_ID, SAMPLE_RANGE,DATA)
            #await message.channel.send('Vos données ont été enregistrées', delete_after=5)
            await message.delete()
            #await message.channel.send(f"Votre Argent:**{DATA[0]}/s** -- Votre Besoin:**{DATA[1]}/s**\n\nVos données ont été enregistrées\nAuto destruction du message dans 15s", delete_after=15)
            #await message.channel.send(f"vous avez {DATA[3]}/s et vous voulez obtenir {DATA[4]}/s\nVous devez attendre ... ou ... (Temps hors ligne)\n**se message va s\'auto detruire dans 10 secondes**", delete_after=10) ## Voir le resultat
            print(DATA)
        else:
            # Needs more/less fields
            await message.channel.send('Erreur : Vous devez ajouter {0} champs, ce qui signifie qu\'il ne peut y avoir que {1} point virgule.'.format(FIELDS,FIELDS-1))
    # Whois
    # Please dont remove the copyright and github repo
    elif len(message.mentions) > 0:
        for muser in message.mentions:
            if muser.id == client.user.id:
                if any(word in message.content for word in ['whois','who is','Help','help','info']):
                    await message.channel.send('This bot was made by hugonun(https://github.com/hugonun/).\nSource code: https://github.com/hugonun/discord2sheet-bot')


client.run('Token') # Add bot token here
