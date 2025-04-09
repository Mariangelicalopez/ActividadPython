class Contacto:
    # Método constructor: inicializa un nuevo contacto con nombre, apellido, correo y teléfono
    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre  
        self.apellido = apellido  
        self.correo = correo  
        self.telefono = telefono 

    # Método para actualizar los datos del contacto. Solo cambia los datos que se ingresen.
    def actualizar(self, nombre=None, apellido=None, correo=None, telefono=None):
        if nombre:
            self.nombre = nombre  
        if apellido:
            self.apellido = apellido  
        if correo:
            self.correo = correo  
        if telefono:
            self.telefono = telefono  #

    # Método especial para mostrar el contacto en formato legible cuando se imprime
    def __str__(self):
        return f"{self.nombre} {self.apellido} - Email: {self.correo} - Tel: {self.telefono}"

    # Convierte el objeto Contacto en un diccionario para poder guardarlo como JSON
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "telefono": self.telefono
        }
    
    # Método estático para crear un objeto Contacto a partir de un diccionario (cuando leemos el JSON)
    @staticmethod
    def from_dict(data):
        return Contacto(data["nombre"], data["apellido"], data["correo"], data["telefono"])