$.get( "/schema/form-1065", function( data ) {
  const schema = JSON.parse(data);
  console.log(schema);
  $("#target").jsonForm({
    schema,
    onSubmit: (error, values ) => {
      const beginning_date = values["beginning_date"];
      const peid = values["partnership_employer_identification_number"];
      const id = beginning_date + "-" + peid;


      $.ajax({
        url: "/data/" + id,
        type: "PUT",
        data: JSON.stringify(values)
      });
    },
    value: {"beginning_date":"dfsadf","partnership_employer_identification_number":"gdfhgfd","is_publicly_traded_partnership":false,"partner_section_704b_book":false}
  })

});