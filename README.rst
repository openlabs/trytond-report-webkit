Webkit based PDF report engine
==============================

.. image:: https://travis-ci.org/openlabs/trytond-report-webkit.png?branch=develop
    :target: https://travis-ci.org/openlabs/trytond-report-webkit

This package allows you to build HTML based reports and then convert them
into PDFs using either `wkhtmltopdf` which uses the webkit rendering engine and
QT. (WebKit is the engine of Apples Safari). or
`Weasyprint<http://http://weasyprint.org/>`_

The templates are written using `Genshi <http://genshi.edgewall.org>`_.
Though Genshi is not our favorite templating engine, it is a package
tryton core depends on, and the authors did not want to add another
template engine as its dependency. Genshi comes with a fairly good
`tutorial <http://genshi.edgewall.org/wiki/Documentation/xml-templates.html>`_.

The package also supports `Jinja's <http://jinja.pocoo.org/>`_ Template
`Inheritance <http://jinja.pocoo.org/docs/templates/#template-inheritance>`_.

Using this in your projects
===========================

Instead of using the default report class from trytond.report use the
ReportWebkit class from this package instead.

::

    from openlabs_report_webkit import ReportWebkit

    class UserReport(ReportWebkit):
        __name__ = 'res.user'

        @classmethod
        def get_jinja_filters(cls, *args, **kwargs):
            """
            Add my custom filters
            """
            filters = super(UserReport, cls).get_jinja_filters(*args, **kwargs)
            filters.update({
                'nl2br': lambda value: value.replace('\n','<br>\n')
            })
            return filters


Output Formats
--------------

To get PDF outputs (instead of standard html) ensure that the report
definition in xml clearly shows the extension as PDF. This could be
changed from the tryton administration section too.

Template Filters
----------------

Tryton HTML reports arrive with some Template filters to make things easier:

- dateformat: Format a date field using Babel
- datetimeformat
- currencyformat (use with currency.code)
- modulepath: Get the absolute Path of a file within a module (e.g.: reports/bg.svg) prefixed with file:///

Of course you can add your own as stated above.

Including Styles
----------------

To include stylesheets, images or any other static data you have two options:

1. Have Tryton serving your files by adding the static-directory to your Tryton json_path
2. Bundle your static files inside the reports module and reference using

::

    <link rel="stylesheet" href="{{ 'reports/main.css' | module_path }}" type="text/css">

The second approach comes with the downside that static files will only be
available on the server, so you can only see the formatted pdf

Adding as a dependency
----------------------

You can add the report toolkit as a dependent package of your tryton
module by adding into the install_requires list on your setup.py script.
Remember to specify the version numbers carefully, or the latest version
of the package available would be installed.

For example if your module is for version 2.6 of tryton, the line to add
would be

::

    install_requires = [
        ...,
        'openlabs_report_webkit>=2.6,<2.7'
        ...,
    ]

Gotchas!
========

The report file is missing
--------------------------

* Did you add the template file to the package_data in your setup.py ?
* Did you add the template file extension to the included files in
  MANIFEST ?

PDF generation problems
-----------------------

* Check if wkhtmltopdf works well:  Installing it simply via 
  `sudo apt-get install wkhtmltopdf` on Ubuntu for exmaple will install a
  reduced functionality version which is probably not what you want.
