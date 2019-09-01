# -*- coding: utf-8 -*-
#Primero hay que tocar manifest
from odoo import models, fields, api

class libreria_categoria(models.Model):
    _name = 'libreria.categoria'

    #Vamos a crear los campos
    #siempre tiene que tener un campo name OBLIGATORIO, el resto de los campos da igual el nombre
    name = fields.Char(string="Nombre categoría", help="Introduce el nombre de la categoría",required=True) #string="Nombre categoría" sería la etiqueta que sale al lado del campo
    #poner parametro help --> salta la ayuda
    #required=True --> campo requerido, si no lo ponemos creemos que va en false
    descripcion = fields.Text(string="Descripción", help="Introduce la descripción de la categoría",required=False)

    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100

class libreria_libro(models.Model):
    _name = 'libreria.libro'

    #Vamos a crear los campos
    #siempre tiene que tener un campo name OBLIGATORIO, el resto de los campos da igual el nombre
    name = fields.Char(string="Título", help="Introduce el título del libro",required=True) #string="Nombre categoría" sería la etiqueta que sale al lado del campo
    #poner parametro help --> salta la ayuda
    #required=True --> campo requerido, si no lo ponemos creemos que va en false
    precio=fields.Float(string="Precio", help="Introduce el precio del libro",required=True) #string="Nombre categoría" sería la etiqueta que sale al lado del campo
    ejemplares=fields.Integer(string="Ejemplares", help="Introduce el número de ejemplares",required=True) #string="Nombre categoría" sería la etiqueta que sale al lado del campo
    fecha = fields.Date(string="Fecha publicación", help="Introduce la fecha publicació",required=False)
    segmano = fields.Boolean(string="Segunda mano", help="Introduce si el libro es de segunda mano o nuevo",required=True)
    descripcion = fields.Text(string="Descripción", help="Introduce la descripción del libro",required=False)
    estado = fields.Selection([('0','Malo'),('1','Regular'),('2','Bueno')],default='2',string="Estado", help="Selecciona el estado del libro",required=False)#para darle las opciones al combo --> es una lista, en cada elemento hay una tupla
    #[('0','Malo'),('1','Regular'),('2','Bueno')],default='2', obligatorio meterlo
