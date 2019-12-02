:mod:`{{module}}`.{{objname}}
{{ underline }}==============


.. currentmodule:: {{ module }}

.. autosummary::
   :toctree: generated/

   Figure

   Figure.show
   Figure.add_traces
   Figure.update_traces
   Figure.update_layout


.. autoclass:: {{ objname }}
   {% block methods %}
   .. automethod:: __init__
   {% endblock %}


.. autoclass:: {{ objname }}
   :members:
   :inherited-members:

.. raw:: html

    <div class="clearer"></div>

