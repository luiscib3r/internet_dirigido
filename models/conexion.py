# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError

class conexion(models.Model):
    _name = 'internet_dirigido.conexion'

    name = fields.Char(compute='_compute_name')

    cliente = fields.Many2one('internet_dirigido.cliente', string="Cliente")

    ip = fields.Char(string="ip", compute='_compute_ip')

    fecha = fields.Date(string="Fecha", required=True, default=fields.Date.today)

    oferta = fields.Many2one('internet_dirigido.oferta', required=True)

    company_currency = fields.Many2one('res.currency')

    precio = fields.Monetary(string="Precio a cobrar", required=True, currency_field='company_currency', readonly=True, compute='_compute_precio')

    estado = fields.Many2one('internet_dirigido.estado', string="Estado", required=True, ondelete='restrict', track_visibility='onchange', index=True, default=0, group_expand='_read_group_stage_ids')

    is_this_week = fields.Integer(compute='_compute_is_this_week', string="Esta semana")

    @api.one
    def _compute_ip(self):
        self.ip = self.cliente.ip

    @api.one
    def _compute_is_this_week(self):
        this_day = fields.Date.today()
        this_day_n = this_day.weekday()
        lunes = this_day - this_day.resolution * this_day_n
        domingo = this_day + this_day.resolution * (6 - this_day_n)

        if (self.fecha >= lunes and self.fecha <= domingo):
            self.is_this_week = 1
        else:
            self.is_this_week = 0

    @api.model
    def _read_group_stage_ids(self,stages,domain,order):
        stage_ids = self.env['internet_dirigido.estado'].search([])
        return stage_ids

    @api.onchange('oferta')
    def _onchange_oferta(self):
        self.precio = self.oferta.precio

    @api.one
    @api.depends('oferta')
    def _compute_precio(self):
        self.precio = self.oferta.precio

    @api.one
    def _compute_name(self):
        try:
            self.name = self.cliente.name + ' ' + str(self.fecha)
        except Exception:
            self.name = '_' + ' ' + str(self.fecha)
