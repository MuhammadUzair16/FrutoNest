from django.contrib import admin

from about.models import TeamMember

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')


admin.site.register(TeamMember, TeamMemberAdmin)