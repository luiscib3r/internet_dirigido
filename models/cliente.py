# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cliente(models.Model):
    _name = 'internet_dirigido.cliente'

    name = fields.Char(unique=True, required=True, string="Nombre")

    ip = fields.Char(string="IP")

    company_currency = fields.Many2one('res.currency')

    debe = fields.Monetary(string="Debe", currency_field='company_currency', compute='_compute_debe')

    @api.one
    def _compute_debe(self):
        conexiones = self.env['internet_dirigido.conexion'].search([('cliente', '=', self.id), ('estado', '=', 1)])

        self.debe = self._sum_money(conexiones)

    def _sum_money(self, records):
        sum = 0.0

        for r in records:
            sum = sum + r.precio

        return sum