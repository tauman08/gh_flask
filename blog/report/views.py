from flask import Blueprint, render_template, redirect

report = Blueprint('report', __name__, url_prefix='/reports', static_folder='../static')

REPORTS = {
    1: 'Base report',
    2: 'Report for marketplace',
    3:  'Report for CRM',
}

@report.route('/')
def report_list():
    return render_template(
        'reports/list.html',
        reports=REPORTS,
    )

@report.route('/<int:pk>')
def get_report(pk: int):
    try:
        report_name = REPORTS[pk]
    except KeyError:
        # raise NotFound(f'Report id {pk} not found')
        return redirect(
            '/reports/'
        )

    return  render_template(
        'reports/details.html',
        report_name = report_name,
    )