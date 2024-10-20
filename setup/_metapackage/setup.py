import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-oca-stock-logistics-warehouse",
    description="Meta package for oca-stock-logistics-warehouse Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-account_move_line_product',
        'odoo8-addon-account_move_line_stock_info',
        'odoo8-addon-business_product_location',
        'odoo8-addon-partner_location_auto_create',
        'odoo8-addon-stock_account_change_product_valuation',
        'odoo8-addon-stock_account_quant_merge',
        'odoo8-addon-stock_available',
        'odoo8-addon-stock_available_immediately',
        'odoo8-addon-stock_available_lot_locked',
        'odoo8-addon-stock_available_mrp',
        'odoo8-addon-stock_available_sale',
        'odoo8-addon-stock_available_unreserved',
        'odoo8-addon-stock_change_qty_reason',
        'odoo8-addon-stock_cycle_count',
        'odoo8-addon-stock_inventory_chatter',
        'odoo8-addon-stock_inventory_discrepancy',
        'odoo8-addon-stock_inventory_exclude_sublocation',
        'odoo8-addon-stock_inventory_exhaustive',
        'odoo8-addon-stock_inventory_hierarchical',
        'odoo8-addon-stock_inventory_hierarchical_exhaustive',
        'odoo8-addon-stock_inventory_line_price',
        'odoo8-addon-stock_inventory_lockdown',
        'odoo8-addon-stock_inventory_preparation_filter',
        'odoo8-addon-stock_inventory_revaluation',
        'odoo8-addon-stock_location_area_data',
        'odoo8-addon-stock_location_area_management',
        'odoo8-addon-stock_location_ownership',
        'odoo8-addon-stock_lot_quantity',
        'odoo8-addon-stock_mts_mto_rule',
        'odoo8-addon-stock_operation_type_location',
        'odoo8-addon-stock_orderpoint_generator',
        'odoo8-addon-stock_orderpoint_manual_procurement',
        'odoo8-addon-stock_orderpoint_uom',
        'odoo8-addon-stock_product_location_sorted_by_qty',
        'odoo8-addon-stock_putaway_product',
        'odoo8-addon-stock_quant_manual_assign',
        'odoo8-addon-stock_quant_merge',
        'odoo8-addon-stock_quant_partner_info',
        'odoo8-addon-stock_reserve',
        'odoo8-addon-stock_reserve_sale',
        'odoo8-addon-stock_traceability_operation',
        'odoo8-addon-stock_valuation_account_manual_adjustment',
        'odoo8-addon-stock_warehouse_orderpoint_stock_info',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 8.0',
    ]
)
