# -*- coding: utf-8 -*-
# from odoo import http


# class Planes(http.Controller):
#     @http.route('/planes/planes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/planes/planes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('planes.listing', {
#             'root': '/planes/planes',
#             'objects': http.request.env['planes.planes'].search([]),
#         })

#     @http.route('/planes/planes/objects/<model("planes.planes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('planes.object', {
#             'object': obj
#         })
