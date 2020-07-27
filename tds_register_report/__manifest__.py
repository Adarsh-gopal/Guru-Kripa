{
    'name': "Tds Register Report",
    'version': '13.31',
    'author': 'Prixgen Tech Solutions Pvt Ltd.',
    'company': 'Prixgen Tech Solutions Pvt Ltd.',
    'website': 'https://www.prixgen.com',
    'installable': True,
    'application': True,
    'depends': ['base','stock','product','account'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/tds_report_history.xml'
        ], 
}


