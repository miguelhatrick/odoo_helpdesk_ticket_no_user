import logging
import werkzeug
import odoo.http as http
import base64
from openerp.http import request
_logger = logging.getLogger(__name__)


class HelpdeskOpenTicketController(http.Controller):

    @http.route('/open_ticket/new', type="http", auth="public", website=True)
    def create_new_ticket(self, **kw):
        categories = http.request.env['helpdesk.ticket.category']. \
            search([('active', '=', True), ('name', 'like', '%web%')])
        email = ''
        name = ''
        return http.request.render('odoo_helpdesk_ticket_no_user.portal_create_open_ticket', {
            'categories': categories, 'email': email, 'name': name})

    @http.route('/open_ticket/submitted',
                type="http", auth="public", website=True, csrf=True)
    def submit_ticket(self, **kw):
        vals = {
            'partner_name': kw.get('name'),
            'company_id': None,
            'category_id': kw.get('category'),
            'partner_email': kw.get('email'),
            'description': kw.get('description'),
            'name': kw.get('subject'),
            'attachment_ids': False,
            'channel_id':
                request.env['helpdesk.ticket.channel'].
                sudo().search([('name', '=', 'Web')]).id,
            'partner_id': None,
        }
        new_ticket = request.env['helpdesk.ticket'].sudo().create(
            vals)
        # new_ticket.message_subscribe(partner_ids=request.env.user.partner_id.ids)

        if kw.get('attachment'):
            for c_file in request.httprequest.files.getlist('attachment'):
                data = c_file.read()
                if c_file.filename:
                    request.env['ir.attachment'].sudo().create({
                        'name': c_file.filename,
                        'datas': base64.b64encode(data),
                        'datas_fname': c_file.filename,
                        'res_model': 'helpdesk.ticket',
                        'res_id': new_ticket.id
                    })

        return http.request.render('odoo_helpdesk_ticket_no_user.thank_you', {
            'name': kw.get('name')})

