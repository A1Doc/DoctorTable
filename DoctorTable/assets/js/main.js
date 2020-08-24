//whole functions will run after document loaded
$(document).ready(function () {
  $("#myfile").change(function () {
    var fileSize = $("#myfile")[0].files[0].size;
    var fileType = $("#myfile")[0].files[0].type;

    if (fileSize > 0 && fileType == "application/pdf") {
      $("#fileDesc").html(
        "<p style='color:green'>File size: " +
          fileSize / 1000 +
          "kb<br>File Type: " +
          fileType +
          "</p>"
      );
      $("#btn").button("enable");
    } else {
      $("#fileDesc").html(
        "<p style='color:#FF0000'>Please select pdf file</p>"
      );
      //alert("Please select pdf file")
    }
  });

  $("#btn").button({
    disabled: true,
  });
});
