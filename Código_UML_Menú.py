classDiagram
direction TB
    class Aperitivo {
	    +nombre: str
	    +precio: float
	    +__str__()
    }

    class Bebidas {
	    +nombre: str
	    +precio: float
	    +tamaño: str
	    +__str__()
	    +get_tamaño()
	    +set_tamaño(nuevo_tamaño: str)
    }

    class Plato_principal {
	    +nombre: str
	    +precio: float
	    +cantidad: str
	    +get_cantidad()
	    +set_cantidad(nueva_cantidad: str)
	    +__str__()
    }

    class Orden {
	    +elementos: List[Menu]
	    +agregar_elemento()
	    +calcular_factura()
	    +hacer-descuento()
	    +mostrar_pedido()
    }

    class Menu {
	    +nombre: str
	    +precio: float
	    +calcular_precio()
	    +__str__()
    }

    Menu "1" <|-- "1" Bebidas
    Menu "1" <|-- "1" Plato_principal
    Menu "1" <|-- "1" Aperitivo
    Menu "0" <|.. "n" Orden

	classDef Peach :, stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D
	classDef Sky :, stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C



