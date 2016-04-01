from openerp import fields, models


class Student(models.Model):
    _name = "test_module.student"

    name = fields.Char("Name")
    lastname = fields.Char("Last name")
    group = fields.Many2one('test_module.group', 'Group ID')


class Group(models.Model):
    _name = "test_module.group"
    _rec_name = 'group_id'

    group_id = fields.Char("Group ID")

