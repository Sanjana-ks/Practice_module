# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Department(models.Model):
    _name = 'department'
    _description = 'Department Names'

    name = fields.Char(string='Department')
    head = fields.Char(string='Head of Department')
    subjects = fields.One2many('subject', 'department_id', string='Subjects')
    student_id = fields.One2many('student', 'department_id', string='Students')


class Subject(models.Model):
    _name = 'subject'
    _description = 'Subject Names'

    department_id = fields.Many2one('department', string='Department')
    name = fields.Char(string='Subject')
