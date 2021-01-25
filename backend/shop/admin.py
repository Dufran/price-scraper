from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from django.contrib.auth.models import Group
from simple_history.admin import SimpleHistoryAdmin





# from .models import Branch, Channel, Admin, AdminGroup, Status

# # # Register your models here.


# # class AlertGroupAdmin(ImportExportMixin, SimpleHistoryAdmin):
# #     list_display = ["email",  "branch"]


# class BranchAdmin(ImportExportMixin, SimpleHistoryAdmin):
#     list_display = (
#         "name",
#         "description",
#     )


# class StatusAdmin(ImportExportMixin, SimpleHistoryAdmin):
#     list_display = (
#         "name",
#         "description",
#     )


# class AdminGroupAdmin(ImportExportMixin, SimpleHistoryAdmin):
#     list_display = ("name",)


# class ChannelAdmin(ImportExportMixin, SimpleHistoryAdmin):
#     list_display = (
#         "name",
#         "url",
#     )


# class AdminAdmin(ImportExportMixin, SimpleHistoryAdmin):
#     list_display = (
#         "name",
#         "description",
#     )


# # # region registering models to admin site
# admin.site.register(Branch, BranchAdmin)
# admin.site.register(AdminGroup, AdminGroupAdmin)
# admin.site.register(Status, StatusAdmin)
# admin.site.register(Admin, AdminAdmin)
# admin.site.register(Channel, ChannelAdmin)
