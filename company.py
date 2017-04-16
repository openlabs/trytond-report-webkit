# -*- coding: utf-8 -*-
"""
    company.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import PoolMeta
from trytond.model import fields
from jinja2 import Environment
from openlabs_report_webkit.__init__ import ReportWebkit

__metaclass__ = PoolMeta
__all__ = ['Company']


class Company:
    __name__ = 'company.company'

    header_html = fields.Text('Header Html')
    footer_html = fields.Text('Footer Html')

    def get_html_header(self):

        env = Environment()
        env.filters.update(ReportWebkit.get_jinja_filters())
        html_template = env.from_string(
            self.header_html
        )
        return html_template

    def get_html_footer(self):

        env = Environment()
        env.filters.update(ReportWebkit.get_jinja_filters())
        html_template = env.from_string(
            self.footer_html
        )
        return html_template
