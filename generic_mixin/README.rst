Generic Mixins
==============

.. |badge1| image:: https://img.shields.io/badge/pipeline-pass-brightgreen.png
    :target: https://github.com/crnd-inc/generic-addons

.. |badge2| image:: https://img.shields.io/badge/license-LGPL--3-blue.png
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3

.. |badge3| image:: https://img.shields.io/badge/powered%20by-yodoo.systems-00a09d.png
    :target: https://yodoo.systems
    
.. |badge5| image:: https://img.shields.io/badge/maintainer-CR&D-purple.png
    :target: https://crnd.pro/

.. |badge6| image:: https://img.shields.io/badge/GitHub-Generic_Mixin-green.png
    :target: https://github.com/crnd-inc/generic-addons/tree/11.0/generic_mixin


|badge1| |badge2| |badge5| |badge6|

This is technical addon, that contains model mixins, that may be useful
in develompent of other addons.

Following mixins ara available:
- ``generic.mixin.name_with_code`` - just add ``name`` and ``code`` fields to model, on name changed - compute code automatically.
- ``generic.mixin.uniq_name_code`` - add *unique* constraint to name and code fields.
- ``generic.mixin.name.by.sequence`` - Add *name* field to your model, that will be automatically filled with value based on ``ir.sequence`` (in same way as in sale order, or other odoo models)
- ``generic.mixin.namesearch.by.fields`` - Easily add name search that allows to search by a set of fields.
- ``generic.mixin.transaction.utils`` - utility methods to handle transactions in Odoo.
- ``generic.mixin.no.unlink`` - deny unlink of specific records in model.
- ``generic.parent.names`` - implement ``name_get`` and ``name_search`` for hierarchial models in generic way
- ``generic.mixin.refresh.view`` - provides methods to refresh views in browser from python
- ``generic.mixin.track.changes`` - provides convenient mechanism to handle changes of specific fields.
- ``generic.mixin.uuid`` - Easy way to generate UUIDs for records in your model

Also, there are ``pre_write``, ``post_write``, ``pre_create`` and ``post_create``  decoratrors,
that could be used together with ``generic.mixin.track.changes``.
These decorators could signifiantly simplify code.

This module is part of the Bureaucrat ITSM project. 
You can try it by the references below.

Launch your own ITSM system in 60 seconds:
''''''''''''''''''''''''''''''''''''''''''

Create your own `Bureaucrat ITSM <https://yodoo.systems/saas/template/bureaucrat-itsm-demo-data-95>`__ database

|badge3| 


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/crnd-inc/generic-addons/issues>`_.
In case of trouble, please check there if your issue has already been reported.


Maintainer
''''''''''
.. image:: https://crnd.pro/web/image/3699/300x140/crnd.png

Our web site: https://crnd.pro/

This module is maintained by the Center of Research & Development company.

We can provide you further Odoo Support, Odoo implementation, Odoo customization, Odoo 3rd Party development and integration software, consulting services. Our main goal is to provide the best quality product for you. 

For any questions `contact us <mailto:info@crnd.pro>`__.

