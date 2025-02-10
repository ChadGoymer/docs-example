from datetime import datetime

import pytest


def pytest_html_report_title(report):
    report.title = "Testing Calculations"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(['<a href="coverage/index.html">Coverage Report</a>'])


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    cells.insert(
        1, f'<td class="col-time">{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</td>'
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
