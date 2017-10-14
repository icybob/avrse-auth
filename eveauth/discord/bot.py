import os, sys
import django
sys.path.append("../")
os.environ['DJANGO_SETTINGS_MODULE'] = 'avrseauth.settings'
django.setup()

from django.db.models import Q
from disco.bot import Plugin
from social_django.models import UserSocialAuth


class AuthPlugin(Plugin):
    @Plugin.command('ping')
    def command_ping(self, event):
        social = self._get_social(event.msg.author.id)
        if social:
            event.msg.reply("Hi %s" % social.user.username)
        else:
            event.msg.reply("Hi %s" % event.msg.author.id)


    @Plugin.listen('GuildMemberAdd')
    def guild_member_join(self, event):
        # Kick the user if they aren't authed
        social = self._get_social(event.member.id)
        if not social:
            event.member.kick()

        # Set their nickname to their EVE Character
        event.member.set_nickname(social.user.profile.character.name)

        # Set corp role
        event.member.add_role(self._get_role(event.guild, social.user.profile.corporation.ticker))

        # Set regular group roles
        groups = social.user.groups.exclude(
            Q(name__startswith="Corp: ") | Q(name__startswith="Alliance: ")
        ).all()
        for group in groups:
            event.member.add_role(self._get_role(event.guild, group.name))

        # Set Access Level Group
        access_level = ["Non-member", "Blue", "Member"][social.user.profile.level]
        event.member.add_role(self._get_role(event.guild, access_level))


    # Try to get the social object from a discord ID. Return None if not found
    def _get_social(self, uid):
        return UserSocialAuth.objects.filter(uid=uid).first()


    # Get a role object from a string
    def _get_role(self, guild, name):
        # Check if the role already exists
        for role in guild.roles.values():
            if role.name == name:
                return role

        # It doesn't so lets make it
        role = guild.create_role()
        self.client.api.guilds_roles_modify(guild.id, role.id, name=name)
        return role