# -*- coding: utf-8 -*-
from odoo import http

# class Telegram(http.Controller):
#     @http.route('/telegram/telegram/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/telegram/telegram/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('telegram.listing', {
#             'root': '/telegram/telegram',
#             'objects': http.request.env['telegram.telegram'].search([]),
#         })

#     @http.route('/telegram/telegram/objects/<model("telegram.telegram"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('telegram.object', {
#             'object': obj
#         })