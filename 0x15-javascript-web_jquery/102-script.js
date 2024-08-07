// JavaScript script that fetches and prints how to say “Hello”
// depending on the language
$(document).ready(() => {
	$("#btn_translate").click(() => {
		const langCode = $("#language_code").val();
		const apiU = `https://www.fourtonfish.com/hellosalut/hello/${langCode}`;

		$.get(apiU, (data) => {
				$("#hello").text(data.hello);
			});
	});
});
