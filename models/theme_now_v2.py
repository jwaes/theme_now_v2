from odoo import models


class ThemeNowV2(models.AbstractModel):
    _inherit = 'theme.utils'

    @classmethod
    def _build_model(cls, pool, cr):
        res = super(ThemeNowV2, cls)._build_model(pool, cr)
        if 'theme_now_v2.template_header_now' not in res._header_templates:
            res._header_templates.insert(0, 'theme_now_v2.template_header_now')
        return res    

    def _theme_now_v2_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('theme_now_v2.template_header_now')
        self.enable_view('website.header_language_selector_inline')
        self.enable_view('website.header_language_selector_code')
