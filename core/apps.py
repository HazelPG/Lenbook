from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    #layout = 'horizontal'
    name = 'suit'
    verbose_name = 'Django Suit'
    # Menu and header layout - horizontal or vertical
    layout = 'vertical'

    # Set default list per page
    list_per_page = 20

    # Show changelist top actions only if any row is selected
    toggle_changelist_top_actions = True

    # Define menu
    #: :type: list of suit.menu.ParentItem
    menu = (
        ParentItem('Prestamos', children=[
            ChildItem(model='prestamos.prestamo'),
            ChildItem('Prestar ', url='/admin/Prestamo/Prestar/'),
            #ChildItem(model='prestamos.detalleprestamo'),
        ]),
        ParentItem('Academia', children=[
            ChildItem(model='personas.personas'),
        ]),
        ParentItem('Libros', children=[
             ChildItem(model='libros.libro'),
             ChildItem(model='libros.autores'),
             ChildItem(model='libros.tipolibro'),

        ]),
        ParentItem('Incidentes', children=[
            ChildItem(model='prestamos.incidente'),
            # ChildItem(model='prestamos.detalleincidente'),
        ]),
        ParentItem('Reportes', children=[
            ChildItem('Reporte ', url='/admin/Reporte/'),
        ]),

        ParentItem('Usuarios', children=[
            ChildItem(model='auth.user'),
            ChildItem(model='auth.group')
        ]),
        ParentItem('Configuracion', children=[
            ChildItem(model='configuracion.programa'),
            ChildItem(model='personas.codigoacceso'),
            ChildItem(model='personas.tipopersona'),
        ]),

    )
