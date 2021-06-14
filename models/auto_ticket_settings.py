 # Copyright (C)
# Copyright 2021- Miguel Hatrick(<http://www.dacosys.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class AutoTicketSettings(models.TransientModel):
    """Helpdesk Ticket Category addon."""
    _inherit = "res.config.settings"

    captcha_site_key = fields.Char(string='Site key', default='SITE KEY')
    captcha_secret_key = fields.Char(string='Secret key', default='SECRET KEY')

    def get_values(self):
        res = super(AutoTicketSettings, self).get_values()
        res.update(captcha_site_key=self.env['ir.config_parameter'].sudo().get_param('helpdesk.captcha_site_key'))
        res.update(captcha_secret_key=self.env['ir.config_parameter'].sudo().get_param('helpdesk.captcha_secret_key'))

        return res

    def set_values(self):
        super(AutoTicketSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('helpdesk.captcha_site_key', self.captcha_site_key)
        self.env['ir.config_parameter'].sudo().set_param('helpdesk.captcha_secret_key', self.captcha_secret_key)
