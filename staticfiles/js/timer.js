CountDownTimer('08/16/2022', 'applystart');
CountDownTimer('08/23/2022', 'applyend');
CountDownTimer('08/27/2022', 'programstart');

function CountDownTimer(dt, id) {
	
	var end = new Date(dt);
	
	var _second = 1000;
	var _minute = _second * 60;
	var _hour = _minute * 60;
	var _day = _hour * 24;
	var timer;
	
	function showRemaining() {
		var now = new Date();
		var distance = end - now;
		if (distance < 0) {
			clearInterval(timer);
			// document.getElementById(id).innerHTML = 'EXPIRED!';
			
			return;
		}
		
		var days = Math.floor(distance / _day);
		var hours = Math.floor((distance % _day) / _hour);
		var minutes = Math.floor((distance % _hour) / _minute);
		var seconds = Math.floor((distance % _minute) / _second);
		
		// const applystart = new Date("2022-08-16T00:00:00z");
		// const applyend = Date("2022-08-23T23:59:59z");
		// const programstart = Date("2022-08-27T18:30:00z");
		
		// if(now<=applystart) {
		// 	document.getElementById(id).innerHTML = 'D-' + days + ' ';
		// 	document.getElementById(id).innerHTML += hours + ' : ';
		// 	document.getElementById(id).innerHTML += minutes + ' : ';
		// 	document.getElementById(id).innerHTML += seconds;
		// } else if(applystart<now<=applyend) {
		// 	document.getElementById(id).innerHTML = 'D-' + days + ' ';
		// 	document.getElementById(id).innerHTML += hours + ' : ';
		// 	document.getElementById(id).innerHTML += minutes + ' : ';
		// 	document.getElementById(id).innerHTML += seconds;
		// }
		// else if(applyend<now==programstart) {
		// 	document.getElementById(id).innerHTML = 'D-' + days + ' ';
		// 	document.getElementById(id).innerHTML += hours + ' : ';
		// 	document.getElementById(id).innerHTML += minutes + ' : ';
		// 	document.getElementById(id).innerHTML += seconds;
		// }
		
		document.getElementById(id).innerHTML = 'D-' + days + ' ';
		document.getElementById(id).innerHTML += hours + ' : ';
		document.getElementById(id).innerHTML += minutes + ' : ';
		document.getElementById(id).innerHTML += seconds;
		
		timer = setInterval(showRemaining, 1000);
	};
}
