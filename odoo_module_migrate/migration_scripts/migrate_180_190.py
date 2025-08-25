# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
# This script is based on the original code from:
# https://github.com/odoo/odoo/blob/master/odoo/upgrade_code/17.5-00-tree-to-list.py

from odoo_module_migrate.base_migration_script import BaseMigrationScript


class MigrationScript(BaseMigrationScript):
    _GLOBAL_FUNCTIONS = []
