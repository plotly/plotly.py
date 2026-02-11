from graphviz import Digraph

# Crear el diagrama
dot = Digraph(comment='Proceso Presupuestal Colombia', format='png')
dot.attr(rankdir='TB', size='8,10')

# Estilos
dot.attr('node', shape='rectangle', style='filled', fontname='Helvetica')

# Nodos Ejecutivo
dot.node('A', 'Elaboración\n(Ejecutivo)', fillcolor='lightblue')
dot.node('B', 'Presentación\n(Ejecutivo)', fillcolor='lightblue')
dot.node('E', 'Sanción\n(Ejecutivo)', fillcolor='lightblue')
dot.node('F', 'Liquidación\n(Ejecución del presupuesto)', fillcolor='lightblue')

# Nodos Legislativo
dot.node('C', 'Estudio\n(Legislativo)', fillcolor='lightgreen')
dot.node('D', 'Aprobación\n(Legislativo)', fillcolor='lightgreen')

# Conexiones
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')

# Renderizar
dot
