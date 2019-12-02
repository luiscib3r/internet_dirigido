# -*- coding: utf-8 -*-

from odoo import models, fields, api

utime_r = ['', 'Minutos', 'Horas']

class oferta(models.Model):
    _name = 'internet_dirigido.oferta'

    name = fields.Char(compute='_compute_name', string="Oferta")

    company_currency = fields.Many2one('res.currency')

    precio = fields.Monetary(string="Precio a cobrar", required=True, currency_field='company_currency')

    tiempo = fields.Char(string="Tiempo", compute='_compute_time')

    time = fields.Integer(string="Tiempo", required=True)
    
    utime = fields.Selection(selection=[(1, 'Minutos'), (2, 'Horas')], required=True, string="Unidad")

    @api.one
    def _compute_name(self):
        self.name = self.tiempo + ' - ' + str(self.precio)
    
    @api.one
    def _compute_time(self):
        self.tiempo = str(self.time) + ' ' + utime_r[self.utime]