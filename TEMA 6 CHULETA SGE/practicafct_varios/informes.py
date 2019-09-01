<odoo>
  <data>
    <report
      id="practicasfct.report_empresa"
      model="practicasfct.empresa"
      string="Informe empresa"
      name="practicasfct.report_empresa_view"
      file="practicasfct.report_empresa_view"
      report_type="qweb-pdf"/>

      <template id="practicasfct.report_empresa_view">

      <t t-call="report.html_container">
        <t t-foreach="docs" t-as="empresa">
          <t t-call="report.external_layout">
            <div class="page">
              <h2 t-field="empresa.name"/>
            </div>
            <div class="page">
              <strong>Alumnos en prácticas:</strong>
              <span t-field="empresa.alumnos"/>
            </div>
          </t>
        </t>
      </t>
    </template>

  </data>
</odoo>
