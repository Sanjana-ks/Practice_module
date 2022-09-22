# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Student(models.Model):
    _name = "student"
    _description = "Student Data"

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')], string='Gender')
    dob = fields.Date(string='DOB', required=True)
    mobile = fields.Char(string='Contact no.', required=True)
    degree = fields.Selection([
        ('ug', 'Bachelors'),
        ('pg', 'Masters')], string='Degree', required=True)
    department_id = fields.Many2one('department', string='Department')
    admission = fields.Datetime(string="Admission Date/Time")
    is_graduated = fields.Boolean(string='Is graduated?')
    document = fields.Binary(string='Upload Document')
    currency_id = fields.Many2one('res.currency', string="Currency")
    fees = fields.Monetary(string='Fees')
    description = fields.Html(string='Description')
    student_marks = fields.One2many('marks', 'student_id', string='Student Marks')
    student_subject = fields.Many2many('subject', 'student_subject_rel', 'student_id', 'subject_id', string='Subjects')
