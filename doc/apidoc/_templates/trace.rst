:mod:`{{module}}`.{{objname}}
{{ underline }}============================


.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}

   {% block methods %}
   .. automethod:: __init__
   {% endblock %}

:mod:`{{module}}`.{{objname.lower()}}
{{ underline }}================================

.. autosummary::
   
   plotly.graph_objs.{{ objname.lower() }}

.. automodule:: plotly.graph_objs.{{ objname.lower() }}
   :members:
   :undoc-members:


.. raw:: html

    <div class="clearer"></div>
