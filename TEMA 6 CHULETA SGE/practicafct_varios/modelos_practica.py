# -*- coding: utf-8 -*-

from odoo import models, fields, api

class practicasfct_alumno(models.Model):
    _name = 'practicasfct.alumno'

    name = fields.Char(string="Nombre", help="Introduce el nombre del alumno",required=True)
    apellidos = fields.Char(string="Apellidos", help="Introduce los apellidos del alumno",required=True)
    fechanacimiento= fields.Date(string="Fecha de nacimiento", help="Introduce la fecha de nacimiento",required=True)
    cicloformativo = fields.Selection([('0','DAM'),('1','DAW'),('2','ASIR')],default='0',string="Clico formativo", help="Selecciona el ciclo que está cursando el alumno",required=False)
    #para darle las opciones al combo --> es una lista, en cada elemento hay una tupla

    #manyToone un estudiante solo puede tener una empresa de prácticas, (contra objeto que queremos la relacion, nombre, campo requerido, que pasa cuando se borra)
    #tira sobre name, por eso hay que ponerlo siempre
    empresa = fields.Many2one("practicasfct.empresa",string="Empresa", required=True,ondelete="cascade", help="Selecciona la empresa de prácticas.")
    #Si la nota numérica está entre 5 y 7: aprobado; entre 7 y 9: notable; entre 9 y 10:sobresaliente.

    notamedia = fields.Float(string="Nota media", help="Introduce la nota media del alumno.",required=False)
    notamediatexto = fields.Char(string="Nota media texto", help="Nota media", compute="_notamediatexto",store=True)
    #store = True --> es para que se calcule solo en determinados casos, cuando se modifique el campo

    #cadena de texto, campo calculado como se indica más abajo
    #Si la nota numérica está entre 5 y 7: aprobado; entre 7 y 9: notable; entre 9 y 10:sobresaliente.
    #@api.depends('notamedia') --> si le ponemos una dependencia, recalculará cuando se actualice el campo entre paréntesis
    #en este caso el self es una colección entonces lo tendremos que recorrecor con un for
    @api.depends('notamedia')
    def _notamediatexto(self):
        for r in self:
            if (r.notamedia <5):
                r.notamediatexto='suspenso'
            elif (r.notamedia <7):
                r.notamediatexto='aprobado'
            elif (r.notamedia <9):
                r.notamediatexto='notable'
            elif (r.notamedia >=9):
                r.notamediatexto='sobresaliente'
            elif (r.notamedia >10):
                r.notamediatexto='No puedes tener más de un 10'


    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100
class practicasfct_empresa(models.Model):
    _name = 'practicasfct.empresa'

    name = fields.Char(string="Nombre", help="Introduce el nombre de la empresa.",required=True)
    direccion = fields.Char(string="Dirección", help="Introduce la dirección de la empresa.",required=False)
    #listaalumnos
    #muchos a uno, aquí si hay que poner contra el campo con el que lo lanzamos --> empresa como el parametro que pusimos antes en las relaciones
    alumnos = fields.One2many("practicasfct.alumno","empresa",string="Alumnos")
