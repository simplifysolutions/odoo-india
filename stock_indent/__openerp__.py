# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Indent Management',
    'version' : '1.0',
    'author' : 'OpenERP SA',
    'sequence': 120,
    'category': 'Warehouse Management',
    'website' : 'http://www.openerp.com',
    'summary' : 'Manage and track internal material requests',
    'description' : """
Indent Management
===================
Usually big companies set-up and maintain internal requisition to be raised by Engineer, Plant Managers or Authorised Employees. Using Indent Management you can control the purchase and issue of material to employees within company warehouse.

- Purchase Indents
- Store purchase
- Capital Purchase
- Repairing Indents
- Project Costing
- Valuation
- etc.

Purchase Indents
++++++++++++++++++
When there is a need of specific materials or services, authorized employees or managers will create a Purchase Indent. He can specify required date, whether the indent is for store or capital, the urgency of materials etc. on indent.

While selecting the product, the system will automatically set the procure method based on the quantity on hand for the product. Once the indent is approved, an internal move has been generated. A purchase order will also be generated if the products are not in stock and to be purchased.


Repairing Indents
++++++++++++++++++
A store manager or will create a repairing indent when the product is needed to be sent for repairing. In case of repairing indent you will be able to select product to be repaired and service for repairing of the product.

A purchase order is generated for the service taken for the supplier who repairs the product, and an internal move has been created for the product to be moved for repairing.
""",
    'depends' : ['stock', 'purchase', 'product_container'],
    'data' : [
        'stock_indent_view.xml',
        'stock_indent_workflow.xml',
        'stock_workflow_change.xml',
        'stock_indent_data.xml',
        'stock_indent_sequence.xml',
        'stock_indent_report.xml',
        'report/stock_indent_analysis_report_view.xml'
    ],
    'demo': [
        'stock_indent_demo.xml'
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
