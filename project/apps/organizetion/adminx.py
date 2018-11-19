__author__ = 'sakura'
__date__ = '2018-11-19 17:19'
from .models import CourseOrg,CityDict,Teacher
import xadmin
class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time',]

class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'add_time','click_nums','fav_nums','image','address','city']
    search_fields =  ['name', 'desc','click_nums','fav_nums','image','address','city']
    list_filter =  ['name', 'desc', 'add_time','click_nums','fav_nums','image','address','city']

class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums','add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums','add_time']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)