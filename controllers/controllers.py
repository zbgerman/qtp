# -*- coding: utf-8 -*-
from odoo import http

# class Qtp(http.Controller):
#     @http.route('/qtp/qtp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qtp/qtp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qtp.listing', {
#             'root': '/qtp/qtp',
#             'objects': http.request.env['qtp.qtp'].search([]),
#         })

#     @http.route('/qtp/qtp/objects/<model("qtp.qtp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qtp.object', {
#             'object': obj
#         })