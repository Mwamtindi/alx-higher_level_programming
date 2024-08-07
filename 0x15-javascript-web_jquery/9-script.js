// javaScript script that fetches from url and display value hello
$("document").ready(function () {
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
    $("DIV#hello").text(data.hello);
  });
});
