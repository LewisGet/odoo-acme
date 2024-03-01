from odoo import http
from odoo.http import request
import re
import os

class LazyAcme(http.Controller):
    default_acme_path = "/var/www/public_html/.well-known/acme-challenge"

    @http.route('/.well-known/acme-challenge/<string:file_name>', type='http', auth='public', methods=['GET'])
    def main(self, file_name, **get):
        if not re.match("^[a-zA-Z0-9\\.]+$", file_name):
            return http.not_found()

        file_path = os.path.join(self.default_acme_path, file_name)

        if not os.path.isfile(file_path):
            return http.not_found()

        with open(file_path, "r") as f:
            data = f.read()

        return data

    @http.route('/en/.well-known/acme-challenge/<string:file_name>', type='http', auth='public', methods=['GET'])
    def en(self, file_name, **get):
        return self.main(file_name)
