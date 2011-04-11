/**
 * Allgemeine Javascript-Datei für die Futurezone
 */

/**
 * Nimmt die Dummy-LI-Elemente der Werbung aus den Übersichts-Seiten heraus
 */
$(document).ready(function() {
	$('.oas_inlist').each(function() {
		$('script:first', this).remove();
		var content = $(this).html();
		$(this).replaceWith(content);
	});
});


/**
 * Leert den Inhalt des übergebenen Objekts
 */
function clearField(objekt) {
	if(objekt.value == 'Suchen nach') {
		objekt.value = '';
	}
}

/**
 * Berechnet und setzt das "Update: vor x Minuten"-Feld
 */
function setUpdateInfoBox(timestamp) {
	if (timestamp == undefined || timestamp == null || timestamp == 0) {
		return;
	}
	var now = new Date();
	var diffSec = Math.floor(now.getTime() / 1000) - timestamp;
	var diffMin = Math.floor(diffSec / 60);
	var diffHours = Math.floor(diffMin / 60);
	var diffDays = Math.floor(diffHours / 24);

	var text = 'Update: vor '
	if (diffDays > 0) {
		text += diffDays + ' Tag';
		if (diffDays > 1) {
			text += 'en';
		}
	} else if (diffHours > 0) {
		text += diffHours + ' Stunde';
		if (diffHours > 1) {
			text += 'n';
		}
	} else if (diffMin > 0) {
		text += diffMin + ' Minute';
		if (diffMin > 1) {
			text += 'n';
		}
	} else {
		text += '1 Minute';
	}
	$('.information .updateinfo').html(text);
}

/*
 * ÖWA Zählpixel generierem
 */
function initOewaCounter(oewasrc)
{
	var OEWAsrc = oewasrc;
	//var OEWAsrc = OEWAsrc + "?r="+escape(document.referrer)+"&d="+(new Date()).getTime();
	var zaehlpixelPic = new Image();
	zaehlpixelPic.src = OEWAsrc;
}