<odoo>
  <data>

    <!-- explicit list view definition -->

    <record model="ir.ui.view" id="practicasfct.alumno_tree">
      <field name="name">Alumno</field>
      <field name="model">practicasfct.alumno</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
          <field name="apellidos"/>
          <field name="fechanacimiento"/>
          <field name="cicloformativo"/>
          <field name="notamedia"/>
        </tree>
      </field>
    </record>

    <record model="ir.ui.view" id="practicasfct.alumno_form">
          <field name="name">Alumno</field>
          <field name="model">practicasfct.alumno</field>
          <field name="arch" type="xml">
            <form>
              <group>
                <field name="name"/>
                <field name="apellidos"/>
                <field name="fechanacimiento"/>
                <field name="cicloformativo"/>
                <field name="notamedia"/>
                <field name="notamediatexto"/>
                <field name="empresa"/>
              </group>
            </form>
          </field>
    </record>


    <record model="ir.ui.view" id="practicasfct.empresa_tree">
              <field name="name">Empresa</field>
              <field name="model">practicasfct.empresa</field>
              <field name="arch" type="xml">
                <tree>
                  <field name="name"/>
                  <field name="direccion"/>
                  <field name="alumnos"/>
                </tree>
              </field>
    </record>
    <record model="ir.ui.view" id="practicasfct.empresa_form">
                  <field name="name">Empresa</field>
                  <field name="model">practicasfct.empresa</field>
                  <field name="arch" type="xml">
                    <form>
                      <group colspan="2" col="2">
                      <field name="name"/>
                        <field name="direccion"/>
                        <field name="alumnos">
<!--Lo dejamos abierto y metemos una vista tree igual no va aquí -->
                            <tree>
                              <field name="name"/>
                              <field name="apellidos"/>
                            </tree>
                        </field>
                      </group>
                    </form>
                  </field>
    </record>

    <record model="ir.ui.view" id="practicasfct.alumno_search">
        <field name="name">Alumnos</field>
        <field name="model">practicasfct.alumno</field>    <!--Modelo sobre el que tiramos -->
        <field name="arch" type="xml">
                    <search>
                      <field name="name" string="Nombre"/> <!--Campos por los que buscar-->
                      <field name="apellidos" string="Apellidos"/> <!--  &lt; o &gt; son los códigos XML para <>-->
                      <filter name="notamedia" domain="[('notamedia','&gt;',9)]"/>
                    </search>
                  </field>
            </record>
    <record model="ir.ui.view" id="practicasfct.empresa_search">
                    <field name="name">Empresa</field>
                    <field name="model">practicasfct.empresa</field>    <!--Modelo sobre el que tiramos -->
                    <field name="arch" type="xml">
                      <search>
                        <field name="name" string="Nombre"/> <!--Campos por los que buscar-->
                      <!--<filter name="baratos" dominio="[('precio','&lt;=',5)]"/>-->
                      </search>
                    </field>
    </record>

                <!-- ACCION VENTANA  -->
                  <!-- Tendremos dos una para categoria y otra para libro -->
    <record model="ir.actions.act_window" id="practicasfct.alumno_action_window">
      <field name="name">Alumnos</field>
      <field name="res_model">practicasfct.alumno</field>
      <field name="view_mode">tree,form</field>
    </record>
    <record model="ir.actions.act_window" id="practicasfct.empresa_action_window">
      <field name="name">Empresa</field>
      <field name="res_model">practicasfct.empresa</field>
      <field name="view_mode">tree,form</field>
    </record>

    <!-- server action to the one above -->
    <!--
    <record model="ir.actions.server" id="practicasfct.action_server">
      <field name="name">practicasfct server</field>
      <field name="model_id" ref="model_practicasfct_practicasfct"/>
      <field name="code">
        action = {
          "type": "ir.actions.act_window",
          "view_mode": "tree,form",
          "res_model": self._name,
        }
      </field>
    </record>
    -->

    <!-- Top menu item -->

    <menuitem name="practicasfct" id="practicasfct.menu_root"/>

    <!-- menu categories -->

    <menuitem name="Alumnos" id="practicasfct.alumno_menu" action="practicasfct.alumno_action_window" parent="practicasfct.menu_root"/>
    <menuitem name="Empresa" id="practicasfct.empresa_menu" action="practicasfct.empresa_action_window"  parent="practicasfct.menu_root"/>

    <!-- actions -->
    <!--
    <menuitem name="List" id="practicasfct.menu_1_list" parent="practicasfct.menu_1"
              action="practicasfct.action_window"/>
    <menuitem name="Server to list" id="practicasfct" parent="practicasfct.menu_2"
              action="practicasfct.action_server"/>
    -->
  </data>
</odoo>
