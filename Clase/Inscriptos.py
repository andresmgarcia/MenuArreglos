__author__ = 'AndresMartinGarcia'

class Inscriptos:
    def __init__(self,dni,nombre,curso,forma,monto):
        self.dni = dni
        self.nom = nombre
        self.curso = curso
        self.forma = forma
        self.monto = monto


def toString(reg):
    r="{:^10}|".format(reg.dni)
    r+="{:^10}|".format(reg.nom)
    r+="{:^10}|".format(reg.curso)
    r+="{:^10}|".format(reg.forma)
    r+="{:^10}|".format(reg.monto)
    return  r

def toString_archi(reg):
    r="{:^10}".format(reg.dni)
    r+="{:^10}".format(reg.nom)
    r+="{:^10}".format(reg.monto)
    return  r


def encabeza():
    r ="{:^10}".format("ID")
    r+="{:^10}".format("NOMBRE")
    r+="{:^10}".format("CURSO")
    r+="{:^12}".format("FORMA DE PAGO ")
    r+="{:^10}".format("MONTO")
    return  r