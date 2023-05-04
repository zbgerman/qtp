# -*- coding: utf-8 -*-

from odoo import models, fields, api

class qtp(models.Model):
    _name = 'qtp.type_task'
    _description = "Type Task"

    name = fields.Char(required=True)
    # type_tasks_ids = fields.One2many(
    #     'qtp.tasks', 'type_task_id', string='Type Task')

class qtp(models.Model):
    _name = 'qtp.tasks'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Tasks"
#     _rec_name = "room_id"


    title = fields.Char(required=True, tracking=True)
    description = fields.Char(tracking=True, compute='_compute_description')
    type_task_id = fields.Many2one('qtp.type_task', string='Type Task', required=True, tracking=True)
    status = fields.Selection([('abierto', 'Abierto'),
                               ('realizado', 'Realizado'),
                               ('verificado', 'Verificado'),
                               ('cerrado', 'Cerrado'),
                               ('activo', 'Activo')], string='Estado', default='abierto', required=True, tracking=True)
    priority = fields.Selection([('Alta', 'Alta'),
                                 ('Media', 'Media'),
                                 ('Baja', 'Baja')], string='Priority', default='Alta', required=True, tracking=True)
    task_user_id = fields.Many2one(
        'res.users', string='User', required=True, tracking=True, default=lambda self: self.env.user)
    assigned_id = fields.Many2many(
        'res.users', string='assigned', required=True, tracking=True)
    start_date = fields.Date(default=fields.Date.today(), tracking=True)
    end_date = fields.Date(default=fields.Date.today(), tracking=True)
    start_time = fields.Datetime(default=fields.Datetime.now(), tracking=True)
    end_time = fields.Datetime(default=fields.Datetime.now(), tracking=True)
    price = fields.Float(digits=(15, 2), help="Entre el valor total", tracking=True)
    details_ids = fields.One2many(
        'qtp.details_tasks', 'task_id', string='Task', tracking=True)

    @api.depends('title', 'price')
    def _compute_description(self):
          self.description = self.title 



class qtp(models.Model):
    _name = 'qtp.details_tasks'
    _description = "Details Tasks"
    
    task_id = fields.Integer(required=True) 
    details = fields.Char(required=True)
