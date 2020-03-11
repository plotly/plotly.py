:mod:`{{module}}`.{{objname}}
{{ underline }}============================


.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}

   {% block methods %}
   .. automethod:: __init__
   {% endblock %}


{{ underline }}================================

.. autosummary::
   
   plotly.graph_objects.{{ objname.lower() }}

.. automodule:: plotly.graph_objects.{{ objname.lower() }}
   :members:
   :undoc-members:


.. raw:: html

    <div class="clearer"></div>
