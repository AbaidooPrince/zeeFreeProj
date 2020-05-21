from django.contrib import admin
from .models import UserProfile,Job,SkillCategory,Certificate,FreelancerSkill,FreelancerPayment,ClientPayment,Attachment,LoggingInfo,JobProposal,JobSkill,Skill

# Register your models here.
admin.site.register(UserProfile),
admin.site.register(Job),
admin.site.register(SkillCategory),
admin.site.register(Certificate),
admin.site.register(FreelancerSkill),
admin.site.register(FreelancerPayment),
admin.site.register(ClientPayment),
admin.site.register(Attachment)
admin.site.register(LoggingInfo)
admin.site.register(JobProposal)
admin.site.register(JobSkill)
admin.site.register(Skill)
