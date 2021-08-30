const questionNumber = document.querySelector(".question-number");
const questionText = document.querySelector(".question-text");
const optionContainer = document.querySelector(".option-container");
const answerIndicatorContainer = document.querySelector(".answer-indicator")
const homeBox = document.querySelector(".home-box");
const quizBox = document.querySelector(".quiz-box");
const resultBox = document.querySelector(".result-box");
const time_line = document.querySelector("header .time_line");
const timeText = document.querySelector(".timer .time_left_txt");
const timeCount = document.querySelector(".timer .timer_sec");
const dialog = document.querySelector(".confirm");
const dialogText = document.querySelector(".confirm .confirm-title");
const dialogDesc = document.querySelector(".confirm .confirm-desc");
const menu = document.querySelector(".menu");
const register = document.querySelector(".register-box");
const intro = document.querySelector(".intro-box");
const form = document.querySelector(".login-form");

let questionCounter = 0;
let currentQuestion;
let availableQuestion = [];
let availableOptions = [];
let correctAnswer = 0;
let attempt = 0;
let questionOrder = []; //array of id q, ref from question.js
questAnsw = {};
questSieve = {};
let currentPage = 0;
let arrayReady = []; //random of q id
let optionReady = []; //random of option ready
let counter;
let counterLine;
let quizTime = 5400;
let audio = new Audio('static/sound/music.webm');
let correctChess = 0;
let correctFootball = 0;
let correctGeography = 0;
let correctMath = 0;
let correctKognitif = 0;
let correctSosio = 0;
let correctFisik = 0;

function setAvailableQuestions(){
	const totalQuestion = quiz.length;
	for( let i=0; i<totalQuestion; i++){
		availableQuestion.push(quiz[i]);
	}
}

function setQuestAnswSieve(){
	for (let i = 0; i < quiz.length; i++){
		questAnsw[i+1] = -1;
		questSieve[i+1] = 0;
	}
}

function getQuestionOrder(){
	const totalQuestion = quiz.length;
	let numArray = [];
	for (let i = 0; i < totalQuestion; i++){
		numArray.push(i);
	}
	for (let i = 0; i < totalQuestion; i++){
		const num = numArray[Math.floor(Math.random() * numArray.length)];
		arrayReady.push(num);
		const index = numArray.indexOf(num);
		numArray.splice(index,1);
	}
}
//temporary : assume each q has 4 options
function getOptionOrder(){
	let numArray = [0,1,2,3];
	let tempArray = [];
	for (let j = 0; j < quiz.length; j++){
		for (let i = 0; i < 4; i++){
			const num = numArray[Math.floor(Math.random() * numArray.length)];
			//console.log(num);
			tempArray.push(num);
			const index = numArray.indexOf(num);
			numArray.splice(index,1);
		}
		optionReady.push(tempArray);
		tempArray = [];
		numArray = [0,1,2,3];
	}
}

function getNewQuestion(){
	questionNumber.innerHTML = "Question " + (currentPage) + " of " + quiz.length;

	/*
	// random
	const questionIndex = availableQuestion[Math.floor(Math.random() * availableQuestion.length)]
	// get the pos of questionIndex from availableQ array
	const index1 = availableQuestion.indexOf(questionIndex);
	// remove index1 from available
	//availableQuestion.splice(index1,1);
	*/
	const questionIndex = availableQuestion[arrayReady[currentPage-1]];
	//console.log(arrayReady);
	//console.log(currentPage);
	currentQuestion = questionIndex;
	questionText.innerHTML = currentQuestion.q;

	const optionLen = currentQuestion.options.length;
	for (let i=0; i<optionLen; i++){
		availableOptions.push(i)
	}
	optionContainer.innerHTML = '';
	let animationDelay = 0.15;
	for (let i=0; i<optionLen; i++){
		const optionIndex = availableOptions[Math.floor(Math.random() * availableOptions.length)];
		const index2 = availableOptions.indexOf(optionIndex);
		availableOptions.splice(index2,1);
		//console.log(optionIndex)
		const option = document.createElement("div");
		option.innerHTML = currentQuestion.options[optionIndex];
		option.id = optionIndex;
		option.style.animationDelay = animationDelay + 's';
		animationDelay += 0.15;
		option.className = "option";
		optionContainer.appendChild(option)
		option.setAttribute("onclick", "getResult(this)");
	}
	questionCounter++;
	questionOrder.push(questionIndex.id);
}

function getQuestionNo(page){
	
	const questionIndex = availableQuestion[arrayReady[page-1]];
	currentQuestion = questionIndex;
	questionText.innerHTML = currentQuestion.q;
	questionNumber.innerHTML = "Question " + (page) + " of " + quiz.length + " - " + currentQuestion.category;

	optionContainer.innerHTML = '';
	let animationDelay = 0.15;
	for (let i=0; i < 4; i++){
		const option = document.createElement("div");
		option.innerHTML = currentQuestion.options[optionReady[page-1][i]];
		option.id = optionReady[page-1][i];
		option.style.animationDelay = animationDelay + 's';
		animationDelay += 0.15;
		option.className = "option";
		optionContainer.appendChild(option)
		option.setAttribute("onclick", "getSelect(this.id)");
	}

	//mark if already answer
	options = optionContainer.getElementsByClassName("option");
	for (let i=0; i<options.length; i++){
		options[i].classList.remove("selected");
		if(questAnsw[questionOrder[currentPage-1]] != -1){
			if (options[i].id === questAnsw[questionOrder[currentPage-1]]){
				options[i].classList.add("selected");
			}
		}
	}
	console.log(questionOrder);
}

function pushAllQuestion(){
	let questionIndex = "";
	for(let i=0; i<quiz.length; i++){
		console.log(i);
		questionIndex = availableQuestion[arrayReady[i]];
		console.log(questionIndex);
		questionOrder.push(questionIndex.id);
	}
}

function getSelect(id){
	options = optionContainer.getElementsByClassName("option");
	questAnsw[questionOrder[currentPage-1]] = id;
	
	for (let i=0; i<options.length; i++){
		options[i].classList.remove("selected");
		if (options[i].id === id){
			options[i].classList.add("selected");
		}
	}
	
	console.log(currentPage-1);
	console.log("This : " + questionOrder[currentPage-1]);
	if(id == currentQuestion.answer){
		questSieve[questionOrder[currentPage-1]] = 1;
		/*
		if(currentQuestion.category == "Chess"){correctChess++;}
		if(currentQuestion.category == "Football"){correctFootball++;}
		if(currentQuestion.category == "Geography"){correctGeography++;}
		if(currentQuestion.category == "Math"){correctMath++;}*/
		if(currentQuestion.category == "Aspek Kognititf"){correctKognitif++;}
		if(currentQuestion.category == "Aspek Sosio Emosional"){correctSosio++;}
		if(currentQuestion.category == "Aspek Fisik"){correctFisik++;}

	}else{
		questSieve[questionOrder[currentPage-1]] = -1;
	}
	updateAnswerIndicator("selected");
}

function getResult(element){
	//console.log(element);
	const id = parseInt(element.id);
	questAnsw[questionOrder[currentPage-1]] = id;
	//console.log(questAnsw);
	if(id === currentQuestion.answer){
		element.classList.add("correct");
		updateAnswerIndicator("correct");
		questSieve[questionOrder[currentPage-1]] = 1;
		correctAnswer++;
	}else{
		element.classList.add("wrong");
		updateAnswerIndicator("wrong");
		questSieve[questionOrder[currentPage-1]] = -1;

		const optionLen = optionContainer.children.length;
		for(let i=0; i<optionLen; i++){
			if(parseInt(optionContainer.children[i].id) === currentQuestion.answer){
				optionContainer.children[i].classList.add("correct");
			}
		}
	}
	//console.log(questSieve);
	// remove later
	attempt++;
	unclickableOptions();
}

function answerIndicator(){
	answerIndicatorContainer.innerHTML = "";
	const totalQuestion = quiz.length;
	for(let i=0; i<totalQuestion; i++){
		const indicator = document.createElement("div");
		answerIndicatorContainer.appendChild(indicator);
		indicator.innerHTML = i+1;
		indicator.id = i+1;
		indicator.setAttribute("onclick", "toPage(this.id)");
	}
}

function toPage(num){
	currentPage = num;
	getQuestionNo(num);
}

function updateAnswerIndicator(mark){
	answerIndicatorContainer.children[currentPage-1].classList.add(mark);
}

function next(){
	currentPage++;
	if(currentPage-1 === quiz.length){
		currentPage = 1;
		getQuestionNo(currentPage);
	}else{
		getQuestionNo(currentPage);
	}
}

function prev(){
	currentPage--;
	if(currentPage+1 === 1){
		currentPage = quiz.length;
		getQuestionNo(currentPage);
	}else{
		getQuestionNo(currentPage);
	}
}

function countResult(){
	let notAnsw = 0;
	for (let i = 0; i < quiz.length; i++){
		if (questAnsw[i+1] == -1){
			notAnsw++;
		}
		if (questSieve[i+1] == 1){
			correctAnswer++;
		}

	}
	attempt = quiz.length - notAnsw;
}

function quizOver(){
	quizBox.classList.add("hide");
	resultBox.classList.remove("hide");
	menu.classList.add("hide");
	clearInterval(counter);
    clearInterval(counterLine);
	quizResult();
	closeDialog();
	pauseAudio();
	//submitQuiz();
}

function quizResult(){
	countResult();
	resultBox.querySelector(".total-question").innerHTML = quiz.length;
	resultBox.querySelector(".total-attempt").innerHTML = attempt;
	resultBox.querySelector(".total-correct").innerHTML = correctAnswer;
	resultBox.querySelector(".total-wrong").innerHTML = attempt - correctAnswer;
	const percentage = (correctAnswer/quiz.length)*100;
	resultBox.querySelector(".percentage").innerHTML = percentage.toFixed(2) + "%";
	resultBox.querySelector(".total-score").innerHTML = correctAnswer + " / " + quiz.length;
	/*
	resultBox.querySelector(".chess").innerHTML = correctChess + " / 4 (" + (correctChess/4)*100 + "%)";
	resultBox.querySelector(".football").innerHTML = correctFootball + " / 4 (" + (correctFootball/4)*100 + "%)";
	resultBox.querySelector(".geography").innerHTML = correctGeography + " / 4 (" + (correctGeography/4)*100 + "%)";
	resultBox.querySelector(".math").innerHTML = correctMath + " / 4 (" + (correctMath/4)*100 + "%)";*/
	const kogScore = correctKognitif*100/29
	const sosScore = correctSosio*100/30
	const fisScore = correctFisik*100/28
	resultBox.querySelector(".kognitif").innerHTML = correctKognitif + " / 29 (" + kogScore.toFixed(2) + "%)";
	resultBox.querySelector(".sosio").innerHTML = correctSosio + " / 30 (" + sosScore.toFixed(2) + "%)";
	resultBox.querySelector(".fisik").innerHTML = correctFisik + " / 28 (" + fisScore.toFixed(2) + "%)";

	//for canvas
	let myChart = document.getElementById('myChart').getContext('2d');

	// Global Options
	Chart.defaults.global.defaultFontFamily = 'sans-serif';
	Chart.defaults.global.defaultFontSize = 18;
	Chart.defaults.global.defaultFontColor = '#777';

	var chartData = {
		  labels: [
		    'Kognititf',
		    'Fisik',
		    'Sosio',
		    'Wrong',
		    'Not Answered'
		  ],
		  datasets: [{
		    label: 'Datasets',
		    data: [correctKognitif, correctFisik, correctSosio, attempt - correctAnswer, 91-attempt],
		    backgroundColor: [
		      'rgb(252, 186, 3)',
		      'rgb(10, 188, 242)',
		      'rgb(18, 204, 59)',
		      'rgb(212, 58, 28)',
		      'rgb(166, 157, 156)'
		    ],
		    hoverOffset: 4
		  }]
	};
	let massPopChart = new Chart(myChart, {
	  type:'doughnut',
	  data: chartData,
	  options:{
	    title:{
	      display:true,
	      text:'',
	      fontSize:25
	    },
	    legend:{
	      display:true,
	      position:'bottom',
	      labels:{ fontColor:'#000' }
	    },
	    layout:{
	      padding:{
	        left:50,
	        right:0,
	        bottom:0,
	        top:0
	      }
	    },
	    tooltips:{
	      enabled:true
	    }
	  }
	});

}

function resetQuiz(){
	questionCounter = 0;
	correctAnswer = 0;
	attempt = 0;
	currentPage = 0;
	/*
	correctChess = 0;
	correctFootball = 0;
	correctGeography = 0;
	correctMath = 0;*/
	correctKognitif = 0;
	correctSosio = 0;
	correctFisik = 0;
	arrayReady = [];
	questAnsw = [];
	setQuestAnswSieve();
	getQuestionOrder();
}

function tryAgainQuiz(){
	resultBox.classList.add("hide");
	quizBox.classList.remove("hide");
	resetQuiz();
	startQuiz();
}

function goToHome(){
	resultBox.classList.add("hide");
	quizBox.classList.add("hide");
	homeBox.classList.add("hide");
	menu.classList.add("hide");
	register.classList.remove("hide");
	clearInterval(counter); //clear counter
    clearInterval(counterLine); //clear counterLine
	resetQuiz();
}

function showInstruction(){
	let filled = true;
	document.getElementById("login-form").querySelectorAll("[required]").forEach(function(i){
		if(!filled) return;
		if(!i.value) filled = false;
	})
	if(!filled){
		alert("Isi semua field")
	}else{
		register.classList.add("hide");
		homeBox.classList.remove("hide");
	}
	
}

function showRegister(){
	intro.classList.add("hide");
	register.classList.remove("hide");
}


function startQuiz(){
	setQuestAnswSieve();
	console.log(questAnsw);
	currentPage++;
	getQuestionOrder()
	console.log(arrayReady);
	getOptionOrder()
	console.log(optionReady);
	homeBox.classList.add("hide");
	quizBox.classList.remove("hide");
	menu.classList.remove("hide");
	setAvailableQuestions();
	pushAllQuestion();
	getQuestionNo(1);
	answerIndicator();
	clearInterval(counter);
    clearInterval(counterLine);
	startTimer(quizTime);
	startTimerLine(0);
	loadAudio();
	resumeAudio();
}

function loadAudio(){
	audio.load();
}

function resumeAudio(){
	audio.play();
}

function pauseAudio(){
	audio.pause();
}

function loadAudio(){
	audio.load();
}

function decreaseVolume(){
	audio.volume -= 0.1;
}

function increaseVolume(){
	audio.volume += 0.1;
}

function mutedAudio(){
	audio.volume = 0;
}

let duration = 0;
function startTimer(time){
    counter = setInterval(timer, 1000);
    function timer(){
    	let hour = Math.floor(time/3600);
    	let res = time - hour*3600;
    	let minute = Math.floor(res/60);
    	let second = res - minute*60;
        //timeCount.textContent = "0" + minute + " : " + second; //changing the value of timeCount with time value
        time--; //decrement the time value
        duration++;
        if(second < 10 && minute < 10){ //if timer is less than 9
            //let addZero = timeCount.textContent; 
            timeCount.textContent = "0" + hour + " : 0" + minute + " : 0" + second; //add a 0 before time value
        }else if(second < 10 && minute >= 10){
        	timeCount.textContent = "0" + hour + " : " + minute + " : 0" + second; //changing the value of timeCount with time value
        }else if(second >= 10 && minute < 10){
        	timeCount.textContent = "0" + hour + " : 0" + minute + " : " + second;
        }else{
        	timeCount.textContent = "0" + hour + " : " + minute + " : " + second;
        }
        if (time < 0){
        	clearInterval(counter); //clear counter
        	timeText.textContent = "Off";
        	quizOver();
        }
    }
}

function startTimerLine(time){
    counterLine = setInterval(timer, 1000);
    function timer(){
        time ++; //upgrading time value with 1
        time_line.style.width = Math.floor(time*100/quizTime) + "%"; //increasing width of time_line with px by time value
        if(time > quizTime){ //if time value is greater than quizTime
            clearInterval(counterLine); //clear counterLine
        }
    }
}

function countAttempt(){
	let x = 0;
	for(let i = 0; i<quiz.length; i++){
		if(questAnsw[i] == -1){
			x++;
		}
	}
	return x+1;
}

function showDialog(){
	let notAnsw = countAttempt();
	let text = "";
	if (notAnsw == 1){
		text = "Anda sudah menjawab semua pertanyaan, tetapi masih ada waktu untuk memeriksa jawaban anda kembali. Selesaikan sekarang?";
	}
	else{
		text = "Masih ada " + notAnsw + " soal yang anda belum jawab. Yakin ingin selesaikan quiz?"
	}
	dialogText.textContent = "Finish Quiz?";
	dialogDesc.textContent = text;
	dialog.classList.remove("hide");
}

function closeDialog(){
	dialog.classList.add("hide");
}

const isValidElement = (element) => {
	return element.name && element.value;
}

const formToJSON = (elements) =>
	[].reduce.call(
	elements,
	(data, element) => {
		if(isValidElement(element)){
			data[element.name] = element.value;
		}
		return data;
	},
	{},
);

let userData;

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
let jsonIP = {};
function handleFormSubmit(event, eventElement){
	event.preventDefault();
	const data = formToJSON(form.elements);
	userData = JSON.stringify(data, null, ' ');
	/*
	$.getJSON('https://ipapi.co/json/', function(data) {
	  //console.log(JSON.stringify(data, null, 2));
	    $.each( data, function( key, val ) {
		    //items.push( "<li id='" + key + "'>" + val + "</li>" );
		    jsonIP[key] = val;
		  });
	});*/
	//console.log(jsonIP);
	//send through ajax
	$.ajax({
		type: 'POST',
		url: $(eventElement).data('url'),
		dataType: 'json',
		data: {
			'id' : 1,
			'data' : userData,
			'jsonIP' : JSON.stringify(jsonIP, null, ' '),
		},
		success: function (data){
			if (data.msg === "Success"){
				alert('Form is submitted');
			}else{
				alert('AJAX failed');
			}
		},
		error: function(jqXHR, textStatus, errorThrown) { 
	       //console.log(errorThrown);
	    }
	});
	console.log(userData);
}
function removeOptions(selectElement) {
   var i, L = selectElement.options.length - 1;
   for(i = L; i >= 0; i--) {
      selectElement.remove(i);
   }
}
function onlyNumberKey(evt) {
    var ASCIICode = (evt.which) ? evt.which : evt.keyCode
    if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
        return false;
    return true;
}
function alphaOnly(event) {
  var key = event.keyCode;
  return ((key >= 65 && key <= 90) || key == 8 || key == 32);
}
selectKab = document.getElementById('kabupaten');
let prov;
function getKab(eventElement){
	$.ajax({
		type: 'GET',
		url: $(eventElement).data('url'),
		success: function(response){
			removeOptions(document.getElementById('kabupaten'));
	        console.log(response.data) //works here
	        const carsData = response.data
	        carsData.map(item=>{
	        	const option = document.createElement('option')
	            option.textContent = item.kabupaten
	            option.setAttribute('class', 'item')
	            option.setAttribute('value', item.kabupaten)
	            selectKab.appendChild(option)
	        })
	    },
		complete: function (){
			console.log("ok");
			//removeOptions($("#kabupaten"));
		},
		error: function(jqXHR, textStatus, errorThrown) { 
	       //console.log(errorThrown);
	    }
	});
}
$(document).ready(function() {
	$("#prov").on('change', function(eventElement) {
		//alert( this.value );
		//send through ajax
		prov = this.value;
		$.ajax({
			type: 'POST',
			url: $(eventElement).data('url'),
			dataType: 'json',
			data: {
				'id' : 2,
				'data' : this.value,	
			},
			complete: function (){
				getKab();
			},
			error: function(jqXHR, textStatus, errorThrown) { 
		       //console.log(errorThrown);
		    }
		});
	});
});

$(document).ready(function() {
	$("#children").on('change', function(eventElement) {
		//alert( this.value );
		//send through ajax
		document.getElementById("childrenage1").removeAttribute("disabled");
		document.getElementById("childrenage2").removeAttribute("disabled");
		console.log(this.value);
		if(this.value == "0"){
			document.getElementById("childrenage1").value = "-";
			document.getElementById("childrenage2").value = "-";
			document.getElementById("childrenage1").setAttribute("disabled", "disabled");
			document.getElementById("childrenage2").setAttribute("disabled", "disabled");
		}
		else if(this.value == "1"){
			document.getElementById("childrenage2").value = "-";
			document.getElementById("childrenage1").removeAttribute("disabled");
			document.getElementById("childrenage2").setAttribute("disabled", "disabled");
		}else{
			document.getElementById("childrenage1").removeAttribute("disabled");
			document.getElementById("childrenage2").removeAttribute("disabled");
		}
	});
});

form.addEventListener('submit', handleFormSubmit);

let questOrderDict = {}
function questionOrderToDict(){
	for (let i=0; i<arrayReady.length; i++){
		//questOrderDict[i] = arrayReady[i] + 1
		questOrderDict[arrayReady[i] + 1] = i + 1
	}
}

function submitQuiz(event, eventElement){
	console.log("In Submit")
	event.preventDefault();
	questionOrderToDict();
	quizOrder = JSON.stringify(questOrderDict, null, ' ');
	quizAnswer = JSON.stringify(questSieve, null, ' ');
	quizChoice = JSON.stringify(questAnsw, null, ' ');
	
	//send through ajax
	$.ajax({
		type: 'POST',
		url: $(eventElement).data('url'),
		dataType: 'json',
		data: {
			'id' : 4,
			'userData' : userData,
			'quizOrder' : quizOrder,	
			'quizAnswer' : quizAnswer,
			'quizChoice' : quizChoice,
			'duration' : duration,
			'correctKognitif' : correctKognitif,
			'correctFisik' : correctFisik,
			'correctSosio' : correctSosio,
			'jsonIP' : JSON.stringify(jsonIP, null, ' '),
		},
		success: function (data){
			if (data.msg === "Success"){
				alert('Form is submitted');
			}else{
				alert('AJAX failed');
			}
		},
		complete: function(){
			console.log("Complete Submit Quiz")
		},
		error: function(jqXHR, textStatus, errorThrown) { 
	       //console.log(errorThrown);
	    }
	});
}
btnSubmit = document.getElementById("submitQuiz");
btnSubmit.addEventListener("click", submitQuiz);
/*
$(document).ready(function() {
  var urls = ["../img/bg1.jpg", "../img/bg2.jpg", "../img/bg3.jpg", "../img/bg4.jpg"];
  //var urls = ['https://pp.userapi.com/c629327/v629327473/db66/r051joYFRX0.jpg', 'https://www.codeproject.com/KB/GDI-plus/ImageProcessing2/img.jpg', 'https://img.wikinut.com/img/gycf69_-6rv_5fol/jpeg/0/Best-Friends-Img-Src:Image:-FreeDigitalPhotos.net.jpeg', 'http://www.travelettes.net/wp-content/uploads/2014/03/IMG_3829-Medium-600x400.jpg'];

  var cout = 1;
  //$('body').css('background-image', 'url("' + urls[0] + '")');
  $('body').css('background-image', 'url("../img/bg1.jpg")');
  setInterval(function() {
    $('body').css('background-image', 'url("' + urls[cout] + '")');
    console.log("change")
    cout == urls.length-1 ? cout = 0 : cout++;
  }, 5000);

});
*/
window.onload = function (){
	homeBox.querySelector(".total-question").innerHTML = quiz.length;
	homeBox.querySelector(".quiz-time").innerHTML = quizTime/60 + " minute";
}