numDocente = int(input("Ingrese el numero de docentes que se registrarán en el personal Academico: "))

class personalAcademico:
    """
    Una clase para representar al personal académico
    ........................................
    Atributos
    ----------------------------------------
    nombre : str
        primer nombre del docente
    apellido : str
        apellido del docente
    edad : int
        edad del docente 
    ----------------------------------------
    Métodos
    ----------------------------------------
    regDocente(self, nombre, apellido, edad)
        registra datos del docente
    """
    def __init__(self, nombre, apellido, edad):
        """
        Construye todos los atributos necesarios para el objeto personalAcademico.
        -----------------------------
        Parámetros
        -----------------------------
        nombre : str
            nombre del docente
        apellido : str
            apellido del docente
        edad: int
            edad del docente 
        """
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def regDocente(self, nombre, apellido, edad, docente):
        docente=[]
        print("-------------------------------------------")
        print("         REGISTRO   PERSONAL")
        print("-------------------------------------------")

        if numDocente >= 1:
           """
           Condicional if
            Para el número de docentes a ingresar debe ser mayor a 0
        """
           for i in range(numDocente):
               """
               Condicional for
               Asigna los valores de acuerdo al numero de docentes seleccionado previamente
               """
               print("Ingrese los datos del docente N°", str(i+1),":", end="")
               valor=str(input())
               docente+=[valor] 
               print(input("Ingrese el nombre del docente: ", self.nombre ))
               print(input("Ingrese el apellido del docente: ", self.apellido ))
               print(input("Ingrese la edad del docente: ", self.edad ))

        elif numDocente <= 0: #condición elif para numero de docentes menores a 1
            print("No se puede ingresar menos de 1 es")
        else: 
            pass


class docente(personalAcademico):
    """
    Una clase para representar un docente que forma parte del personal académico | Hereda la clase personalAcademico
    ........................................
    Atributos
    ----------------------------------------
    rol : str
        rol del docente
    departamento : str
        departamento del docente
    salario : float
        salario del docente
    ----------------------------------------
    Métodos
    ----------------------------------------
    regCuenta(self, usuario, contra, contra1)
        registra una cuenta mediante usuario y validación de contraseña
    """
    def __init__(self, rol, departamento, salario):
        """
        Construye todos los atributos necesarios para el objeto empleado.
        -----------------------------
        Parámetros
        -----------------------------
        nombre : str
            primer nombre del cliente
        telefono : str
            telefono del cliente
        estado : str
            estado del cliente 
        """
        self.rol=rol
        self.departamento=departamento
        self.salario=salario
    def regDatosDocente(self, rol, departamento, salario):
        
        print("-------------------------------------------")
        print("          ACTUALIZAR DATOS DOCENTE "  )
        print("-------------------------------------------")
        print(input("Ingrese el rol del docente", rol ))
        print(input("Ingrese el departamento", departamento ))
        print(input("Imgrese el salario", salario))
        
p = personalAcademico()
print(p)
d = docente()
print(d)


