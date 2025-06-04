from django.contrib import admin
from django.utils.safestring import mark_safe
from cspreports.models import get_report_model

CSPReport = get_report_model()

@admin.register(CSPReport)
class CSPReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'document_uri', 'blocked_uri')
    fields = ('created', 'modified', 'json_as_html')
    readonly_fields = ('created', 'modified', 'json_as_html')

    @admin.display(
        description="Report"
    )
    def json_as_html(self, instance):
        return mark_safe("<br />" + instance.json_as_html())

    def document_uri(self, instance):
        return instance.data.get('csp-report', {}).get('document-uri')

    def blocked_uri(self, instance):
        return instance.data.get('csp-report', {}).get('blocked-uri')


