// JavaScript script that fetches and prints how to say “Hello”
// depending on the language
$(document).ready(function () {
	function fetchTranslation() {
		const langCode = $("#language_code").val();
		const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${langCode}`;

		$.get(apiUrl, function (data) {
			$("#hello").text(data.hello);
		}
		);

	}

	$("#btn_translate").click(fetchTranslation);
	$("#language_code").keypress(function (e) {
		if (e.which === 13) {
			fetchTranslation();
		}
	}
	);
}
);
