# -*- coding: utf-8 -*-
from odoo import http

# class InternetDirigido(http.Controller):
#     @http.route('/internet_dirigido/internet_dirigido/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/internet_dirigido/internet_dirigido/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('internet_dirigido.listing', {
#             'root': '/internet_dirigido/internet_dirigido',
#             'objects': http.request.env['internet_dirigido.internet_dirigido'].search([]),
#         })

#     @http.route('/internet_dirigido/internet_dirigido/objects/<model("internet_dirigido.internet_dirigido"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('internet_dirigido.object', {
#             'object': obj
#         })